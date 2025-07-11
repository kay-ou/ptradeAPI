# Ptrade 策略示例汇总

> 📖 **导航**: [文档库主页](README.md) | [API参考](api-reference/) | [入门指南](getting-started/) | [版本对比](versions/)

基于三个版本API文档整理的策略示例集合。

## 📚 策略分类

### 基础策略示例

#### 1. 简单买卖策略
**适用版本**: 所有版本 (V005, V016, V041)

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 简单的买入逻辑
    if context.portfolio.cash > 10000:
        order(g.security, 100)
```

#### 2. 双均线策略
**适用版本**: 所有版本 (V005, V016, V041)

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    
def handle_data(context, data):
    security = g.security
    
    # 获取历史数据
    df = get_history(10, '1d', 'close', security, fq=None, include=False)
    
    # 计算均线
    ma5 = round(df['close'][-5:].mean(), 3)
    ma10 = round(df['close'][-10:].mean(), 3)
    
    # 交易逻辑
    cash = context.portfolio.cash
    
    if ma5 > ma10:
        order_value(security, cash)
        log.info("Buying %s" % security)
    elif ma5 < ma10 and get_position(security).amount > 0:
        order_target(security, 0)
        log.info("Selling %s" % security)
```

### 高级策略示例

#### 3. 集合竞价追涨停策略
**适用版本**: V016, V041 (需要get_snapshot支持)

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    # 每天9:23分运行集合竞价处理函数
    run_daily(context, aggregate_auction_func, time='9:23')  

def aggregate_auction_func(context):
    stock = g.security
    # 最新价
    snapshot = get_snapshot(stock)
    price = snapshot[stock]['last_px']
    # 涨停价
    up_limit = snapshot[stock]['up_px']
    # 如果最新价不小于涨停价，买入
    if float(price) >= float(up_limit):
        order(g.security, 100, limit_price=up_limit)
        
def handle_data(context, data):
    pass
```

#### 4. MACD策略
**适用版本**: V016, V041 (内置MACD函数) / V005 (手动计算)

**V016/V041版本 (使用内置函数)**:
```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    security = g.security
    
    # 使用内置MACD函数
    macd_data = get_MACD(security, 12, 26, 9)
    
    if macd_data:
        dif = macd_data['DIF'][-1]
        dea = macd_data['DEA'][-1]
        
        cash = context.portfolio.cash
        
        # DIF上穿DEA，买入信号
        if dif > dea and len(macd_data['DIF']) > 1:
            if macd_data['DIF'][-2] <= macd_data['DEA'][-2]:
                order_value(security, cash)
                log.info("MACD买入信号: %s" % security)
        
        # DIF下穿DEA，卖出信号
        elif dif < dea and get_position(security).amount > 0:
            if len(macd_data['DIF']) > 1 and macd_data['DIF'][-2] >= macd_data['DEA'][-2]:
                order_target(security, 0)
                log.info("MACD卖出信号: %s" % security)
```

**V005版本 (手动计算)**:
```python
def f_expma(N, m, EXPMA1, price):
    a = m/(N+1)
    EXPMA2 = a * price + (1 - a)*EXPMA1
    return EXPMA2

def macd(N1, N2, N3, m, EXPMA12_1, EXPMA26_1, DEA1, price):
    EXPMA12_2 = f_expma(N1, m, EXPMA12_1, price)
    EXPMA26_2 = f_expma(N2, m, EXPMA26_1, price)
    DIF2 = EXPMA12_2 - EXPMA26_2
    a = m/(N3+1)
    DEA2 = a * DIF2 + (1 - a)*DEA1
    BAR2 = 2*(DIF2-DEA2)
    return EXPMA12_2, EXPMA26_2, DIF2, DEA2, BAR2

def initialize(context):
    global init_price
    init_price = None
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    security = g.security
    close_price = get_history(2, '1d', field='close', security_list=[security])
    
    global init_price, EXPMA12_1, EXPMA26_1, DIF1, DEA1
    
    if init_price is None:
        init_price = close_price[security].mean()
        EXPMA12_1 = init_price
        EXPMA26_1 = init_price
        DIF1 = init_price
        DEA1 = init_price
    
    m = 2.0
    N1, N2, N3 = 12, 26, 9
    
    EXPMA12_2, EXPMA26_2, DIF2, DEA2, BAR2 = macd(
        N1, N2, N3, m, EXPMA12_1, EXPMA26_1, DEA1, close_price[security][-1])
    
    current_price = data[security].price
    cash = context.portfolio.cash
    
    # MACD交易逻辑
    if DIF2 > 0 and DEA2 > 0 and DIF1 < DEA1 and DIF2 > DEA2:
        number_of_shares = int(cash/current_price)
        if number_of_shares > 0:
            order(security, +number_of_shares)
            log.info("MACD买入: %s" % security)
    
    elif DIF2 < 0 and DEA2 < 0 and DIF1 > DEA1 and DIF2 < DEA2 and get_position(security).amount > 0:
        order_target(security, 0)
        log.info("MACD卖出: %s" % security)
    
    # 更新全局变量
    DEA1 = DEA2
    DIF1 = DIF2
    EXPMA12_1 = EXPMA12_2
    EXPMA26_1 = EXPMA26_2
