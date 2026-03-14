# Margin Trading API

This document details API functions for margin trading (two-financing) business on the Ptrade platform, including collateral trading, margin trading orders, and various status queries.

---

## Trading Functions

### `margin_trade()` - Collateral Trading

-   **Interface Description**: Perform ordinary buy/sell operations on collateral in credit account.
-   **Parameters**:
    -   `security` (str): Stock code.
    -   `amount` (int): Trading quantity, positive for buy, negative for sell.
    -   `limit_price` (float, optional): Limit price.
    -   `market_type` (int, optional): Market order type.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `margincash_open()` - Margin Buy

-   **Interface Description**: Margin buy specified underlying security.
-   **Parameters**:
    -   `security` (str): Stock code.
    -   `amount` (int): Trading quantity (positive).
    -   `limit_price` (float, optional): Limit price.
    -   `market_type` (int, optional): Market order type.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `margincash_close()` - Sell to Repay

-   **Interface Description**: Sell held securities, proceeds are prioritized for repaying margin debt.
-   **Parameters**:
    -   `security` (str): Stock code.
    -   `amount` (int): Trading quantity (positive).
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `margincash_direct_refund()` - Direct Repayment

-   **Interface Description**: Use own funds to directly repay margin debt.
-   **Parameters**:
    -   `value` (float): Repayment amount.
-   **Return**: `None`.

### `marginsec_open()` - Short Sell

-   **Interface Description**: Short sell specified underlying security.
-   **Parameters**:
    -   `security` (str): Stock code.
    -   `amount` (int): Trading quantity (positive).
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `marginsec_close()` - Buy to Cover

-   **Interface Description**: Buy securities to repay short selling debt.
-   **Parameters**:
    -   `security` (str): Stock code.
    -   `amount` (int): Trading quantity (positive).
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `marginsec_direct_refund()` - Direct Securities Return

-   **Interface Description**: Use own held securities to directly repay short selling debt.
-   **Parameters**:
    -   `security` (str): Stock code.
    -   `amount` (int): Securities return quantity (positive).
-   **Return**: `None`.

---

## Query Functions

### `get_margin_assert()` - Credit Asset Query

-   **Interface Description**: Query credit account's assets, liabilities, margin, and other overall situations.
-   **Return**: `dict`, containing fields such as `assure_asset` (collateral asset), `total_debit` (total liabilities), `enable_bail_balance` (available margin), etc.

### `get_margin_contract()` - Contract Query

-   **Interface Description**: Query details of margin trading contracts.
-   **Return**: `dict`, containing contract details.

---

> 🔙 **Return**: [API Documentation Home](README.md)