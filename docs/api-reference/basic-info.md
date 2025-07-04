# 基础信息API

本文档介绍获取基础信息的API函数，包括交易日期、市场信息等。

## get_trading_day - 获取交易日期

```python
get_trading_day(day)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该函数用于获取当前时间数天前或数天后的交易日期。

注意事项：

1. 默认情况下，回测中当前时间为策略中调用该接口的回测日日期(context.blotter.current_dt)。
2. 默认情况下，研究中当前时间为调用当天日期。
3. 默认情况下，交易中当前时间为调用当天日期。

### 参数

day：表示天数，正的为数天后，负的为数天前，day取0表示获取当前交易日，如果当前日期为非交易日则返回上一交易日的日期。day默认取值为0，不建议获取交易所还未公布的交易日期(int)；

### 返回

date：datetime.date日期对象

### 示例

```python
def initialize(context):
    g.security = ['600670.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    # 获取后一天的交易日期
    previous_trading_date = get_trading_day(1)
    log.info(previous_trading_date)
    # 获取前一天的交易日期
    next_trading_date = get_trading_day(-1)
    log.info(next_trading_date)
```

## get_all_trades_days - 获取全部交易日期

```python
get_all_trades_days(date=None)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该函数用于获取某个日期之前的所有交易日日期。

注意事项：

1. 默认情况下，回测中date为策略中调用该接口的回测日日期(context.blotter.current_dt)。
2. 默认情况下，研究中date为调用当天日期。
3. 默认情况下，交易中date为调用当天日期。

### 参数

date：如'2016-02-13'或'20160213'

### 返回

一个包含所有交易日的numpy.ndarray

### 示例

```python
def initialize(context):
    # 获取当前回测日期之前的所有交易日
    all_trades_days = get_all_trades_days()
    log.info(all_trades_days)
    all_trades_days_date = get_all_trades_days('20150312')
    log.info(all_trades_days_date)
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    pass
```

## get_trade_days - 获取指定范围交易日期

```python
get_trade_days(start_date=None, end_date=None, count=None)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该函数用于获取指定范围交易日期。

注意事项：

1. 默认情况下，回测中end_date为策略中调用该接口的回测日日期(context.blotter.current_dt)。
2. 默认情况下，研究中end_date为调用当天日期。
3. 默认情况下，交易中end_date为调用当天日期。

### 参数

start_date：开始日期，与count二选一，不可同时使用。如'2016-02-13'或'20160213',开始日期最早不超过1990年(str)；

end_date：结束日期，如'2016-02-13'或'20160213'。如果输入的结束日期大于今年则至多返回截止到今年的数据(str)；

count：数量，与start_date二选一，不可同时使用，必须大于0。表示获取end_date往前的count个交易日，包含end_date当天。count建议不大于3000，即返回数据的开始日期不早于1990年(int)；

### 返回

一个包含指定范围交易日的numpy.ndarray

### 示例

```python
def initialize(context):
    # 获取指定范围内交易日
    trade_days = get_trade_days('2016-01-01', '2016-02-01')
    log.info(trade_days)
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    # 获取回测日期往前10天的所有交易日，包含历史回测日期
    trading_days = get_trade_days(count=10)
    log.info(trading_days)
```

## 市场信息

### get_market_list - 获取市场列表

```python
get_market_list()
```

#### 使用场景

该函数在研究、回测、交易模块可用

#### 接口说明

该函数用于获取市场列表。

#### 参数

无

#### 返回

DataFrame，包含市场信息

#### 示例

```python
def initialize(context):
    market_list = get_market_list()
    log.info(market_list)
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    pass
```

### get_market_detail - 获取市场详细信息

```python
get_market_detail(market_code)
```

#### 使用场景

该函数在研究、回测、交易模块可用

#### 接口说明

该函数用于获取指定市场的详细信息。

#### 参数

market_code：市场代码(str)

#### 返回

DataFrame，包含市场详细信息

#### 示例

```python
def initialize(context):
    market_detail = get_market_detail('XSHG')
    log.info(market_detail)
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    pass
```

### get_cb_list - 获取可转债市场代码表

```python
get_cb_list()
```

#### 使用场景

该函数在交易模块可用

#### 接口说明

该函数用于获取可转债市场代码表。

#### 参数

无

#### 返回

DataFrame，包含可转债代码信息

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def before_trading_start(context, data):
    cb_list = get_cb_list()
    log.info(cb_list)

def handle_data(context, data):
    pass
```

## 相关文档

- [行情数据API](market-data.md) - 获取历史和实时行情数据
- [股票信息API](stock-info.md) - 获取股票基础信息
- [工具函数](utilities.md) - 其他实用工具函数
