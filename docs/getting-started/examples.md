# 策略示例

本文档提供了一些完整的策略示例，帮助您快速理解如何使用 Ptrade API 编写量化交易策略。

## 集合竞价追涨停策略

这个策略在集合竞价阶段检测涨停股票并进行买入。

```python
def initialize(context):
    # 初始化此策略
    # 设置我们要操作的股票池, 这里我们只操作一支股票
    g.security = '600570.SS'
    set_universe(g.security)
    #每天9:23分运行集合竞价处理函数
    run_daily(context, aggregate_auction_func, time='9:23')  

def aggregate_auction_func(context):
    stock = g.security
    #最新价
    snapshot = get_snapshot(stock)
    price = snapshot[stock]['last_px']
    #涨停价
    up_limit = snapshot[stock]['up_px']
    #如果最新价不小于涨停价，买入
    if float(price) >= float(up_limit):
        order(g.security, 100, limit_price=up_limit)
    
def handle_data(context, data):
    pass
```

## tick级别均线策略

这个策略使用tick级别数据，基于5日和10日均线进行交易决策。

```python
def initialize(context):
    # 初始化此策略
    # 设置我们要操作的股票池, 这里我们只操作一支股票
    g.security = '600570.SS'
    set_universe(g.security)
    #每3秒运行一次主函数
    run_interval(context, func, seconds=3)
      
#盘前准备历史数据
def before_trading_start(context, data):
    history = get_history(10, '1d', 'close', g.security, fq='pre', include=False)
    g.close_array = history['close'].values
    
#当五日均线高于十日均线时买入，当五日均线低于十日均线时卖出
def func(context):
    
    stock = g.security
    
    #获取最新价
    snapshot = get_snapshot(stock)
    price = snapshot[stock]['last_px']
    
    # 得到五日均线价格
    days = 5
    ma5 = get_MA_day(stock, days, g.close_array[-4:], price)   
    # 得到十日均线价格
    days = 10
    ma10 = get_MA_day(stock, days, g.close_array[-9:], price)

    # 得到当前资金余额
    cash = context.portfolio.cash
    
    # 如果当前有余额，并且五日均线大于十日均线
    if ma5 > ma10:
        # 用所有 cash 买入股票
        order_value(stock, cash)
        # 记录这次买入
        log.info("Buying %s" % (stock))
        
    # 如果五日均线小于十日均线，并且目前有头寸
    elif ma5 < ma10 and get_position(stock).amount > 0:
        # 全部卖出
        order_target(stock, 0)
        # 记录这次卖出
        log.info("Selling %s" % (stock))

def get_MA_day(stock, days, close_array, price):
    """
    计算移动平均线
    """
    # 将最新价格加入历史价格数组
    prices = list(close_array) + [price]
    # 计算指定天数的移动平均
    if len(prices) >= days:
        return sum(prices[-days:]) / days
    else:
        return sum(prices) / len(prices)

def handle_data(context, data):
    pass
```

## 双均线策略

经典的双均线策略，使用日线数据进行交易。

```python
def initialize(context):
    # 设置股票池
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    stock = g.security
    
    # 获取历史数据
    hist = get_history(20, '1d', 'close', stock, fq='pre', include=False)
    
    # 计算5日和20日移动平均线
    ma5 = hist['close'][-5:].mean()
    ma20 = hist['close'][-20:].mean()
    
    # 获取当前价格
    current_price = data[stock]['close']
    
    # 获取当前持仓
    position = get_position(stock)
    
    # 买入信号：5日均线上穿20日均线，且当前价格高于5日均线
    if ma5 > ma20 and current_price > ma5 and position.amount == 0:
        # 全仓买入
        order_value(stock, context.portfolio.cash)
        log.info('买入信号触发，买入 %s' % stock)
    
    # 卖出信号：5日均线下穿20日均线
    elif ma5 < ma20 and position.amount > 0:
        # 全部卖出
        order_target(stock, 0)
        log.info('卖出信号触发，卖出 %s' % stock)
```

## MACD策略

使用MACD技术指标进行交易决策的策略。

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    stock = g.security
    
    # 获取历史数据
    hist = get_history(50, '1d', 'close', stock, fq='pre', include=False)
    
    # 计算MACD指标
    macd_data = get_MACD(hist['close'].values)
    
    # 获取MACD线、信号线和柱状图
    macd_line = macd_data['macd'][-1]
    signal_line = macd_data['signal'][-1]
    histogram = macd_data['histogram'][-1]
    
    # 获取前一天的数据用于判断金叉死叉
    prev_macd = macd_data['macd'][-2]
    prev_signal = macd_data['signal'][-2]
    
    # 获取当前持仓
    position = get_position(stock)
    
    # 金叉买入信号：MACD线从下方穿越信号线
    if prev_macd <= prev_signal and macd_line > signal_line and position.amount == 0:
        order_value(stock, context.portfolio.cash)
        log.info('MACD金叉，买入 %s' % stock)
    
    # 死叉卖出信号：MACD线从上方穿越信号线
    elif prev_macd >= prev_signal and macd_line < signal_line and position.amount > 0:
        order_target(stock, 0)
        log.info('MACD死叉，卖出 %s' % stock)
```

## 融资融券双均线策略

使用融资融券功能的双均线策略示例。

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    stock = g.security
    
    # 获取历史数据
    hist = get_history(20, '1d', 'close', stock, fq='pre', include=False)
    
    # 计算移动平均线
    ma5 = hist['close'][-5:].mean()
    ma10 = hist['close'][-10:].mean()
    
    # 获取当前价格
    current_price = data[stock]['close']
    
    # 获取当前持仓
    position = get_position(stock)
    
    # 多头信号：5日均线上穿10日均线
    if ma5 > ma10 and position.amount <= 0:
        if position.amount < 0:
            # 先平空头仓位
            marginsec_close(stock, abs(position.amount))
            log.info('平空头仓位 %s' % stock)
        # 融资买入
        margincash_open(stock, 1000)
        log.info('融资买入 %s' % stock)
    
    # 空头信号：5日均线下穿10日均线
    elif ma5 < ma10 and position.amount >= 0:
        if position.amount > 0:
            # 先平多头仓位
            margincash_close(stock, position.amount)
            log.info('平多头仓位 %s' % stock)
        # 融券卖出
        marginsec_open(stock, 1000)
        log.info('融券卖出 %s' % stock)
```

## 策略要点总结

1. **初始化函数**：在 `initialize` 中设置股票池、全局变量等
2. **主逻辑函数**：在 `handle_data` 中实现主要的交易逻辑
3. **技术指标**：合理使用各种技术指标进行信号判断
4. **风险控制**：注意仓位管理和止损设置
5. **日志记录**：使用 `log.info` 记录重要的交易决策

## 下一步

- [API参考文档](../api-reference/) - 查看详细的API说明
- [常见问题](../advanced/faq.md) - 解决开发中的常见问题
