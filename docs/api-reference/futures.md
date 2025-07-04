# 期货交易API

本文档介绍期货交易相关的API函数，包括开仓、平仓、查询等功能。

## 期货交易函数

### buy_open - 多开

```python
buy_open(contract, amount, limit_price=None)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

买入开仓

注意：

1. 不同期货品种每一跳的价格变动都不一样，limit_price入参的时候要参考对应品种的价格变动规则
2. 如limit_price不做入参则会以交易的行情快照最新价或者回测的分钟最新价进行报单
3. 根据交易所规则，每天结束时会取消所有未完成交易

#### 参数

contract：期货合约代码(str)；

amount：交易数量，正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None

#### 示例

```python
def initialize(context):
    g.security = ['IF2312.CCFX']
    set_universe(g.security)

def handle_data(context, data):
    # 买入开仓
    buy_open('IF2312.CCFX', 1)
    # 指定价格买入开仓
    buy_open('IF2312.CCFX', 1, limit_price=4500.0)
```

### sell_close - 多平

```python
sell_close(contract, amount, limit_price=None, close_today=False)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

卖出平仓

注意：

1. 不同期货品种每一跳的价格变动都不一样，limit_price入参的时候要参考对应品种的价格变动规则
2. 如limit_price不做入参则会以交易的行情快照最新价或者回测的分钟最新价进行报单
3. 根据交易所规则，每天结束时会取消所有未完成交易

#### 参数

contract：期货合约代码(str)；

amount：交易数量，正数(int)；

limit_price：买卖限价(float)；

close_today：平仓方式(bool)。close_today=False为优先平昨仓，不足部分再平今仓；close_today=True为仅平今仓，委托数量若大于今仓系统会调整为今仓数量。close_today=True仅对上海期货交易所生效，其他交易所无需入参close_today字段；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None

#### 示例

```python
def initialize(context):
    g.security = ['IF2312.CCFX']
    set_universe(g.security)

def handle_data(context, data):
    # 卖出平仓
    sell_close('IF2312.CCFX', 1)
    # 平今仓
    sell_close('IF2312.CCFX', 1, close_today=True)
```

### sell_open - 空开

```python
sell_open(contract, amount, limit_price=None)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

卖出开仓

注意：

1. 不同期货品种每一跳的价格变动都不一样，limit_price入参的时候要参考对应品种的价格变动规则
2. 如limit_price不做入参则会以交易的行情快照最新价或者回测的分钟最新价进行报单
3. 根据交易所规则，每天结束时会取消所有未完成交易

#### 参数

contract：期货合约代码(str)；

amount：交易数量，正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None

#### 示例

```python
def initialize(context):
    g.security = ['IF2312.CCFX']
    set_universe(g.security)

def handle_data(context, data):
    # 卖出开仓
    sell_open('IF2312.CCFX', 1)
    # 指定价格卖出开仓
    sell_open('IF2312.CCFX', 1, limit_price=4400.0)
```

### buy_close - 空平

```python
buy_close(contract, amount, limit_price=None, close_today=False)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

买入平仓

注意：

1. 不同期货品种每一跳的价格变动都不一样，limit_price入参的时候要参考对应品种的价格变动规则
2. 如limit_price不做入参则会以交易的行情快照最新价或者回测的分钟最新价进行报单
3. 根据交易所规则，每天结束时会取消所有未完成交易

#### 参数

contract：期货合约代码(str)；

amount：交易数量，正数(int)；

limit_price：买卖限价(float)；

close_today：平仓方式(bool)。close_today=False为优先平昨仓，不足部分再平今仓；close_today=True为仅平今仓，委托数量若大于今仓系统会调整为今仓数量。close_today=True仅对上海期货交易所生效，其他交易所无需入参close_today字段；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None

#### 示例

```python
def initialize(context):
    g.security = ['IF2312.CCFX']
    set_universe(g.security)

def handle_data(context, data):
    # 买入平仓
    buy_close('IF2312.CCFX', 1)
    # 平今仓
    buy_close('IF2312.CCFX', 1, close_today=True)
```

## 期货设置函数

### set_margin_rate - 设置保证金比例

