# Futures Trading API

> 📖 **Navigation**: [API Documentation Home](README.md) | [Stock Trading](stock-trading.md) | [Options Trading](options.md) | [Market Data](market-data.md)

This document details API functions for futures trading on the Ptrade platform, including opening/closing positions, settings, and queries.

---

## Trading Functions

### `buy_open()` - Long Open

-   **Interface Description**: Buy to open position.
-   **Parameters**:
    -   `contract` (str): Futures contract code.
    -   `amount` (int): Trading quantity (lots, positive number).
    -   `limit_price` (float, optional): Limit price. If not specified, market order is used.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `sell_close()` - Long Close

-   **Interface Description**: Sell to close position.
-   **Parameters**:
    -   `contract` (str): Futures contract code.
    -   `amount` (int): Trading quantity (lots, positive number).
    -   `limit_price` (float, optional): Limit price.
    -   `close_today` (bool): Whether to close today's position. `True` for closing only today's position, `False` (default) for prioritizing yesterday's position. This parameter only applies to Shanghai Futures Exchange.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `sell_open()` - Short Open

-   **Interface Description**: Sell to open position.
-   **Parameters**:
    -   `contract` (str): Futures contract code.
    -   `amount` (int): Trading quantity (lots, positive number).
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `buy_close()` - Short Close

-   **Interface Description**: Buy to close position.
-   **Parameters**:
    -   `contract` (str): Futures contract code.
    -   `amount` (int): Trading quantity (lots, positive number).
    -   `limit_price` (float, optional): Limit price.
    -   `close_today` (bool): Whether to close today's position, same rules as `sell_close()`.
-   **Return**: `id` (str) of the `Order` object or `None`.

---

## Setting Functions

### `set_future_commission()` - Set Commission

-   **Usage Scenario**: Only available in backtest module.
-   **Interface Description**: Set futures commission by trading code.
-   **Parameters**:
    -   `transaction_code` (str): Trading code of futures contract (e.g., "IF", "CU").
    -   `commission` (float): Commission. Can be set as fixed amount (e.g., `2.0` represents 2 yuan/lot) or by ratio (e.g., `0.00004` represents 0.004%).
-   **Return**: `None`.

### `set_margin_rate()` - Set Margin Rate

-   **Usage Scenario**: Available in backtest and trading modules.
-   **Interface Description**: Set futures margin rate by trading code.
-   **Parameters**:
    -   `transaction_code` (str): Trading code of futures contract.
    -   `margin_rate` (float): Margin rate (e.g., `0.08` represents 8%).
-   **Return**: `None`.

---

## Query Functions

### `get_margin_rate()` - Get Margin Rate

-   **Usage Scenario**: Only available in backtest module.
-   **Interface Description**: Get the margin rate set by user for a trading code. If not set, returns exchange default rate.
-   **Parameters**:
    -   `transaction_code` (str): Trading code of futures contract.
-   **Return**: Margin rate (float).

---

> 🔙 **Return**: [API Documentation Home](README.md)