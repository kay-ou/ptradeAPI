# 常见问题

本文档收集了使用 Ptrade API 过程中的常见问题和解决方案。

## 基础问题

### Q: 如何开始使用 Ptrade API？

A: 请按照以下步骤开始：
1. 阅读[使用说明](../getting-started/usage.md)了解基本概念
2. 查看[快速入门](../getting-started/quick-start.md)学习编写第一个策略
3. 参考[策略示例](../getting-started/examples.md)了解完整的策略结构

### Q: 策略必须包含哪些函数？

A: 一个完整的策略必须包含：
- `initialize(context)` - 初始化函数（必选）
- `handle_data(context, data)` - 主逻辑函数（必选）

可选函数包括：
- `before_trading_start(context, data)` - 盘前处理
- `after_trading_end(context, data)` - 盘后处理
- `tick_data(context, data)` - tick级别处理

### Q: 如何设置股票池？

A: 使用 `set_universe()` 函数：
```python
def initialize(context):
    # 单只股票
    set_universe('600570.SS')
    
    # 多只股票
    set_universe(['600570.SS', '000001.SZ'])
```

## 数据相关问题

### Q: 如何获取历史行情数据？

A: 使用 `get_history()` 函数：
```python
# 获取过去10天的收盘价
hist = get_history(10, '1d', 'close', '600570.SS')

# 获取过去30分钟的OHLC数据
hist = get_history(30, '1m', ['open', 'high', 'low', 'close'], '600570.SS')
```

### Q: 如何获取实时行情数据？

A: 在 `handle_data` 函数中通过 `data` 参数获取：
```python
def handle_data(context, data):
    # 获取当前价格
    current_price = data['600570.SS']['close']
    
    # 或使用 get_snapshot() 获取更详细的实时数据
    snapshot = get_snapshot('600570.SS')
    price = snapshot['600570.SS']['last_px']
```

### Q: 数据中的股票代码格式是什么？

A: 股票代码格式为：代码.交易所
- 上海证券交易所：600570.SS
- 深圳证券交易所：000001.SZ

### Q: 支持哪些数据种类？

A: 在研究、回测、交易模块均可调用2005年以来的历史财务数据以及历史行情数据，包含分钟、日线、周线不同周期数据。交易场景还支持tick级别行情快照数据。数据支持股票、可转债、指数等多品种。

### Q: 如何进行数据读写？

A: 研究环境可以存放文件，根目录路径为'/home/fly/notebook/'，可通过get_research_path接口获取。回测和交易中均可以通过该路径进行策略中的读写等操作，从而实现数据的保存和读取。

### Q: 可以访问本地数据吗？

A: 由于PTrade为云端部署，策略中是无法与本地路径进行直接交互的。

### Q: 行情数据复权如何处理？

A: PTrade行情数据支持不复权、前复权、后复权、动态前复权四种取历史行情数据的方法，但要注意的是回测中回测引擎撮合的价格是不复权的，因此可以通过除权因子进行价格除权处理。

### Q: 是否提供Level2数据？

A: 云纪网络的仿真环境不提供level2数据，券商环境是否提供，由所在券商决定。

### Q: 文件传输有什么限制？

A:
- 单个文件手动上传下载目前限制单个文件数据大小不超过50M
- 暂时不支持文件夹上传，文件需要逐个上传
- 定时上传功能可以实现研究环境自动从本地路径读取文件，但上传次数是有限制的（具体由券商配置决定）

## 交易相关问题

### Q: 如何下单买卖股票？

A: 使用 order 系列函数：
```python
# 按数量下单
order('600570.SS', 100)  # 买入100股

# 按金额下单
order_value('600570.SS', 10000)  # 买入1万元

# 调整到目标持仓
order_target('600570.SS', 1000)  # 调整到持有1000股
```

### Q: 如何查看当前持仓？

A: 使用 `get_position()` 函数：
```python
def handle_data(context, data):
    # 获取单只股票持仓
    position = get_position('600570.SS')
    log.info('持仓数量: %d' % position.amount)
    
    # 获取所有持仓
    positions = get_positions()
    for stock, pos in positions.items():
        log.info('%s 持仓: %d' % (stock, pos.amount))
```

### Q: 如何撤销订单？

A: 使用 `cancel_order()` 函数：
```python
# 下单后获取订单ID
order_id = order('600570.SS', 100)

# 撤销订单
cancel_order(order_id)
```

### Q: 可以同时运行多少个交易？

A: 默认允许同时运行5个交易，具体以券商配置为准。

### Q: 交易过程可以客户端离线吗？

A: 交易在服务器上运行，因此客户端关闭或掉线并不影响策略运行。

### Q: 不同交易的账户如何管理？

A: 所有运行的模拟交易或实盘交易都共享一个账户（资金、持仓无法隔离），暂不支持子账户交易系统。

