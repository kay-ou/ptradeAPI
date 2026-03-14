# Strategy Engine Framework

This document details the business process framework and core callback functions of the Ptrade strategy engine, helping you understand the strategy lifecycle and event-driven mechanism.

## Business Process Framework

The Ptrade quantitative engine is based on **event-driven** architecture, building and executing strategies through a series of predefined functions (event handlers). In a typical trading day, the strategy lifecycle mainly consists of the following core events:

1.  **`initialize(context)` (Initialization)**: Executed once when the strategy starts, for global settings.
2.  **`before_trading_start(context, data)` (Pre-market Processing)**: Executed once before market open each trading day.
3.  **`handle_data(context, data)` (Main Logic)**: Executed in a loop during market hours at set frequency (daily or minute).
4.  **`after_trading_end(context, data)` (Post-market Processing)**: Executed once after market close each trading day.

Additionally, the platform supports more flexible event handlers:
-   **`tick_data(context, data)`**: For processing Tick-level logic.
-   **`run_daily()` / `run_interval()`**: Scheduled tasks, can be executed daily or at custom second-level intervals.
-   **`on_order_response()` / `on_trade_response()`**: Real-time push events for order and trade responses.

---

## Core Callback Functions

### `initialize(context)`

-   **Description**: Initialization function, called once when the strategy starts (at the beginning of backtest or trading), used for setting global configuration and initializing variables. **This function is required.**
-   **Callable Interfaces**:
    -   **Setting Functions**: `set_universe`, `set_benchmark`, `set_commission`, `set_slippage`, `set_fixed_slippage`, `set_volume_ratio`, `set_limit_mode`, `set_yesterday_position`, `set_parameters`, `set_future_commission`, `set_margin_rate`
    -   **Scheduled Functions**: `run_daily`, `run_interval`
    -   **Others**: `get_trading_day`, `get_all_trades_days`, `get_trade_days`, `convert_position_from_csv`, `get_user_name`, `is_trade`, `get_research_path`, `permission_test`, `get_margin_rate`, `create_dir`
-   **Parameters**:
    -   `context`: [Context Object](objects.md#Context), used to store and pass strategy context information.
-   **Return**: `None`

### `before_trading_start(context, data)`

-   **Description**: Called once before market open each trading day, used for daily data preparation and initialization.
-   **Call Timing**:
    -   **Backtest**: 08:30 of each backtest trading day.
    -   **Trading**: Executed immediately at startup, then at 09:10 (default) each trading day.
-   **Notes**: In trading mode, calling real-time market data interfaces before 09:10 may retrieve stale data.
-   **Parameters**:
    -   `context`: [Context Object](objects.md#Context).
    -   `data`: Reserved field, no data currently.
-   **Return**: `None`

### `handle_data(context, data)`

-   **Description**: The core function of the strategy, called repeatedly according to your set frequency (daily or minute), used to execute main trading logic. **This function is required.**
-   **Call Timing**:
    -   **Daily**: Called once at 15:00 (backtest) or 14:50 (trading, configurable).
    -   **Minute**: Called once after each minute K-line ends (09:31-15:00).
-   **Parameters**:
    -   `context`: [Context Object](objects.md#Context).
    -   `data`: A dictionary, key is security code, value is [SecurityUnitData Object](objects.md#SecurityUnitData) for that period.
-   **Return**: `None`

### `after_trading_end(context, data)`

-   **Description**: Called once after market close each trading day, used to execute post-market tasks for the day.
-   **Call Timing**: 15:30 each trading day (default).
-   **Common Operations**:
    -   Analyze day's trade records.
    -   Save day's strategy state for next day preparation.
    -   Generate day's trading report.
-   **Parameters**:
    -   `context`: [Context Object](objects.md#Context).
    -   `data`: Reserved field, no data currently.
-   **Return**: `None`

### `tick_data(context, data)`

-   **Description**: Used for processing Tick-level strategy logic, executed every 3 seconds.
-   **Usage Scenario**: Only available in trading module.
-   **Notes**:
    -   Execution time is 09:30 - 14:59.
    -   The structure of `data` parameter is different from `handle_data`, containing more detailed order book and tick-by-tick data.
    -   L2 market data requires additional subscription.
    -   If strategy logic execution time exceeds 3 seconds, intermediate Tick data will be dropped.

---

> 🔙 **Return**: [API Documentation Home](README.md)