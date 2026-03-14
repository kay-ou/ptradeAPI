# Basic Information API

This document details API functions for obtaining platform basic information (such as trading days, market lists, convertible bond information, etc.).

---

## Trading Day Information

### `get_trading_day()` - Get Single Trading Day

```python
get_trading_day(day=0)
```

-   **Interface Description**: Get a single trading day relative to the current date (in backtest or trading, it is `context.blotter.current_dt`) with specified offset.
-   **Parameters**:
    -   `day` (int): Day offset. Positive for future, negative for past, 0 for current trading day (if current day is not a trading day, returns next trading day). Default is 0.
-   **Return**: `datetime.date` object.

### `get_all_trades_days()` - Get All Historical Trading Days

```python
get_all_trades_days(date=None)
```

-   **Interface Description**: Get all trading days list before specified date.
-   **Parameters**:
    -   `date` (str): Query end date, format `YYYY-MM-DD` or `YYYYMMDD`. Defaults to current date.
-   **Return**: `numpy.ndarray` containing all trading days.

### `get_trade_days()` - Get Range Trading Days

```python
get_trade_days(start_date=None, end_date=None, count=None)
```

-   **Interface Description**: Get all trading days list within specified time range.
-   **Notes**: `start_date` and `count` parameters are mutually exclusive, choose one.
-   **Parameters**:
    -   `start_date` (str): Start date.
    -   `end_date` (str): End date. Defaults to current date.
    -   `count` (int): Number of trading days calculated backward from `end_date`.
-   **Return**: `numpy.ndarray` containing trading days within specified range.

---

## Market and Product Information

### `get_market_list()` - Get Market List

```python
get_market_list()
```

-   **Interface Description**: Return all currently supported market lists.
-   **Notes**: In backtest and trading, it is recommended to call in `before_trading_start` or `after_trading_end`.
-   **Return**: A `pandas.DataFrame`, containing `finance_mic` (market code) and `finance_name` (market name) columns.

### `get_market_detail()` - Get Market Detail Information

```python
get_market_detail(finance_mic)
```

-   **Interface Description**: Return detailed information of specified market, including all product codes and names under that market.
-   **Notes**: In backtest and trading, it is recommended to call in `before_trading_start` or `after_trading_end`.
-   **Parameters**:
    -   `finance_mic` (str): Market code, can be obtained through `get_market_list()`.
-   **Return**: A `pandas.DataFrame`, containing fields such as `prod_code`, `prod_name`, etc.

### `get_cb_list()` - Get Convertible Bond List

```python
get_cb_list()
```

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Return all convertible bond code lists currently on the market (including halted ones).
-   **Notes**: To reduce server pressure, multiple calls within the same minute will return cached data.
-   **Return**: `list` containing all convertible bond codes.

---

> 🔙 **Return**: [API Documentation Home](README.md)