### Q: 交易什么时候可以开启？

A: 交易在任何时间都可以开启，开启后会立刻运行initialize和before_trading_start（如果策略中定义的话）。要注意的是：开盘前开启交易，before_trading_start肯定会先于handle_data开启；但开盘期间开启交易，before_trading_start和handle_data可能会同时运行。

### Q: 策略中模块的运行顺序是什么？

A: 交易中before_trading_start、handle_data、tick_data、run_interval都是独立的线程，当交易开启之后，每个线程都会启动，理论上没有先后顺序关系。因此建议在策略中设置强制顺序的控制系统。

### Q: 回测与交易代码如何兼容？

A: 由于交易中支持tick数据以及市价单下单，因此大多数情况下回测和交易在代码设计上会有不同。为了减少代码维护的难度，PTrade量化提供了is_trade接口。通过该接口，用户可以在一套代码中兼容回测和交易两种逻辑。

### Q: 如何保证模拟交易的稳定性？

A: 常见的影响交易稳定性的因素来自于几方面：
1. **历史行情K线数据服务器更新异常** - 可以通过比较入参的K线数量、实际返回数据框的长度、时间戳index去重后的返回数据框的长度来做判断
2. **实时行情数据获取失败** - 需要做数据保护，进行非空判断和字段数据保护
3. **财务数据获取失败** - 建议加入重连机制做保护
4. **服务器环境异常** - 可以通过持久化处理，让策略在短暂停止后重新拉起并保持原有的策略逻辑连贯

### Q: 账户数据更新频率是多少？

A: 模拟交易和实盘交易的账户数据同步理论上是6秒一次，包括资金、持仓、订单状态、撤单状态等。因此用户需要自建一定的中间变量做过渡，防止重复交易或者重复判断。

### Q: 委托数量有什么要求？

A: 委托接口有委托数量校验，如果数量不是整数，会下单失败返回None。

### Q: 支持集合竞价下单吗？

A: 已支持集合竞价下单。

### Q: 如何监控委托状态？

A: get_orders接口可以获取当日本策略的所有订单信息（6秒同步更新），交易模块还可调用on_trade_response接口获取成交回报主推。

### Q: 可以撤销手动委托单吗？

A: 通过get_all_orders接口获取账户当日全部订单，再结合cancel_order_ex撤单接口，可以对手动委托单进行撤单。

### Q: 什么是隔夜单？

A: 每个交易日15:00之后，通过order、order_target、order_value、order_target_value、order_market这五个接口处理的委托订单都会放到委托队列，第二天9:15分报给柜台。

### Q: 如何开通实盘交易？

A: 向开展PTrade量化业务的所在券商进行申请。

### Q: 实盘与模拟交易有什么区别？

A: 模拟交易和实盘交易在数据获取的机制上是一致的，只是成交撮合机制不同。

## 策略运行问题

### Q: 策略运行频率如何设置？

A: 策略运行频率在创建策略时设置：
- 日线级别：每天运行一次
- 分钟级别：每分钟运行一次
- tick级别：需要使用 `run_interval()` 或 `tick_data()` 函数

### Q: 如何在特定时间执行函数？

A: 使用 `run_daily()` 函数：
```python
def initialize(context):
    # 每天9:30执行开盘函数
    run_daily(context, market_open_func, time='9:30')
    
    # 每天15:00执行收盘函数
    run_daily(context, market_close_func, time='15:00')
```

### Q: 全局变量如何使用？

A: 使用 `g` 对象存储全局变量：
```python
def initialize(context):
    g.security = '600570.SS'
    g.buy_signal = False
    
def handle_data(context, data):
    if g.buy_signal:
        order(g.security, 100)
```

## 回测相关问题

### Q: 回测与研究有什么区别？

A:
- **研究环境**: 更侧重于数据的清洗、处理、建模、画图、debug调试等，类似于本地的Python编程，无法调用诸如order下单，账户资产等与交易相关的函数
- **回测环境**: 更适用于完成完整的交易策略搭建、参数调优、历史收益回测等，更贴近交易

### Q: 可以同时进行多少个回测？

A: 目前支持同时进行5个回测。

### Q: 如何提高回测速度？

A:
1. PTrade量化中部分接口为在线调用接口，比如get_fundamentals、get_Ashares，回测中按实际需求尽量少频次地调用这类在线调用接口
2. 分钟级别策略中如果用到日频的历史数据，在before_trading_start模块处理一次就可以，这样可以提升回测的速度

### Q: 支持哪些回测周期？

A: 目前回测只支持分钟和日线周期的回测。

### Q: 是否支持离线回测？

A: PTrade量化平台目前不支持离线回测，回测期间必须保障客户端打开。

### Q: 回测撮合是否受真实成交限制？

