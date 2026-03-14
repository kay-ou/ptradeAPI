# Technical Indicators API

> 📖 **Navigation**: [API Documentation Home](README.md) | [Market Data](market-data.md) | [Stock Trading](stock-trading.md) | [Strategy Examples](../examples.md)

This document introduces API functions related to technical indicator calculations, including commonly used technical indicators such as MACD, KDJ, RSI, CCI, etc.

## get_MACD - Moving Average Convergence Divergence

```python
get_MACD(close, short=12, long=26, m=9)
```

### Usage Scenario

This function is only available in backtest and trading modules.

### Interface Description

Get the calculation results of MACD (Moving Average Convergence Divergence) indicator.

### Parameters

- `close`: Time series data of prices, numpy.ndarray type.
- `short`: Short period, int type.
- `long`: Long period, int type.
- `m`: Moving average period, int type.

### Return

- MACD indicator DIF value time series, numpy.ndarray type.
- MACD indicator DEA value time series, numpy.ndarray type.
- MACD indicator MACD value time series, numpy.ndarray type.

### Example

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
    
    # Use MACD indicator for trading decisions
    if dif > dea and macdDIF_data[-2] <= macdDEA_data[-2]:
        # Golden cross buy
        order_value(g.security, context.portfolio.cash)
        log.info('MACD golden cross, buy')
    elif dif < dea and macdDIF_data[-2] >= macdDEA_data[-2]:
        # Death cross sell
        order_target(g.security, 0)
        log.info('MACD death cross, sell')
```

## get_KDJ - Stochastic Oscillator

```python
get_KDJ(high, low, close, n=9, m1=3, m2=3)
```

### Usage Scenario

This function is only available in backtest and trading modules.

### Interface Description

Get the calculation results of KDJ (Stochastic Oscillator) indicator.

### Parameters

- `high`: Time series data of high prices, numpy.ndarray type.
- `low`: Time series data of low prices, numpy.ndarray type.
- `close`: Time series data of close prices, numpy.ndarray type.
- `n`: Calculation period, int type, default is 9.
- `m1`: K value smoothing period, int type, default is 3.
- `m2`: D value smoothing period, int type, default is 3.

### Return

- K value time series, numpy.ndarray type.
- D value time series, numpy.ndarray type.
- J value time series, numpy.ndarray type.

---

> 🔙 **Return**: [API Documentation Home](README.md)