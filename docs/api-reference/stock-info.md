# 股票信息API

本文档详细介绍了用于获取各类证券（股票、ETF、可转债等）基础信息的API函数。

---

## 证券基础信息

### `get_stock_name()`

-   **接口说明**: 获取指定证券代码的名称。
-   **参数**:
    -   `stocks` (str or list[str]): 单个或多个证券代码。
-   **返回**: `dict`，key为证券代码，value为名称。查询失败时value为`None`。
-   **示例**:
    ```python
    stock_names = get_stock_name(['600570.SS', '000001.SZ'])
    log.info(stock_names)
    # 输出: {'600570.SS': '恒生电子', '000001.SZ': '平安银行'}
    ```

### `get_stock_info()`

-   **接口说明**: 获取证券的上市日期、退市日期等基础信息。
-   **参数**:
    -   `stocks` (str or list[str]): 单个或多个证券代码。
    -   `field` (str or list[str]): 需要查询的字段，可选 `'stock_name'`, `'listed_date'`, `'de_listed_date'`。默认为 `'stock_name'`。
-   **返回**: `dict`，key为证券代码，value为包含所查询字段的字典。
-   **示例**:
    ```python
    info = get_stock_info('600570.SS', ['listed_date', 'de_listed_date'])
    log.info(info)
    # 输出: {'600570.SS': {'listed_date': '2003-12-16', 'de_listed_date': '2900-01-01'}}
    ```

### `get_stock_status()`

-   **接口说明**: 查询指定日期指定证券的状态（ST、停牌、退市）。
-   **参数**:
    -   `stocks` (str or list[str]): 证券代码。
    -   `query_type` (str): 查询类型，可选 `'ST'`, `'HALT'`, `'DELISTING'`。默认为 `'ST'`。
    -   `query_date` (str): 查询日期，格式 `YYYYmmdd`。默认为当前日期。
-   **返回**: `dict`，key为证券代码，value为布尔值 (`True`/`False`)。

### `get_stock_exrights()`

-   **接口说明**: 获取指定股票的完整除权除息信息。
-   **参数**:
    -   `stock_code` (str): 股票代码。
    -   `date` (str): 查询指定日期的除权除息信息。默认为 `None`，获取全部历史记录。
-   **返回**: `pandas.DataFrame`，包含 `allotted_ps` (送股), `bonus_ps` (分红) 等字段。

---

## 板块与成分股

### `get_stock_blocks()`

-   **接口说明**: 获取单个股票所属的行业、地域和概念板块。
-   **注意事项**: 该函数获取的是当前最新的板块信息，在回测中使用可能引入未来数据。
-   **参数**:
    -   `stock_code` (str): 股票代码。
-   **返回**: `dict`，key为板块类型（如 'HY', 'DY', 'GN'），value为板块代码和名称的列表。

### `get_index_stocks()`

-   **接口说明**: 获取指定指数在某一天的成分股列表。
-   **参数**:
    -   `index_code` (str): 指数代码，如 `'000300.SS'`。
    -   `date` (str): 查询日期，格式 `YYYYMMDD`。默认为当前日期。
-   **返回**: 股票代码列表 `list[str]`。

### `get_industry_stocks()`

-   **接口说明**: 获取指定行业的所有成分股列表。
-   **注意事项**: 该函数获取的是当前最新的成分股信息，在回测中使用可能引入未来数据。
-   **参数**:
    -   `industry_code` (str): 行业代码，可通过 `get_stock_blocks()` 获取。
-   **返回**: 股票代码列表 `list[str]`。

### `get_etf_stock_list()`

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取指定ETF的成分券列表。
-   **参数**:
    -   `etf_code` (str): ETF代码。
-   **返回**: 成分券代码列表 `list[str]`。

---

## A股与ETF列表

### `get_Ashares()`

-   **接口说明**: 获取指定日期的所有A股代码列表。
-   **参数**:
    -   `date` (str): 查询日期，格式 `YYYYMMDD`。默认为当前日期。
-   **返回**: A股代码列表 `list[str]`。

### `get_etf_list()`

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取柜台返回的完整ETF代码列表。
-   **返回**: ETF代码列表 `list[str]`。

### `get_ipo_stocks()`

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取当日可进行IPO申购的标的列表。
-   **返回**: `dict`，key为市场类型（如 '上证科创板代码', '可转债代码'），value为申购代码列表。
