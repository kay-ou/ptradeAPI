# 行情数据API

本文档详细介绍了用于获取各类行情数据的API函数，包括历史K线、实时快照、以及L2级别的逐笔和分时数据。

---

## 历史行情

### `get_history()`

```python
get_history(count, frequency='1d', field='close', security_list=None, fq=None, include=False, fill='nan', is_dict=False)
```

-   **接口说明**: 获取最近 `count` 个周期的历史行情K线数据。支持多标的、多字段获取。
-   **注意事项**:
    -   只能获取2005年之后的数据。
    -   停牌日的处理：返回的数据会包含停牌日，价格使用停牌前的数据填充，成交量为0。
    -   该接口与 `get_price()` 不支持在多线程中同时调用。
-   **参数**:
    -   `count` (int): K线数量，必填。
    -   `frequency` (str): K线周期，支持 '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', 'mo', '1q', '1y'。默认为 `'1d'`。
    -   `field` (str or list): 行情字段，如 'open', 'high', 'low', 'close', 'volume', 'money' 等。默认为 `['open','high','low','close','volume','money','price']`。
    -   `security_list` (str or list): 证券代码。默认为 `set_universe()` 设置的股票池。
    -   `fq` (str): 复权选项，'pre'-前复权, 'post'-后复权, 'dypre'-动态前复权, `None`-不复权。
    -   `include` (bool): 是否包含当前未结束的周期。默认为 `False`。
    -   `fill` (str): 分钟数据缺失时的填充方式，'pre'-用上一分钟数据填充, 'nan'-填充NaN。默认为 `'nan'`。
    -   `is_dict` (bool): 是否返回字典格式，可以提升获取速度。默认为 `False`。
-   **返回**: `pandas.DataFrame`, `pandas.Panel` 或 `dict`，具体格式取决于输入参数。

### `get_price()`

```python
get_price(security, start_date=None, end_date=None, frequency='1d', fields=None, fq=None, count=None, is_dict=False)
```

-   **接口说明**: 获取指定时间范围或指定条数的历史行情K线数据。
-   **注意事项**:
    -   `start_date` 和 `count` 参数互斥，必须且只能使用一个。
    -   返回数据不包含 `end_date` 当天。
-   **参数**:
    -   `security` (str or list): 证券代码。
    -   `start_date` (str): 开始日期。
    -   `end_date` (str): 结束日期。
    -   `count` (int): 从 `end_date` 往前推算的K线数量。
    -   其他参数与 `get_history()` 相同。
-   **返回**: 与 `get_history()` 类似，返回 `pandas.DataFrame`, `pandas.Panel` 或 `dict`。

---

## 实时行情

### `get_snapshot()`

```python
get_snapshot(security)
```

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取指定证券的实时行情快照。
-   **返回**: 一个字典，key为证券代码，value为包含该证券所有快照信息的字典，如 `last_px`, `open_px`, `high_px`, `low_px`, `bid_grp`, `offer_grp` 等。

---

## L2 行情 (需开通Level-2权限)

### `get_individual_entrust()` - 逐笔委托

```python
get_individual_entrust(stocks=None, data_count=50, start_pos=0, search_direction=1, is_dict=False)
```

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取当日的逐笔委托行情数据。
-   **参数**:
    -   `stocks` (list): 证券代码列表。
    -   `data_count` (int): 获取的数据条数，最大200。
-   **返回**: `dict` 或 `pandas.Panel`。

### `get_individual_transaction()` - 逐笔成交

```python
get_individual_transaction(stocks=None, data_count=50, start_pos=0, search_direction=1, is_dict=False)
```

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取当日的逐笔成交行情数据。
-   **参数**:
    -   `stocks` (list): 证券代码列表。
    -   `data_count` (int): 获取的数据条数，最大200。
-   **返回**: `dict` 或 `pandas.Panel`。

### `get_tick_direction()` - 分时成交

```python
get_tick_direction(symbols=None, query_date=0, start_pos=0, search_direction=1, data_count=50)
```

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取当日的分时成交行情数据。
-   **返回**: `OrderedDict`，包含每只代码的分时成交行情。

---

## 其他行情

### `get_gear_price()` - 档位行情

```python
get_gear_price(sids)
```

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取指定代码的买卖盘档位行情价格。
-   **返回**: 字典，包含 `bid_grp` (委买档位) 和 `offer_grp` (委卖档位) 信息。

### `get_sort_msg()` - 板块/行业排名

```python
get_sort_msg(sort_type_grp=None, sort_field_name=None, sort_type=1, data_count=100)
```

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 获取板块或行业的涨跌幅排名。
-   **参数**:
    -   `sort_type_grp` (str): 板块或行业代码 (如 'XBHS.DY', 'XBHS.GN')。
    -   `sort_field_name` (str): 排序字段，如 'px_change_rate' (涨跌幅)。
    -   `sort_type` (int): 排序方式，0-升序, 1-降序。
-   **返回**: 列表，每个元素是一个包含排名信息的字典。
