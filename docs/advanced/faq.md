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
