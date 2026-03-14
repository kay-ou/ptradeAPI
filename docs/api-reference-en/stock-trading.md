# Stock Trading API

> 📖 **Navigation**: [API Documentation Home](README.md) | [Market Data](market-data.md) | [Technical Indicators](technical-indicators.md) | [Data Objects](objects.md)

This documentation details various API functions for stock and other securities trading on the Ptrade platform, including basic order placement, advanced trading, order and position queries, etc.

---

## Basic Order Functions

These functions are the most basic ways to execute buy/sell operations.

### `order()` - Order by Quantity

-   **Interface Description**: Buy or sell securities by specified quantity. Supports stocks, convertible bonds, ETFs, LOFs, and bond reverse repos.
-   **Parameters**:
    -   `security` (str): Security code.
    -   `amount` (int): Trading quantity. Positive for buy, negative for sell.
    -   `limit_price` (float, optional): Limit price. If not specified, market order is used.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `order_target()` - Order by Target Quantity

-   **Interface Description**: Adjust the position of the specified security to the target quantity.
-   **Notes**: Due to position synchronization delays during trading, frequent calls may cause duplicate orders. Use with caution.
-   **Parameters**:
    -   `security` (str): Security code.
    -   `amount` (int): Desired target position quantity.
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `order_value()` - Order by Value

-   **Interface Description**: Buy or sell securities of specified value.
-   **Parameters**:
    -   `security` (str): Security code.
    -   `value` (float): Trading value. Positive for buy, negative for sell.
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `order_target_value()` - Order by Target Value

-   **Interface Description**: Adjust the position of the specified security to the target value.
-   **Notes**: Similar to `order_target`, use with caution to avoid duplicate orders during trading.
-   **Parameters**:
    -   `security` (str): Security code.
    -   `value` (float): Desired target position value.
    -   `limit_price` (float, optional): Limit price.
-   **Return**: `id` (str) of the `Order` object or `None`.

---

## Advanced Trading Functions

### `order_market()` - Market Order

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Use multiple market order types supported by the exchange for delegation.
-   **Parameters**:
    -   `security` (str): Security code.
    -   `amount` (int): Trading quantity.
    -   `market_type` (int): Market order type (e.g., `0`: best price of counterparty, `1`: best five levels immediate execution remaining to limit price, etc.).
    -   `limit_price` (float, optional): Protective limit price, required for Shanghai Stock Exchange stocks.
-   **Return**: `None`.

### `order_tick()` - Tick Data Triggered Order

-   **Usage Scenario**: Only available within the `tick_data` function.
-   **Interface Description**: Place orders based on real-time Tick data, can specify bid/ask price levels.
-   **Parameters**:
    -   `sid` (str): Security code.
    -   `amount` (int): Trading quantity.
    -   `priceGear` (str): Price level, such as `'1'` (buy one), `'-1'` (sell one).
    -   `limit_price` (float, optional): Specified price, takes priority over `priceGear`.
-   **Return**: Order serial number (str).

### `ipo_stocks_order()` - New Stock/New Bond Subscription

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: One-click subscription for all available new stocks and new bonds on the current day.
-   **Parameters**:
    -   `market_type` (int, optional): Subscription by market, such as `0` (Shanghai A-shares), `1` (Science and Technology Innovation Board), `4` (convertible bonds).
    -   `black_stocks` (str or list, optional): Blacklist of stocks not to participate in subscription.
-   **Return**: `dict` containing detailed information of each subscription order.

### `after_trading_order()` - Post-Market Fixed Price Order

-   **Usage Scenario**: Only available in trading module.
-   **Interface Description**: Submit fixed price orders during post-market trading hours (15:05-15:30).
-   **Parameters**:
    -   `security` (str): Security code.
    -   `amount` (int): Trading quantity.
    -   `entrust_price` (float): Entrusted price, must be the closing price of the day.
-   **Return**: `id` (str) of the `Order` object or `None`.

### `etf_basket_order()` / `etf_purchase_redemption()` - ETF Trading

-   **Usage Scenario**: Only available in trading module.
-   **`etf_basket_order`**: ETF component basket order.
-   **`etf_purchase_redemption`**: ETF fund purchase/redemption.

---

## Order and Position Management

### Position Query

-   **`get_position(security)`**: Get [Position object](objects.md#position) for a single security.
-   **`get_positions()`**: Get dictionary of [Position objects](objects.md#position) for all positions.

### Order Query

-   **`get_orders(security=None)`**: Get all orders generated by **this strategy** on the current day.
-   **`get_open_orders(security=None)`**: Get all uncompleted orders of **this strategy** on the current day.
-   **`get_order(order_id)`**: Get a single order specified by **this strategy**.
-   **`get_all_orders(security=None)`**: Get all entrustment records of **this account** on the current day (including manual orders and orders from other strategies).
-   **`get_trades()`**: Get all transaction records of **this strategy** on the current day.

### Order Cancellation

-   **`cancel_order(order_param)`**: Cancel orders of this strategy based on `Order` object or `order_id`.
-   **`cancel_order_ex(order_param)`**: Cancel any order in the account based on order information dictionary obtained from `get_all_orders()`.
-   **`after_trading_cancel_order(order_param)`**: Cancel post-market fixed price orders.

---

## 📚 Related Documentation

- [**Market Data API**](market-data.md) - Get stock prices, K-line and other market data
- [**Technical Indicators API**](technical-indicators.md) - Calculate technical indicators like MACD, KDJ, RSI
- [**Data Object Definitions**](objects.md) - Detailed descriptions of Order, Position, Security and other objects
- [**Futures Trading API**](futures.md) - Futures contract trading interfaces
- [**Options Trading API**](options.md) - Options contract trading interfaces
- [**Margin Trading API**](margin-trading.md) - Margin trading related interfaces

> 🔙 **Return**: [API Documentation Home](README.md) | [Complete API Classification](../api-classification.md)