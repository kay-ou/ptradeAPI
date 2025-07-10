# 期货交易API

本文档详细介绍了 Ptrade 平台中用于期货交易的API函数，包括开平仓、设置和查询等功能。

---

## 交易函数

### `buy_open()` - 多头开仓

-   **接口说明**: 买入开仓。
-   **参数**:
    -   `contract` (str): 期货合约代码。
    -   `amount` (int): 交易数量（手数，正数）。
    -   `limit_price` (float, optional): 限价。若不指定，则按市价委托。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `sell_close()` - 多头平仓

-   **接口说明**: 卖出平仓。
-   **参数**:
    -   `contract` (str): 期货合约代码。
    -   `amount` (int): 交易数量（手数，正数）。
    -   `limit_price` (float, optional): 限价。
    -   `close_today` (bool): 是否平今仓。`True` 为仅平今仓，`False` (默认) 为优先平昨仓。此参数仅对上海期货交易所生效。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `sell_open()` - 空头开仓

-   **接口说明**: 卖出开仓。
-   **参数**:
    -   `contract` (str): 期货合约代码。
    -   `amount` (int): 交易数量（手数，正数）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `buy_close()` - 空头平仓

-   **接口说明**: 买入平仓。
-   **参数**:
    -   `contract` (str): 期货合约代码。
    -   `amount` (int): 交易数量（手数，正数）。
    -   `limit_price` (float, optional): 限价。
    -   `close_today` (bool): 是否平今仓，规则同 `sell_close()`。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

---

## 设置函数

### `set_future_commission()` - 设置手续费

-   **使用场景**: 仅回测模块可用。
-   **接口说明**: 按交易代码设置期货的手续费。
-   **参数**:
    -   `transaction_code` (str): 期货合约的交易代码（如 "IF", "CU"）。
    -   `commission` (float): 手续费。可按固定金额（如 `2.0` 代表2元/手）或按比例（如 `0.00004` 代表万分之0.4）设置。
-   **返回**: `None`。

### `set_margin_rate()` - 设置保证金比例

-   **使用场景**: 回测、交易模块可用。
-   **接口说明**: 按交易代码设置期货的保证金比例。
-   **参数**:
    -   `transaction_code` (str): 期货合约的交易代码。
    -   `margin_rate` (float): 保证金比例（如 `0.08` 代表8%）。
-   **返回**: `None`。

---

## 查询函数

### `get_margin_rate()` - 获取保证金比例

-   **使用场景**: 仅回测模块可用。
-   **接口说明**: 获取用户为某一交易代码设置的保证金比例。若未设置，则返回交易所默认比例。
-   **参数**:
    -   `transaction_code` (str): 期货合约的交易代码。
-   **返回**: 保证金比例 (float)。

### `get_instruments()` - 获取合约信息

-   **接口说明**: 获取指定期货合约的详细信息。
-   **参数**:
    -   `contract` (str): 期货合约代码。
-   **返回**: `FutureParams` 对象，包含 `contract_code`, `contract_name`, `exchange`, `trade_unit`, `contract_multiplier`, `delivery_date`, `listing_date`, `trade_code`, `margin_rate` 等字段。

---

## 注意事项

1.  **价格精度**: 不同期货品种的最小价格变动单位（tick size）不同，进行限价委托时需特别注意。
2.  **保证金**: 期货交易采用保证金制度，请确保账户资金充足，并密切关注保证金水平以防范强平风险。
3.  **合约到期**: 期货合约有交割日期，需在到期前及时移仓或平仓。
4.  **手续费**: 期货交易的双边手续费（开仓和平仓）是重要的交易成本，应在策略中予以考虑。