```python
set_margin_rate(transaction_code, margin_rate)
```

#### 使用场景

该函数仅在回测模块可用

#### 接口说明

设置期货合约的保证金比例

#### 参数

transaction_code：期货合约的交易代码，str类型，如沪铜2112（"CU2112"）的交易代码为"CU"；

margin_rate：保证金比例，float类型，如0.08表示8%；

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = "IF2312.CCFX"
    set_universe(g.security)
    # 设置沪深300指数的保证金比例为8%
    set_margin_rate("IF", 0.08)
    # 设置5年期国债的保证金比例为2%
    set_margin_rate("TF", 0.02)

def handle_data(context, data):
    pass
```

### set_future_commission - 设置期货手续费

```python
set_future_commission(transaction_code, commission_ratio=0.0, commission_per_lot=0.0, commission_type='ratio')
```

#### 使用场景

该函数仅在回测模块可用

#### 接口说明

设置期货合约的手续费

#### 参数

transaction_code：期货合约的交易代码(str)；

commission_ratio：手续费比例(float)；

commission_per_lot：每手手续费(float)；

commission_type：手续费类型，'ratio'表示按比例，'per_lot'表示按手数(str)；

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = "IF2312.CCFX"
    set_universe(g.security)
    # 设置沪深300指数手续费为万分之0.25
    set_future_commission("IF", commission_ratio=0.000025)

def handle_data(context, data):
    pass
```

## 期货查询函数

### get_margin_rate - 获取保证金比例

```python
get_margin_rate(transaction_code)
```

#### 使用场景

该函数仅在回测模块可用

#### 接口说明

获取用户设置的保证金比例

#### 参数

transaction_code：期货合约的交易代码，str类型，如沪铜2112（"CU2112"）的交易代码为"CU"；

#### 返回

用户设置的保证金比例，float浮点型数据，默认返回交易所设定的保证金比例

#### 示例

```python
def initialize(context):
    g.security = "IF2312.CCFX"
    set_universe(g.security)
    # 设置沪深300指数的保证金比例为8%
    set_margin_rate("IF", 0.08)

def before_trading_start(context, data):
    # 获取沪深300指数的保证金比例
    margin_rate = get_margin_rate("IF")
    log.info('IF保证金比例: %.2f%%' % (margin_rate * 100))

def handle_data(context, data):
    pass
```

## 期货策略示例

### 简单趋势跟踪策略

```python
def initialize(context):
    g.contract = 'IF2312.CCFX'
    set_universe(g.contract)
    # 设置保证金比例
    set_margin_rate("IF", 0.15)

def handle_data(context, data):
    # 获取历史数据
    hist = get_history(20, '1d', 'close', g.contract)
    
    # 计算移动平均线
    ma5 = hist['close'][-5:].mean()
    ma20 = hist['close'][-20:].mean()
    
    # 获取当前持仓
    position = get_position(g.contract)
    
    # 多头信号：短期均线上穿长期均线
    if ma5 > ma20 and position.long_amount == 0:
        if position.short_amount > 0:
            # 先平空仓
            buy_close(g.contract, position.short_amount)
            log.info('平空仓')
        # 开多仓
        buy_open(g.contract, 1)
        log.info('开多仓')
    
    # 空头信号：短期均线下穿长期均线
    elif ma5 < ma20 and position.short_amount == 0:
        if position.long_amount > 0:
            # 先平多仓
            sell_close(g.contract, position.long_amount)
            log.info('平多仓')
        # 开空仓
        sell_open(g.contract, 1)
        log.info('开空仓')
```

## 注意事项

1. **保证金要求**: 期货交易需要缴纳保证金，注意资金管理
2. **价格跳动**: 不同品种的最小价格变动单位不同
3. **交易时间**: 期货有特定的交易时间，注意夜盘时间
4. **强制平仓**: 保证金不足时会被强制平仓
5. **交割日期**: 注意合约的交割日期，及时换月
6. **手续费**: 期货交易有开仓和平仓手续费

## 相关文档

- [股票交易API](stock-trading.md) - 股票交易功能
- [对象说明](objects.md) - Order、Position等对象详解
- [策略示例](../getting-started/examples.md) - 更多策略示例
