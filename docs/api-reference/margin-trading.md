# 融资融券API

本文档详细介绍了 Ptrade 平台中用于融资融券（两融）业务的API函数，包括担保品交易、融资融券下单以及各类状态查询。

---

## 交易类函数

### `margin_trade()` - 担保品买卖

-   **接口说明**: 对信用账户中的担保品进行普通买卖操作。
-   **参数**:
    -   `security` (str): 股票代码。
    -   `amount` (int): 交易数量，正数买入，负数卖出。
    -   `limit_price` (float, optional): 限价。
    -   `market_type` (int, optional): 市价委托类型。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `margincash_open()` - 融资买入

-   **接口说明**: 融资买入指定的标的证券。
-   **参数**:
    -   `security` (str): 股票代码。
    -   `amount` (int): 交易数量（正数）。
    -   `limit_price` (float, optional): 限价。
    -   `market_type` (int, optional): 市价委托类型。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `margincash_close()` - 卖券还款

-   **接口说明**: 卖出持仓证券，所得资金优先用于归还融资负债。
-   **参数**:
    -   `security` (str): 股票代码。
    -   `amount` (int): 交易数量（正数）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `margincash_direct_refund()` - 直接还款

-   **接口说明**: 使用自有资金直接归还融资负债。
-   **参数**:
    -   `value` (float): 还款金额。
-   **返回**: `None`。

### `marginsec_open()` - 融券卖出

-   **接口说明**: 融券卖出指定的标的证券。
-   **参数**:
    -   `security` (str): 股票代码。
    -   `amount` (int): 交易数量（正数）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `marginsec_close()` - 买券还券

-   **接口说明**: 买入证券以归还融券负债。
-   **参数**:
    -   `security` (str): 股票代码。
    -   `amount` (int): 交易数量（正数）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `marginsec_direct_refund()` - 直接还券

-   **接口说明**: 使用自有持仓的证券直接归还融券负债。
-   **参数**:
    -   `security` (str): 股票代码。
    -   `amount` (int): 还券数量（正数）。
-   **返回**: `None`。

---

## 查询类函数

### `get_margin_assert()` - 信用资产查询

-   **接口说明**: 查询信用账户的资产、负债、保证金等总体情况。
-   **返回**: `dict`，包含 `assure_asset` (担保资产), `total_debit` (负债总额), `enable_bail_balance` (可用保证金) 等字段。

### `get_margin_contract()` - 合约查询

-   **接口说明**: 查询当前所有的融资融券合约详情。
-   **返回**: `pandas.DataFrame`，包含每笔合约的详细信息，如 `compact_id` (合约编号), `stock_code`, `compact_type` (合约类型), `repaid_balance` (已还金额) 等。

### `get_margincash_stocks()` / `get_marginsec_stocks()` - 标的列表查询

-   **`get_margincash_stocks()`**: 获取最新的可融资标的列表。
-   **`get_marginsec_stocks()`**: 获取最新的可融券标的列表。
-   **返回**: `list[str]`，包含所有标的的代码。

### `get_assure_security_list()` - 担保品列表查询

-   **接口说明**: 获取最新的可作为保证金的担保品证券列表。
-   **返回**: `list[str]`，包含所有担保品的代码。

### 可用数量查询

-   **`get_margincash_open_amount(security, price)`**: 查询指定价格下，某证券的最大可融资买入数量。
-   **`get_margincash_close_amount(security, price)`**: 查询指定价格下，某证券的最大可卖券还款数量。
-   **`get_marginsec_open_amount(security, price)`**: 查询指定价格下，某证券的最大可融券卖出数量。
-   **`get_marginsec_close_amount(security, price)`**: 查询指定价格下，某证券的最大可买券还券数量。
-   **`get_margin_entrans_amount(security)`**: 查询某证券可用于直接还券的数量。
-   **`get_enslo_security_info()`**: 查询融券头寸的详细信息，如可用数量、保证金比例等。

---

## 注意事项

1.  **权限要求**: 所有融资融券相关操作都需要在开通了融资融券权限的账户下进行。
2.  **保证金**: 交易时需确保账户有足够的保证金，避免因保证金不足导致废单或强制平仓。
3.  **费用与利息**: 融资融券交易会产生额外的利息和费用，请在策略中充分考虑。
4.  **标的范围**: 并非所有证券都支持融资融券，请通过 `get_margincash_stocks()` 和 `get_marginsec_stocks()` 查询最新的标的列表。
