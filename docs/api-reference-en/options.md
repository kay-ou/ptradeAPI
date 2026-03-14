# Options Trading API

> 📖 **Navigation**: [API Documentation Home](README.md) | [Stock Trading](stock-trading.md) | [Futures Trading](futures.md) | [Market Data](market-data.md)

This document details various API functions for options trading on the Ptrade platform, including contract queries, trading orders, covered positions, and exercise functions.

---

## Query Functions

### `get_opt_objects()` - Get Options Underlying List

-   **Interface Description**: Get all ETF options underlying list for a specified trading day.
-   **Parameters**:
    -   `date` (str, optional): Query date, format `YYYY-MM-DD` or `YYYYMMDD`. Defaults to current date.
-   **Return**: `list[str]`, list containing underlying security codes.

### `get_opt_last_dates()` - Get Contract Expiration Dates

-   **Interface Description**: Get all listed contract expiration dates for a specified options underlying on a specific trading day.
-   **Parameters**:
    -   `security` (str): Options underlying security code, such as `'510050.SS'`.
    -   `date` (str, optional): Query date. Defaults to current date.
-   **Return**: `list[str]`, list containing all expiration dates, format `YYYY-MM-DD`.

### `get_opt_contracts()` - Get Contract List

-   **Interface Description**: Get all listed contract codes for a specified options underlying on a specific trading day.
-   **Parameters**:
    -   `security` (str): Options underlying security code.
    -   `date` (str, optional): Query date. Defaults to current date.
-   **Return**: `list[str]`, list containing all contract codes.

### `get_contract_info()` - Get Contract Information

-   **Interface Description**: Get detailed information of a single options contract.
-   **Parameters**:
    -   `contract` (str): Options contract code, such as `'10003975.XSHO'`.
-   **Return**: `dict`, containing detailed contract information, such as `contract_name`, `option_type` (C/P), `exercise_price`, `expiration_date`, etc.

---

## Trading Functions

### `buy_open()` - Long Open (Buy to Open)

-   **Interface Description**: Buy options, establish long position.
-   **Parameters**:
    -   `contract` (str): Options contract code.
    -   `amount` (int): Trading quantity (contracts).
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `sell_close()` - Long Close (Sell to Close)

-   **Interface Description**: Sell held options, close long position.
-   **Parameters**:
    -   `contract` (str): Options contract code.
    -   `amount` (int): Trading quantity (contracts).
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `sell_open()` - Short Open (Sell to Open)

-   **Interface Description**: Sell options, establish short position.
-   **Parameters**:
    -   `contract` (str): Options contract code.
    -   `amount` (int): Trading quantity (contracts).
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `buy_close()` - Short Close (Buy to Close)

-   **Interface Description**: Buy options, close short position.
-   **Parameters**:
    -   `contract` (str): Options contract code.
    -   `amount` (int): Trading quantity (contracts).
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

---

> 🔙 **Return**: [API Documentation Home](README.md)