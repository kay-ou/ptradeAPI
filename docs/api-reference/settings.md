# 设置函数

本文档详细介绍了用于配置策略回测与交易环境的各类设置函数。

---

## `set_universe()` - 设置股票池

```python
set_universe(security_list)
```

-   **使用场景**: 回测、交易模块。
-   **接口说明**: 用于设置或更新策略要操作的证券（股票、基金、可转债等）列表。在股票策略中，此函数主要用于设定 `get_history()` 等数据获取函数的默认证券列表。
-   **参数**:
    -   `security_list` (str or list[str]): 证券代码或列表。
-   **返回**: `None`

---

## `set_benchmark()` - 设置基准

```python
set_benchmark(security)
```

-   **使用场景**: 回测、交易模块。
-   **接口说明**: 设置策略的业绩比较基准。设置后，回测报告中的各项风险指标（如 Alpha、Beta、夏普比率等）都将基于此基准进行计算。
-   **注意事项**:
    -   此函数只能在 `initialize()` 函数中使用。
    -   若不设置，系统默认使用沪深300指数 (`000300.SS`) 作为基准。
-   **参数**:
    -   `security` (str): 股票、指数或ETF的代码。
-   **返回**: `None`

---

## `set_commission()` - 设置佣金

```python
set_commission(commission_ratio=0.0003, min_commission=5.0, type="STOCK")
```

-   **使用场景**: 回测模块。
-   **接口说明**: 设置回测时模拟的交易佣金。
-   **注意事项**:
    -   回测总手续费 = 佣金 + 经手费。
    -   佣金 = `commission_ratio` * 交易金额 (最低 `min_commission`)。
    -   经手费按交易所标准计算（如：万分之0.487）。
-   **参数**:
    -   `commission_ratio` (float): 佣金费率，默认为万分之三。
    -   `min_commission` (float): 每笔最低佣金，默认为5元。
    -   `type` (str): 交易类型，支持 "STOCK", "ETF", "LOF"。
-   **返回**: `None`

---

## `set_slippage()` / `set_fixed_slippage()` - 设置滑点

滑点是为模拟真实交易中因市场延迟、流动性等因素造成的成交价与委托价之间的差异。

### `set_slippage()` - 按比例滑点

```python
set_slippage(slippage=0.001)
```

-   **接口说明**: 设置一个百分比作为滑点。
-   **计算公式**: `成交价 = 委托价 ± 委托价 * slippage / 2`
-   **参数**:
    -   `slippage` (float): 滑点比例，默认为 0.001 (即0.1%)。

### `set_fixed_slippage()` - 按固定值滑点

```python
set_fixed_slippage(fixed_slippage=0.0)
```

-   **接口说明**: 设置一个固定的价格作为滑点。
-   **计算公式**: `成交价 = 委托价 ± fixed_slippage / 2`
-   **参数**:
    -   `fixed_slippage` (float): 固定的滑点价差，默认为0。

---

## `set_volume_ratio()` - 设置成交量比例

```python
set_volume_ratio(volume_ratio=0.25)
```

-   **使用场景**: 回测模块。
-   **接口说明**: 设置回测中单笔委托的最大成交量占市场总成交量的比例，用于模拟流动性对大额订单的冲击。
-   **注意事项**: 如果委托数量超过按此比例计算的成交量，多余部分将不会挂单。
-   **参数**:
    -   `volume_ratio` (float): 成交比例，默认为0.25。
-   **返回**: `None`

---

## `set_limit_mode()` - 设置成交量限制模式

```python
set_limit_mode(limit_mode='LIMIT')
```

-   **使用场景**: 回测模块。
-   **接口说明**: 控制回测时是否受市场成交量的限制。
-   **参数**:
    -   `limit_mode` (str):
        -   `'LIMIT'`: (默认) 受成交量限制，成交量不超过市场真实成交量。
        -   `'UNLIMITED'`: 不受限制，适用于对流动性不敏感的低频策略。
-   **返回**: `None`

---

## `set_yesterday_position()` - 设置回测底仓

```python
set_yesterday_position(poslist)
```

-   **使用场景**: 回测模块。
-   **接口说明**: 在回测开始前设置初始持仓。
-   **参数**:
    -   `poslist` (list[dict]): 持仓列表，每个字典代表一只股票的持仓信息。
    -   **字典格式**: `{'sid': '代码', 'amount': 持仓数量, 'enable_amount': 可用数量, 'cost_basis': 成本价}`
    -   也可以通过 `convert_position_from_csv()` 从 CSV 文件加载。
-   **返回**: `None`

---

## `set_parameters()` - 设置策略配置参数

```python
set_parameters(**kwargs)
```

-   **使用场景**: 交易模块。
-   **接口说明**: 用于设置策略运行时的特定行为参数。
-   **支持的参数**:
    -   `holiday_not_do_before` (str): "1" 或 "0"，节假日是否执行 `before_trading_start`。
    -   `tick_data_no_l2` (str): "1" 或 "0"，`tick_data` 的 `data` 参数中是否包含 order 和 transaction 数据。
    -   `receive_other_response` (str): "1" 或 "0"，是否接收非本交易产生的主推回报。
    -   `receive_cancel_response` (str): "1" 或 "0"，是否接收撤单委托产生的主推回报。
-   **返回**: `None`
