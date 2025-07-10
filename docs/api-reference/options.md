# 期权交易API

本文档详细介绍了 Ptrade 平台中用于期权交易的各类API函数，包括合约查询、交易下单、备兑和行权等功能。

---

## 查询函数

### `get_opt_objects()` - 获取期权标的列表

-   **接口说明**: 获取指定交易日的所有ETF期权标的列表。
-   **参数**:
    -   `date` (str, optional): 查询日期，格式 `YYYY-MM-DD` 或 `YYYYMMDD`。默认为当前日期。
-   **返回**: `list[str]`，包含期权标的证券代码的列表。

### `get_opt_last_dates()` - 获取合约到期日

-   **接口说明**: 获取指定期权标的在特定交易日的所有挂牌合约的到期日。
-   **参数**:
    -   `security` (str): 期权标的证券代码，如 `'510050.SS'`。
    -   `date` (str, optional): 查询日期。默认为当前日期。
-   **返回**: `list[str]`，包含所有到期日的列表，格式为 `YYYY-MM-DD`。

### `get_opt_contracts()` - 获取合约列表

-   **接口说明**: 获取指定期权标的在特定交易日的所有挂牌合约代码。
-   **参数**:
    -   `security` (str): 期权标的证券代码。
    -   `date` (str, optional): 查询日期。默认为当前日期。
-   **返回**: `list[str]`，包含所有合约代码的列表。

### `get_contract_info()` - 获取合约信息

-   **接口说明**: 获取单个期权合约的详细信息。
-   **参数**:
    -   `contract` (str): 期权合约代码，如 `'10003975.XSHO'`。
-   **返回**: `dict`，包含合约的详细信息，如 `contract_name`, `option_type` (C/P), `exercise_price`, `expiration_date` 等。

---

## 交易函数

### `buy_open()` - 权利仓开仓 (买入开仓)

-   **接口说明**: 买入期权，建立权利仓。
-   **参数**:
    -   `contract` (str): 期权合约代码。
    -   `amount` (int): 交易数量（张）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `sell_close()` - 权利仓平仓 (卖出平仓)

-   **接口说明**: 卖出持有的期权，了结权利仓。
-   **参数**:
    -   `contract` (str): 期权合约代码。
    -   `amount` (int): 交易数量（张）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `sell_open()` - 义务仓开仓 (卖出开仓)

-   **接口说明**: 卖出期权，建立义务仓。
-   **参数**:
    -   `contract` (str): 期权合约代码。
    -   `amount` (int): 交易数量（张）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `buy_close()` - 义务仓平仓 (买入平仓)

-   **接口说明**: 买入期权，了结义务仓。
-   **参数**:
    -   `contract` (str): 期权合约代码。
    -   `amount` (int): 交易数量（张）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

---

## 备兑与行权

### `open_prepared()` - 备兑开仓

-   **接口说明**: 在持有足额标的证券的前提下，卖出对应的认购期权。
-   **注意事项**: 仅支持上交所ETF认购期权。
-   **参数**:
    -   `contract` (str): 认购期权合约代码。
    -   `amount` (int): 交易数量（张）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `close_prepared()` - 备兑平仓

-   **接口说明**: 买入之前备兑开仓的认购期权，了结备兑仓位。
-   **参数**:
    -   `contract` (str): 认购期权合约代码。
    -   `amount` (int): 交易数量（张）。
    -   `limit_price` (float, optional): 限价。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

### `option_covered_lock()` / `option_covered_unlock()` - 备兑锁定/解锁

-   **`option_covered_lock(code, amount)`**: 锁定现货账户中指定数量的ETF，用于备兑开仓。
-   **`option_covered_unlock(code, amount)`**: 解锁已备兑锁定的ETF。
-   **注意事项**: 仅支持上交所ETF期权标的。

### `option_exercise()` - 行权

-   **接口说明**: 在期权到期日，对持有的价内期权执行行权操作。
-   **参数**:
    -   `contract` (str): 期权合约代码。
    -   `amount` (int): 行权数量（张）。
-   **返回**: `Order` 对象的 `id` (str) 或 `None`。

---

## 注意事项

1.  **权限要求**: 期权交易需要开通相应权限。
2.  **保证金**: 卖出期权（义务仓、备兑仓）需要缴纳保证金。
3.  **到期日**: 务必关注合约的到期日和最后交易日，及时处理持仓。
4.  **风险**: 期权交易具有高杠杆性，风险较大，请务必充分了解相关规则。
