# 技术指标API

本文档介绍技术指标计算相关的API函数，包括MACD、KDJ、RSI、CCI等常用技术指标。

## get_MACD - 异同移动平均线

```python
get_MACD(close, short=12, long=26, m=9)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

获取异同移动平均线MACD指标的计算结果

### 参数

close：价格的时间序列数据, numpy.ndarray类型；

short: 短周期, int类型；

long: 长周期, int类型；

m: 移动平均线的周期, int类型；

### 返回

MACD指标dif值的时间序列, numpy.ndarray类型

MACD指标dea值的时间序列, numpy.ndarray类型

MACD指标macd值的时间序列, numpy.ndarray类型

### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def handle_data(context, data):
    h = get_history(100, '1d', ['close','high','low'], security_list=g.security)
    close_data = h['close'].values
    macdDIF_data, macdDEA_data, macd_data = get_MACD(close_data, 12, 26, 9)
    dif = macdDIF_data[-1]
    dea = macdDEA_data[-1]
    macd = macd_data[-1]
    
    # 使用MACD指标进行交易决策
    if dif > dea and macdDIF_data[-2] <= macdDEA_data[-2]:
        # 金叉买入
        order_value(g.security, context.portfolio.cash)
        log.info('MACD金叉，买入')
    elif dif < dea and macdDIF_data[-2] >= macdDEA_data[-2]:
        # 死叉卖出
        order_target(g.security, 0)
        log.info('MACD死叉，卖出')
```

## get_KDJ - 随机指标

```python
get_KDJ(high, low, close, n=9, m1=3, m2=3)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

获取随机指标KDJ指标的计算结果

### 参数

high：最高价的时间序列数据, numpy.ndarray类型；

low：最低价的时间序列数据, numpy.ndarray类型；

close：收盘价的时间序列数据, numpy.ndarray类型；

n: 周期, int类型；

m1: 参数m1, int类型；

m2: 参数m2, int类型；

### 返回

KDJ指标k值的时间序列, numpy.ndarray类型

KDJ指标d值的时间序列, numpy.ndarray类型

KDJ指标j值的时间序列, numpy.ndarray类型

### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def handle_data(context, data):
    h = get_history(100, '1d', ['close','high','low'], security_list=g.security)
    high_data = h['high'].values
    low_data = h['low'].values
    close_data = h['close'].values
    k_data, d_data, j_data = get_KDJ(high_data, low_data, close_data, 9, 3, 3)
    k = k_data[-1]
    d = d_data[-1]
    j = j_data[-1]
    
    # 使用KDJ指标进行交易决策
    if k > d and k_data[-2] <= d_data[-2] and k < 20:
        # K线上穿D线且在超卖区域，买入
        order_value(g.security, context.portfolio.cash)
        log.info('KDJ金叉且超卖，买入')
    elif k < d and k_data[-2] >= d_data[-2] and k > 80:
        # K线下穿D线且在超买区域，卖出
        order_target(g.security, 0)
        log.info('KDJ死叉且超买，卖出')
```

## get_RSI - 相对强弱指标

```python
get_RSI(close, n=6)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

获取相对强弱指标RSI指标的计算结果

### 参数

close：价格的时间序列数据, numpy.ndarray类型；

n: 周期, int类型；

### 返回

RSI指标rsi值的时间序列, numpy.ndarray类型

### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def handle_data(context, data):
    h = get_history(100, '1d', ['close','high','low'], security_list=g.security)
    close_data = h['close'].values
    rsi_data = get_RSI(close_data, 6)
    rsi = rsi_data[-1]
    
    # 使用RSI指标进行交易决策
    if rsi < 30:
        # RSI小于30，超卖，买入
        order_value(g.security, context.portfolio.cash)
        log.info('RSI超卖，买入')
    elif rsi > 70:
        # RSI大于70，超买，卖出
        order_target(g.security, 0)
        log.info('RSI超买，卖出')
```

## get_CCI - 顺势指标

```python
get_CCI(high, low, close, n=14)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

获取顺势指标CCI指标的计算结果

### 参数

high：最高价的时间序列数据, numpy.ndarray类型；

low：最低价的时间序列数据, numpy.ndarray类型；

close：收盘价的时间序列数据, numpy.ndarray类型；

n: 周期, int类型；

### 返回

CCI指标cci值的时间序列, numpy.ndarray类型

### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def handle_data(context, data):
    h = get_history(100, '1d', ['close','high','low'], security_list=g.security)
    high_data = h['high'].values
    low_data = h['low'].values
    close_data = h['close'].values
    cci_data = get_CCI(high_data, low_data, close_data, 14)
    cci = cci_data[-1]
    
    # 使用CCI指标进行交易决策
    if cci < -100:
        # CCI小于-100，超卖，买入
        order_value(g.security, context.portfolio.cash)
        log.info('CCI超卖，买入')
    elif cci > 100:
        # CCI大于100，超买，卖出
        order_target(g.security, 0)
        log.info('CCI超买，卖出')
```

## 技术指标使用技巧

### 组合使用

技术指标往往需要组合使用才能提高准确性：

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def handle_data(context, data):
    h = get_history(100, '1d', ['close','high','low'], security_list=g.security)
    close_data = h['close'].values
    high_data = h['high'].values
    low_data = h['low'].values
    
    # 计算多个技术指标
    macdDIF, macdDEA, macd = get_MACD(close_data, 12, 26, 9)
    k, d, j = get_KDJ(high_data, low_data, close_data, 9, 3, 3)
    rsi = get_RSI(close_data, 14)
    
    # 组合判断买入信号
    buy_signal = (
        macdDIF[-1] > macdDEA[-1] and  # MACD金叉
        k[-1] > d[-1] and              # KDJ金叉
        rsi[-1] < 70                   # RSI未超买
    )
    
    # 组合判断卖出信号
    sell_signal = (
        macdDIF[-1] < macdDEA[-1] or   # MACD死叉
        rsi[-1] > 80                   # RSI超买
    )
    
    if buy_signal and get_position(g.security).amount == 0:
        order_value(g.security, context.portfolio.cash)
        log.info('多指标确认买入信号')
    elif sell_signal and get_position(g.security).amount > 0:
        order_target(g.security, 0)
        log.info('多指标确认卖出信号')
```

### 参数优化

不同的市场环境可能需要调整技术指标的参数：

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)
    # 可以通过回测优化这些参数
    g.macd_short = 12
    g.macd_long = 26
    g.macd_m = 9
    g.rsi_period = 14

def handle_data(context, data):
    h = get_history(100, '1d', 'close', security_list=g.security)
    close_data = h['close'].values
    
    # 使用自定义参数
    macdDIF, macdDEA, macd = get_MACD(close_data, g.macd_short, g.macd_long, g.macd_m)
    rsi = get_RSI(close_data, g.rsi_period)
    
    # 交易逻辑...
```

## 注意事项

1. **数据长度**：确保输入的价格数据长度足够计算指标，建议至少100个数据点
2. **指标滞后性**：技术指标都有一定的滞后性，不要过度依赖单一指标
3. **市场环境**：不同的市场环境下，同一指标的有效性可能不同
4. **参数调优**：通过回测优化指标参数，找到最适合的设置
5. **风险控制**：技术指标只是辅助工具，还需要结合风险管理

## 相关文档

- [行情数据API](market-data.md) - 获取计算指标所需的价格数据
- [股票交易API](stock-trading.md) - 基于指标信号进行交易
- [策略示例](../getting-started/examples.md) - 查看使用技术指标的完整策略