```

### 专业策略示例

#### 5. 融资融券双均线策略
**适用版本**: 所有版本 (V005, V016, V041)

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def before_trading_start(context, data):
    g.order_buy_flag = False
    g.order_sell_flag = False

def handle_data(context, data):
    # 获取历史数据
    df = get_history(10, "1d", "close", g.security, fq=None, include=False)
    ma5 = round(df["close"][-5:].mean(), 3)
    ma10 = round(df["close"][-10:].mean(), 3)
    
    # 融资买入
    if ma5 > ma10:
        if not g.order_buy_flag:
            amount = get_margincash_open_amount(g.security).get(g.security)
            margincash_open(g.security, amount)
            log.info("融资买入 %s Amount %s" % (g.security, amount))
            g.order_buy_flag = True

    # 卖券还款
    elif ma5 < ma10 and get_position(g.security).amount > 0:
        if not g.order_sell_flag:
            amount = get_margincash_close_amount(g.security).get(g.security)
            margincash_close(g.security, -amount)
            log.info("卖券还款 %s Amount %s" % (g.security, amount))
            g.order_sell_flag = True
```

#### 6. 可转债套利策略
**适用版本**: V005, V041 (支持get_cb_info) / V016 (需要手动实现)

**V005/V041版本**:
```python
def initialize(context):
    # 获取可转债列表
    g.cb_list = get_cb_list()
    set_universe(g.cb_list[:10])  # 选择前10只可转债

def handle_data(context, data):
    for cb_code in g.cb_list[:10]:
        # 获取可转债信息
        cb_info = get_cb_info(cb_code)
        
        if cb_info:
            # 转股价值
            conversion_value = cb_info.get('conversion_value', 0)
            # 可转债价格
            cb_price = data[cb_code]['close']
            
            # 套利逻辑：转股价值高于可转债价格一定比例时买入
            if conversion_value > cb_price * 1.05:
                order_value(cb_code, 10000)
                log.info("可转债套利买入: %s" % cb_code)
            
            # 平仓逻辑
            elif conversion_value < cb_price * 0.98 and get_position(cb_code).amount > 0:
                order_target(cb_code, 0)
                log.info("可转债套利卖出: %s" % cb_code)
```

### Tick级别策略示例

#### 7. Tick级别均线策略
**适用版本**: V016, V041 (交易模块支持tick_data)

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    # 每3秒运行一次主函数
    run_interval(context, func, seconds=3)
      
def before_trading_start(context, data):
    history = get_history(10, '1d', 'close', g.security, fq='pre', include=False)
    g.close_array = history['close'].values
    
def func(context):
    stock = g.security
    
    # 获取最新价
    snapshot = get_snapshot(stock)
    price = snapshot[stock]['last_px']
    
    # 计算实时均线
    ma5 = get_MA_day(stock, 5, g.close_array[-4:], price)   
    ma10 = get_MA_day(stock, 10, g.close_array[-9:], price)

    cash = context.portfolio.cash
    
    if ma5 > ma10:
        order_value(stock, cash)
        log.info("Tick买入 %s" % stock)
    elif ma5 < ma10 and get_position(stock).amount > 0:
        order_target(stock, 0)
        log.info("Tick卖出 %s" % stock)    

def get_MA_day(stock, days, close_array, current_price):
    close_sum = close_array[-(days-1):].sum()
    MA = (current_price + close_sum)/days
    return MA

def handle_data(context, data):
    pass
```

## 🔧 版本特定功能示例

### V005 (社区维护) 独有功能

#### 企业微信推送
```python
def handle_data(context, data):
    # 交易后发送企业微信通知
    if get_position(g.security).amount > 0:
        message = f"已买入 {g.security}"
        send_qywx(message)
```

#### 资金调拨
```python
def initialize(context):
    # 设置资金调拨
    fund_transfer(10000, 'A', 'B')  # 从A账户调拨10000到B账户
```

### V016/V041 (券商版本) 独有功能

#### 技术指标组合策略
```python
def handle_data(context, data):
    security = g.security
    
    # 获取多个技术指标
    macd = get_MACD(security, 12, 26, 9)
    kdj = get_KDJ(security, 9, 3, 3)
    rsi = get_RSI(security, 14)
    
    # 多指标确认
    if (macd['DIF'][-1] > macd['DEA'][-1] and 
        kdj['K'][-1] > kdj['D'][-1] and 
        rsi['RSI'][-1] < 70):
        
        order_value(security, context.portfolio.cash)
        log.info("多指标买入信号: %s" % security)
