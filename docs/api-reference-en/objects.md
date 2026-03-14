# Objects and Data Dictionary

This document details the core objects (such as `g`, `context`, `Portfolio`, `Position`, `Order`) involved in the Ptrade API during strategy execution and their attributes, and provides data dictionaries for key fields.

---

## `g` - Global Object

-   **Object Description**: The global object `g` is a special variable used to pass and store user-defined data between different functions in the strategy. All attributes set on `g` can be accessed anywhere in the strategy.
-   **Usage Scenarios**:
    -   Store global configurations that don't change over time, such as security lists, parameters, etc.
    -   Save state variables that need to be shared at different time points (such as `before_trading_start` and `handle_data`).
-   **Notes**:
    -   Variables starting with double underscore `__` are private variables and won't be saved by the platform's persistence mechanism.
    -   Complex class instances involving IO (such as opened files) or that cannot be serialized should not be stored in the `g` object, otherwise persistence will fail.
-   **Example**:
    ```python
    def initialize(context):
        # Store security list
        g.security_pool = ['600570.SS', '000001.SZ']
        # Store strategy parameters
        g.ma_short = 10
        g.ma_long = 20
        # Store a status flag
        g.traded_today = False
    ```

---

## `context` - Context Object

-   **Object Description**: The `context` object contains all context information during strategy execution, serving as the bridge connecting strategy logic with account and market data. It is passed as a parameter to almost all core functions.
-   **Core Attributes**:
    -   `context.portfolio`: [Portfolio Object](#Portfolio---Portfolio-Object), provides access to account assets, positions, and other information.
    -   `context.blotter.current_dt`: Current strategy time (`datetime.datetime` object), in backtest it is backtest time, in live trading it is real-time.
    -   `context.previous_date`: Previous trading day's date (`datetime.date` object).

---

## `Portfolio` - Portfolio Object

-   **Object Description**: The `portfolio` object represents your entire investment portfolio, containing all account-level information such as funds, positions, market value, profit/loss, etc.
-   **Core Attributes**:
    -   `portfolio.cash` (float): Current available funds.
    -   `portfolio.positions` (dict): A dictionary, key is security code, value is corresponding [Position Object](#Position---Position-Object).
    -   `portfolio.portfolio_value` (float): Total account assets (position market value + cash).
    -   `portfolio.positions_value` (float): Total position market value.
    -   `portfolio.pnl` (float): Current account's floating profit/loss.
    -   `portfolio.returns` (float): Current cumulative return rate.
-   **Options/Futures Specific Attributes**:
    -   `portfolio.margin` (float): (Options) Margin.
    -   `portfolio.risk_degree` (float): (Options) Risk degree.

---

## `Position` - Position Object

-   **Object Description**: The `Position` object represents all information about a single underlying you hold.
-   **Core Attributes (Stocks)**:
    -   `sid` (str): Underlying code.
    -   `amount` (int): Total position quantity.
    -   `enable_amount` (int): Available (sellable) quantity.
    -   `cost_basis` (float): Position cost price.
    -   `last_sale_price` (float): Latest market price.
-   **Core Attributes (Futures)**:
    -   `long_amount` / `short_amount`: Long/Short total position.
    -   `long_enable_amount` / `short_enable_amount`: Long/Short available position.
    -   `long_cost_basis` / `short_cost_basis`: Long/Short position cost.
    -   `long_pnl` / `short_pnl`: Long/Short floating profit/loss.
-   **Core Attributes (Options)**:
    -   `long_amount` / `short_amount` / `covered_amount`: Long/Short/Covered position quantity.
    -   `long_cost_basis` / `short_cost_basis` / `covered_cost_basis`: Corresponding position cost.
    -   `long_pnl` / `short_pnl` / `covered_pnl`: Corresponding floating profit/loss.

---

## `Order` - Order Object

-   **Object Description**: The `Order` object represents a specific order, containing all status and information of the order.
-   **Core Attributes**:
    -   `order_id` (str): Order ID.
    -   `security` (str): Security code.
    -   `amount` (int): Order quantity.
    -   `filled` (int): Filled quantity.
    -   `price` (float): Order price.
    -   `status` (str): Order status.

---

> 🔙 **Return**: [API Documentation Home](README.md)