# Market Data API

> 📖 **Navigation**: [API Documentation Home](README.md) | [Stock Trading](stock-trading.md) | [Technical Indicators](technical-indicators.md) | [Stock Information](stock-info.md)

This documentation details API functions for obtaining various market data, including historical K-lines, real-time snapshots, and Level-2 tick-by-tick and time-sharing data.

---

## Historical Data

### `get_history()`

```python
get_history(count, frequency='1d', field='close', security_list=None, fq=None, include=False, fill='nan', is_dict=False)
```

-   **Interface Description**: Get historical K-line data for the most recent `count` periods. Supports multi-security and multi-field retrieval.
-   **Notes**:
    -   Only data from 2005 onwards can be obtained.
    -   Handling of suspension days: The returned data will include suspension days, with prices filled using data before suspension and volume as 0.
    -   This interface and `get_price()` do not support simultaneous calls in multiple threads.
-   **Parameters**:
    -   `count` (int): Number of K-lines, required.
    -   `frequency` (str): K-line period, supports '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', 'mo', '1q', '1y'. Default is `'1d'`.
    -   `field` (str or list): Market fields, such as 'open', 'high', 'low', 'close', 'volume', 'money', etc. Default is `['open','high','low','close','volume','money','price']`.
    -   `security_list` (str or list): Security codes. Default is the stock pool set by `set_universe()`.
    -   `fq` (str): Adjustment option, 'pre'-forward adjustment, 'post'-backward adjustment, 'dypre'-dynamic forward adjustment, `None`-no adjustment.
    -   `include` (bool): Whether to include the current unfinished period. Default is `False`.
    -   `fill` (str): Filling method for missing minute data, 'pre'-fill with previous minute data, 'nan'-fill with NaN. Default is `'nan'`.
    -   `is_dict` (bool): Whether to return dictionary format, which can improve retrieval speed. Default is `False`.
-   **Return**: `pandas.DataFrame`, `pandas.Panel` or `dict`, specific format depends on input parameters.

### `get_price()`

```python
get_price(security, start_date=None, end_date=None, frequency='1d', fields=None, fq=None, count=None, is_dict=False)
```

-   **Interface Description**: Get historical K-line data for a specified time range or specified number of bars.
-   **Notes**:
    -   `start_date` and `count` parameters are mutually exclusive, only one must be used.
    -   Returned data does not include the `end_date`当天.
-   **Parameters**:
    -   `security` (str or list): Security code.
    -   `start_date` (str): Start date.
    -   `end_date` (str): End date.
    -   `count` (int): Number of K-lines calculated backwards from `end_date`.
    -   Other parameters are the same as `get_history()`.
-   **Return**: Similar to `get_history()`, returns `pandas.DataFrame`, `pandas.Panel` or `dict`.

---

## Real-time Market Data

### `get_snapshot()`

```python
get_snapshot(security)
```

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Get real-time market snapshot for specified securities.
-   **Return**: A dictionary where key is security code and value is a dictionary containing all snapshot information for that security, such as `last_px`, `open_px`, `high_px`, `low_px`, `bid_grp`, `offer_grp`, etc.

---

## L2 Market Data (Requires Level-2 Permission)

### `get_individual_entrust()` - Tick-by-Tick Entrustment

```python
get_individual_entrust(stocks=None, data_count=50, start_pos=0, search_direction=1, is_dict=False)
```

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Get tick-by-tick entrustment market data for the current day.
-   **Parameters**:
    -   `stocks` (list): List of security codes.
    -   `data_count` (int): Number of data items to get, maximum 200.
-   **Return**: `dict` or `pandas.Panel`.

### `get_individual_transaction()` - Tick-by-Tick Transaction

```python
get_individual_transaction(stocks=None, data_count=50, start_pos=0, search_direction=1, is_dict=False)
```

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Get tick-by-tick transaction market data for the current day.
-   **Parameters**:
    -   `stocks` (list): List of security codes.
    -   `data_count` (int): Number of data items to get, maximum 200.
-   **Return**: `dict` or `pandas.Panel`.

### `get_tick_direction()` - Time-sharing Transaction

```python
get_tick_direction(symbols=None, query_date=0, start_pos=0, search_direction=1, data_count=50)
```

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Get time-sharing transaction market data for the current day.
-   **Return**: `OrderedDict` containing time-sharing transaction market data for each code.

---

## Other Market Data

### `get_gear_price()` - Price Level Data

```python
get_gear_price(sids)
```

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Get bid/ask price level data for specified codes.
-   **Return**: Dictionary containing `bid_grp` (bid price levels) and `offer_grp` (ask price levels) information.

### `get_sort_msg()` - Sector/Industry Ranking

```python
get_sort_msg(sort_type_grp=None, sort_field_name=None, sort_type=1, data_count=100)
```

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Get ranking of sectors or industries by price change rate.
-   **Parameters**:
    -   `sort_type_grp` (str): Sector or industry code (e.g., 'XBHS.DY', 'XBHS.GN').
    -   `sort_field_name` (str): Sorting field, such as 'px_change_rate' (price change rate).
    -   `sort_type` (int): Sorting method, 0-ascending, 1-descending.
-   **Return**: List where each element is a dictionary containing ranking information.

---

## 📚 Related Documentation

- [**Stock Trading API**](stock-trading.md) - Use market data for trading decisions
- [**Technical Indicators API**](technical-indicators.md) - Calculate technical indicators based on market data
- [**Stock Information API**](stock-info.md) - Get basic stock information and financial data
- [**Financial Data API**](financial-data.md) - Get detailed financial statement data
- [**Basic Information API**](basic-info.md) - Trading calendar, stock list and other basic data

> 🔙 **Return**: [API Documentation Home](README.md) | [Complete API Classification](../api-classification.md)