A: 回测提供了两种成交撮合方式，通过set_limit_mode接口控制：
- 一种是按初始化设定的分钟成交量比例进行成交撮合
- 另一种是不受分钟成交量限制
前者可以较为真实地反映流动性对策略的影响，后者比较适合低频调仓策略。

### Q: 如何获取每次回测代码？

A: 在回测记录中找到目标回测记录，在'操作'栏中点击详情按钮获得回测代码。

### Q: 如何设置回测参数？

A: 在 `initialize()` 函数中设置：
```python
def initialize(context):
    # 设置基准
    set_benchmark('000300.SS')

    # 设置佣金
    set_commission(commission_ratio=0.0003, min_commission=5.0)

    # 设置滑点
    set_slippage(slippage=0.002)
```

### Q: 如何查看回测结果？

A: 回测完成后，系统会自动显示：
- 收益曲线图
- 策略评价指标
- 交易明细
- 持仓变化

### Q: 什么是调试功能？

A: 量化分步调试功能可以帮助开发者更高效地debug策略代码。该功能在回测模块中，支持调用堆栈查询、变量监视、本地变量查询功能。

### Q: 什么是性能分析？

A: 性能分析功能会对运行结果做分析，包括语句的触发次数和耗时情况，能够帮助用户快速地做策略性能优化。

## 错误处理

### Q: 遇到 "股票不在股票池中" 错误怎么办？

A: 确保在交易前已经将股票添加到股票池：
```python
def initialize(context):
    set_universe(['600570.SS', '000001.SZ'])
```

### Q: 遇到 "资金不足" 错误怎么办？

A: 检查账户余额和下单金额：
```python
def handle_data(context, data):
    cash = context.portfolio.cash
    if cash > 10000:  # 确保有足够资金
        order_value('600570.SS', 10000)
```

### Q: 如何调试策略？

A: 使用 `log.info()` 输出调试信息：
```python
def handle_data(context, data):
    price = data['600570.SS']['close']
    log.info('当前价格: %.2f' % price)
    
    position = get_position('600570.SS')
    log.info('当前持仓: %d' % position.amount)
```

## 性能优化

### Q: 如何提高策略运行速度？

A: 
1. 减少不必要的数据获取
2. 避免在循环中重复计算
3. 使用合适的数据结构
4. 缓存计算结果

### Q: 如何处理大量股票的策略？

A: 
1. 分批处理股票列表
2. 使用向量化计算
3. 避免频繁的数据库查询
4. 合理设置股票池大小

## 技术细节问题

### Q: 如何快速获取最新价？

A:
- 在回测中建议用 `data[stock].price`（注意这种方法取到的是不复权数据）
- 交易中用 `get_snapshot` 接口获取行情快照的最新价

### Q: 日线策略什么时候运行？

A:
- 回测中是15:00执行
- 交易中默认设置是14:50分，具体看所在券商的配置

### Q: get_history中的include参数如何使用？

A: get_history中的include参数默认为False，如果设置为True，则返回包含当前周期的数据。日线周期（或以上级别）策略的回测场景设置include参数为True获取当日数据，可以使得回测更加快速便捷，其他场景建议谨慎使用该参数。

### Q: 基准可以设置为什么？

A: 基准支持设置为指数/个股/ETF，可参阅set_benchmark。

### Q: 如何实现跨周期处理？

A: 可以通过run_interval和handle_data相结合实现，根据策略逻辑进行编写。

### Q: tick_data和run_interval有什么关系？

A: tick_data和run_interval都可以实现tick级别周期策略：
- tick_data固定3秒一个间隔
- run_interval可以随意设置运行间隔时间，最小间隔3秒
- 数据源也都是行情快照数据，因此可以选择其一进行策略设计

### Q: 批量委托性能如何？

A: 策略发起委托到柜台接收的速度，测试结果：300笔委托耗时2秒。

### Q: 如何将信号推送给自己？

A: 可通过邮件、企业微信接口实现，因该业务需要开通外网，实际看券商环境是否支持。

### Q: 策略上传和下载如何保证安全？

A: PTrade量化平台所创建的策略是可以加密下载和上传的，利用AES/DES加密技术对文件流进行加密处理，随机生成盐值进行干扰混淆，保障上传与下载安全私密性。该功能的用途在于支持同一策略在不同账户上实现隐藏代码地进行模拟交易。

### Q: 研究环境资源有限制吗？

A: 目前单个的客户研究环境资源没有上限。

## 技术支持

如果以上问题无法解决您的问题，请：

1. 查看[API参考文档](../api-reference/)获取详细说明
2. 检查[策略示例](../getting-started/examples.md)寻找类似用法
3. 联系技术支持团队

## 更多资源

- [使用说明](../getting-started/usage.md)
- [快速入门](../getting-started/quick-start.md)
- [API参考](../api-reference/)
- [支持的三方库](supported-libraries.md)
