# 基础信息API

本文档详细介绍了用于获取平台基础信息（如交易日、市场列表、可转债信息等）的API函数。

---

## 交易日信息

### `get_trading_day()` - 获取单个交易日

```python
get_trading_day(day=0)
```

-   **接口说明**: 获取相对于当前日期（回测或交易中为 `context.blotter.current_dt`）指定偏移量的单个交易日。
-   **参数**:
    -   `day` (int): 天数偏移量。正数表示未来，负数表示过去，0表示当前交易日（若当天非交易日，则返回下一个交易日）。默认为 0。
-   **返回**: `datetime.date` 对象。

### `get_all_trades_days()` - 获取所有历史交易日

```python
get_all_trades_days(date=None)
```

-   **接口说明**: 获取指定日期之前的所有交易日列表。
-   **参数**:
    -   `date` (str): 查询截止日期，格式为 `YYYY-MM-DD` 或 `YYYYMMDD`。默认为当前日期。
-   **返回**: 包含所有交易日的 `numpy.ndarray`。

### `get_trade_days()` - 获取区间交易日

```python
get_trade_days(start_date=None, end_date=None, count=None)
```

-   **接口说明**: 获取指定时间范围内的所有交易日列表。
-   **注意事项**: `start_date` 和 `count` 参数互斥，二者择一。
-   **参数**:
    -   `start_date` (str): 开始日期。
    -   `end_date` (str): 结束日期。默认为当前日期。
    -   `count` (int): 从 `end_date` 往前推算的交易日数量。
-   **返回**: 包含指定范围内交易日的 `numpy.ndarray`。

---

## 市场与品种信息

### `get_market_list()` - 获取市场列表

```python
get_market_list()
```

-   **接口说明**: 返回当前支持的所有市场列表。
-   **注意事项**: 在回测和交易中，建议在 `before_trading_start` 或 `after_trading_end` 中调用。
-   **返回**: 一个 `pandas.DataFrame`，包含 `finance_mic` (市场编码) 和 `finance_name` (市场名称) 两列。

### `get_market_detail()` - 获取市场详细信息

```python
get_market_detail(finance_mic)
```

-   **接口说明**: 返回指定市场的详细信息，包括该市场下的所有产品代码和名称。
-   **注意事项**: 在回测和交易中，建议在 `before_trading_start` 或 `after_trading_end` 中调用。
-   **参数**:
    -   `finance_mic` (str): 市场代码，可通过 `get_market_list()` 获取。
-   **返回**: 一个 `pandas.DataFrame`，包含 `prod_code`, `prod_name` 等字段。

### `get_cb_list()` - 获取可转债列表

```python
get_cb_list()
```

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 返回当前市场上所有可转债的代码列表（包含已停牌）。
-   **注意事项**: 为减少服务器压力，同一分钟内多次调用将返回缓存数据。
-   **返回**: 包含所有可转债代码的 `list`。

### `get_cb_info()` - 获取可转债基础信息

```python
get_cb_info()
```

-   **使用场景**: 研究、交易模块。
-   **接口说明**: 获取所有可转债的详细基础信息。
-   **注意事项**: 需确认账户有可转债基础数据权限，否则返回空。
-   **返回**: 一个 `pandas.DataFrame`，包含 `bond_code`, `stock_code`, `premium_rate`, `convert_price` 等字段。

### `get_reits_list()` - 获取公募REITs列表

```python
get_reits_list(date=None)
```

-   **接口说明**: 获取指定日期的所有公募REITs基金代码列表。
-   **参数**:
    -   `date` (str): 查询日期，格式为 `YYYYMMDD`。默认为当前日期。
-   **返回**: 包含所有公募REITs基金代码的 `list`。
