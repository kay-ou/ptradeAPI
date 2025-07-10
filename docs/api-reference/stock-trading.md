# 股票交易API

本文档详细介绍了 Ptrade 平台中用于股票及其他证券交易的各类API函数，包括基础下单、高级交易、订单与持仓查询等。

---

## 基础下单函数

这些函数是执行买卖操作最基本的方式。

### `order()` - 按数量下单

-   **接口说明**: 按指定的数量买入或卖出证券。支持股票、可转债、ETF、LOF及国债逆回购。
-   **参数**:
    -   `security` (str): 证券代码。
    -   `amount` (int): 交易数量。正数表示买入，负数表示卖出。
    -   `limit_price` (float, optional): 限价。若不指定，则按市价委托。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `order_target()` - 按目标数量下单

-   **接口说明**: 调整指定证券的持仓到目标数量。
-   **注意事项**: 交易中因持仓同步延迟，频繁调用可能导致重复下单，建议谨慎使用。
-   **参数**:
    -   `security` (str): 证券代码。
    -   `amount` (int): 期望的目标持仓数量。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `order_value()` - 按价值下单

-   **接口说明**: 买入或卖出指定价值的证券。
-   **参数**:
    -   `security` (str): 证券代码。
    -   `value` (float): 交易价值。正数表示买入，负数表示卖出。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `order_target_value()` - 按目标价值下单

-   **接口说明**: 调整指定证券的持仓到目标价值。
-   **注意事项**: 与 `order_target` 类似，交易中需谨慎使用以避免重复下单。
-   **参数**:
    -   `security` (str): 证券代码。
    -   `value` (float): 期望的目标持仓价值。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

---

## 高级交易函数

### `order_market()` - 市价委托

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 使用交易所支持的多种市价单类型进行委托。
-   **参数**:
    -   `security` (str): 证券代码。
    -   `amount` (int): 交易数量。
    -   `market_type` (int): 市价委托类型（如 `0`: 对手方最优价，`1`: 最优五档即时成交剩余转限价等）。
    -   `limit_price` (float, optional): 保护限价，对上交所股票为必填项。
-   **返回**: `None`。

### `order_tick()` - Tick 行情触发下单

-   **使用场景**: 仅在 `tick_data` 函数内可用。
-   **接口说明**: 根据实时 Tick 行情进行下单，可指定买卖盘口档位。
-   **参数**:
    -   `sid` (str): 证券代码。
    -   `amount` (int): 交易数量。
    -   `priceGear` (str): 盘口档位，如 `'1'` (买一), `'-1'` (卖一)。
    -   `limit_price` (float, optional): 指定价格，优先级高于 `priceGear`。
-   **返回**: 委托流水号 (str)。

### `ipo_stocks_order()` - 新股/新债申购

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 一键申购当日所有可申购的新股和新债。
-   **参数**:
    -   `market_type` (int, optional): 按市场申购，如 `0` (上证A股), `1` (科创板), `4` (可转债)。
    -   `black_stocks` (str or list, optional): 不参与申购的黑名单。
-   **返回**: `dict`，包含各申购委托的详细信息。

### `after_trading_order()` - 盘后固定价委托

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 在盘后交易时段（15:05-15:30）提交固定价格委托。
-   **参数**:
    -   `security` (str): 证券代码。
    -   `amount` (int): 交易数量。
    -   `entrust_price` (float): 委托价格，必须为当日收盘价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `etf_basket_order()` / `etf_purchase_redemption()` - ETF 交易

-   **使用场景**: 仅交易模块可用。
-   **`etf_basket_order`**: ETF 成分券一篮子下单。
-   **`etf_purchase_redemption`**: ETF 基金申购/赎回。

---

## 订单与持仓管理

### 查询持仓

-   **`get_position(security)`**: 获取单个标的的 [Position对象](objects.md#Position)。
-   **`get_positions()`**: 获取所有持仓的 [Position对象](objects.md#Position) 字典。

### 查询订单

-   **`get_orders(security=None)`**: 获取**本策略**当日产生的所有订单。
-   **`get_open_orders(security=None)`**: 获取**本策略**当日所有未完成的订单。
-   **`get_order(order_id)`**: 获取**本策略**指定的单个订单。
-   **`get_all_orders(security=None)`**: 获取**该账户**当日所有委托记录（包括手动下单和其他策略的订单）。
-   **`get_trades()`**: 获取**本策略**当日所有成交记录。

### 撤销订单

-   **`cancel_order(order_param)`**: 根据 `Order` 对象或 `order_id` 撤销本策略的订单。
-   **`cancel_order_ex(order_param)`**: 根据从 `get_all_orders()` 获取的订单信息字典，撤销账户内的任意订单。
-   **`after_trading_cancel_order(order_param)`**: 撤销盘后固定价委托。