```

## 📖 使用指南

### 策略选择建议

1. **新手入门**: 从简单买卖策略和双均线策略开始
2. **进阶学习**: 尝试MACD策略和融资融券策略
3. **专业应用**: 使用可转债套利和Tick级别策略

### 版本兼容性

- **V005**: 适合学习和研究，功能丰富
- **V016**: 适合稳定交易，标准功能
- **V041**: 适合专业交易，最新功能

## 🚀 回测优化技巧

### 性能优化建议

#### 1. 减少在线接口调用
```python
def initialize(context):
    # 在初始化时获取一次性数据
    g.stock_list = get_Ashares()  # 只调用一次
    g.fundamentals_cache = {}

def before_trading_start(context, data):
    # 在开盘前处理日频数据
    for stock in g.stock_list:
        fundamental = get_fundamentals(stock, 'valuation', 'pe_dynamic')
        g.fundamentals_cache[stock] = fundamental

def handle_data(context, data):
    # 使用缓存的数据，避免重复调用
    for stock in g.stock_list:
        pe = g.fundamentals_cache.get(stock, 0)
        if pe > 0 and pe < 30:
            order_value(stock, 10000)
```

#### 2. 优化历史数据获取
```python
def initialize(context):
    g.history_cache = {}

def get_optimized_history(security, count, frequency):
    """优化的历史数据获取"""
    cache_key = f"{security}_{count}_{frequency}"

    # 检查缓存是否存在且未过期
    if cache_key in g.history_cache:
        cached_data, cache_time = g.history_cache[cache_key]
        # 如果是同一天的数据，直接使用缓存
        if cache_time.date() == context.current_dt.date():
            return cached_data

    # 获取新数据并缓存
    data = get_history(count, frequency, 'close', security)
    g.history_cache[cache_key] = (data, context.current_dt)

    return data
```

#### 3. 批量处理优化
```python
def handle_data(context, data):
    # 批量获取快照数据
    securities = ['600570.SS', '000001.SZ', '000002.SZ']
    snapshots = get_snapshot(securities)  # 一次获取多个

    # 批量处理
    orders = []
    for security in securities:
        if snapshots[security]:
            price = snapshots[security]['last_px']
            if price > 0:
                orders.append((security, 100, price))

    # 批量下单
    for security, amount, price in orders:
        order(security, amount, limit_price=price)
```

### 调试功能使用

#### 1. 分步调试
```python
def handle_data(context, data):
    # 设置断点进行调试
    security = '600570.SS'

    # 检查数据完整性
    assert security in data, f"股票 {security} 不在数据中"

    # 获取价格数据
    current_price = data[security].price
    log.info(f"当前价格: {current_price}")

    # 计算技术指标
    ma5 = get_history(5, '1d', 'close', security).mean()
    log.info(f"5日均线: {ma5}")

    # 交易逻辑
    if current_price > ma5:
        order_value(security, 10000)
        log.info(f"买入 {security}")
```

#### 2. 性能分析
```python
import time

def handle_data(context, data):
    start_time = time.time()

    # 策略逻辑
    for security in context.universe:
        # 记录各部分耗时
        data_start = time.time()
        price_data = get_history(10, '1d', 'close', security)
        data_time = time.time() - data_start

        calc_start = time.time()
        ma = price_data.mean()
        calc_time = time.time() - calc_start

        if data[security].price > ma:
            order_value(security, 10000)

    total_time = time.time() - start_time
    log.info(f"总耗时: {total_time:.3f}s")
```

### 回测配置优化

#### 1. 成交模式设置
```python
def initialize(context):
    # 设置成交模式
    set_limit_mode(True)  # 受成交量限制，更真实
    # set_limit_mode(False)  # 不受限制，适合低频策略

    # 设置成交比例
    set_volume_ratio(0.25)  # 最多成交25%的分钟成交量

    # 设置滑点
    set_slippage(FixedSlippage(0.002))  # 0.2%固定滑点
```

#### 2. 数据频率优化
```python
def initialize(context):
    # 对于日线策略，在before_trading_start处理数据
    pass

def before_trading_start(context, data):
    # 获取日线数据，避免在handle_data中重复获取
    g.daily_data = {}
    for security in context.universe:
        g.daily_data[security] = get_history(20, '1d', 'close', security)

def handle_data(context, data):
    # 使用预处理的日线数据
    for security in context.universe:
        daily_close = g.daily_data[security]
        ma20 = daily_close.mean()

        if data[security].price > ma20:
            order_value(security, 10000)
```

### 风险提示

- 所有策略仅供学习参考
- 实盘交易前请充分测试
- 注意风险控制和资金管理
- 使用调试功能时注意性能影响

---

## 📚 相关文档

- [**API参考文档**](api-reference/) - 查看示例中使用的API详细说明
- [**入门指南**](getting-started/) - 从基础开始学习Ptrade
- [**版本差异对比**](version-differences.md) - 了解不同版本的功能差异
- [**常见问题**](advanced/faq.md) - 策略开发中的常见问题解答

> 🔙 **返回**: [文档库主页](README.md) | [完整API分类](api-classification.md)

---

> **更新**: 基于三个版本的实际API差异整理
> **来源**: 官方文档和社区贡献
