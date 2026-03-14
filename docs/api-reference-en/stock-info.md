# Stock Information API

This document details API functions for obtaining basic information of various securities (stocks, ETFs, convertible bonds, etc.).

---

## Security Basic Information

### `get_stock_name()`

-   **Interface Description**: Get the name of specified security code.
-   **Parameters**:
    -   `stocks` (str or list[str]): Single or multiple security codes.
-   **Return**: `dict`, key is security code, value is name. Value is `None` when query fails.
-   **Example**:
    ```python
    stock_names = get_stock_name(['600570.SS', '000001.SZ'])
    log.info(stock_names)
    # Output: {'600570.SS': 'Hundsun Technologies', '000001.SZ': 'Ping An Bank'}
    ```

### `get_stock_info()`

-   **Interface Description**: Get basic information such as listing date and delisting date of securities.
-   **Parameters**:
    -   `stocks` (str or list[str]): Single or multiple security codes.
    -   `field` (str or list[str]): Fields to query, optional `'stock_name'`, `'listed_date'`, `'de_listed_date'`. Default is `'stock_name'`.
-   **Return**: `dict`, key is security code, value is dictionary containing queried fields.
-   **Example**:
    ```python
    info = get_stock_info('600570.SS', ['listed_date', 'de_listed_date'])
    log.info(info)
    # Output: {'600570.SS': {'listed_date': '2003-12-16', 'de_listed_date': '2900-01-01'}}
    ```

### `get_stock_status()`

-   **Interface Description**: Query the status (ST, halt, delisting) of specified securities on a specified date.
-   **Parameters**:
    -   `stocks` (str or list[str]): Security codes.
    -   `query_type` (str): Query type, optional `'ST'`, `'HALT'`, `'DELISTING'`. Default is `'ST'`.
    -   `query_date` (str): Query date, format `YYYYmmdd`. Defaults to current date.
-   **Return**: `dict`, key is security code, value is boolean (`True`/`False`).

### `get_stock_exrights()`

-   **Interface Description**: Get complete ex-rights and ex-dividend information of specified stock.
-   **Parameters**:
    -   `stock_code` (str): Stock code.
    -   `date` (str): Query ex-rights and ex-dividend information for specified date. Default is `None`, get all historical records.
-   **Return**: `pandas.DataFrame`, containing fields such as `allotted_ps` (bonus shares), `bonus_ps` (dividend), etc.

---

## Sectors and Constituents

### `get_stock_blocks()`

-   **Interface Description**: Get the industry, region, and concept sectors that a single stock belongs to.
-   **Notes**: This function gets the current latest sector information, using it in backtest may introduce future data.
-   **Parameters**:
    -   `stock_code` (str): Stock code.
-   **Return**: `dict`, key is sector type (e.g., 'HY', 'DY', 'GN'), value is list of sector codes and names.

### `get_index_stocks()`

-   **Interface Description**: Get the constituent stock list of a specified index on a certain day.
-   **Parameters**:
    -   `index_code` (str): Index code, such as `'000300.SS'`.
    -   `date` (str): Query date, format `YYYYMMDD`. Defaults to current date.
-   **Return**: Stock code list `list[str]`.

### `get_industry_stocks()`

-   **Interface Description**: Get all constituent stock list of a specified industry.
-   **Notes**: This function gets the current latest constituent information, using it in backtest may introduce future data.
-   **Parameters**:
    -   `industry_code` (str): Industry code, can be obtained through `get_stock_blocks()`.
-   **Return**: Stock code list `list[str]`.

---

> 🔙 **Return**: [API Documentation Home](README.md)