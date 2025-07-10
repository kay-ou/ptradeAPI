# 策略引擎框架

本文档详细介绍了 Ptrade 策略引擎的业务流程框架和核心回调函数，帮助您理解策略的生命周期和事件驱动机制。

## 业务流程框架

Ptrade 量化引擎以**事件驱动**为基础，通过一系列预定义的函数（事件处理器）来构建和执行策略。一个典型的交易日中，策略的生命周期主要由以下几个核心事件构成：

![业务流程框架](https://github.com/ptrade-dev/ptrade-docs/assets/13328734/9e8d1c7f-8d6e-4b9c-8b9a-0e8d1c7f8d6e)

1.  **`initialize(context)` (初始化)**: 策略启动时执行一次，用于全局设置。
2.  **`before_trading_start(context, data)` (盘前处理)**: 每个交易日开盘前执行一次。
3.  **`handle_data(context, data)` (主逻辑)**: 盘中按设定的频率（日或分钟）循环执行。
4.  **`after_trading_end(context, data)` (盘后处理)**: 每个交易日收盘后执行一次。

此外，平台还支持更灵活的事件处理器：
-   **`tick_data(context, data)`**: 用于处理 Tick 级别的逻辑。
-   **`run_daily()` / `run_interval()`**: 定时任务，可按日或自定义秒级间隔执行。
-   **`on_order_response()` / `on_trade_response()`**: 委托和成交回报的实时推送事件。

---

## 核心回调函数

### `initialize(context)`

-   **说明**: 初始化函数，在策略启动时（回测或交易开始时）调用一次，用于设置策略的全局配置和初始化变量。**此函数为必选函数。**
-   **可调用接口**:
    -   **设置函数**: `set_universe`, `set_benchmark`, `set_commission`, `set_slippage`, `set_fixed_slippage`, `set_volume_ratio`, `set_limit_mode`, `set_yesterday_position`, `set_parameters`, `set_future_commission`, `set_margin_rate`
    -   **定时函数**: `run_daily`, `run_interval`
    -   **其他**: `get_trading_day`, `get_all_trades_days`, `get_trade_days`, `convert_position_from_csv`, `get_user_name`, `is_trade`, `get_research_path`, `permission_test`, `get_margin_rate`, `create_dir`
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)，用于存储和传递策略上下文信息。
-   **返回**: `None`

### `before_trading_start(context, data)`

-   **说明**: 在每个交易日开盘前调用一次，用于进行每日的数据准备和初始化工作。
-   **调用时机**:
    -   **回测**: 每个回测交易日的 08:30。
    -   **交易**: 启动时立即执行一次，之后每个交易日 09:10 (默认) 执行。
-   **注意事项**: 在交易模式下，09:10 前调用实时行情接口可能获取到旧数据。
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)。
    -   `data`: 保留字段，暂无数据。
-   **返回**: `None`

### `handle_data(context, data)`

-   **说明**: 策略最核心的函数，根据您设置的频率（日或分钟）被反复调用，用于执行主要的交易逻辑。**此函数为必选函数。**
-   **调用时机**:
    -   **日线**: 每天 15:00 (回测) 或 14:50 (交易，可配置) 调用一次。
    -   **分钟**: 每个分钟 K 线结束后调用一次 (09:31-15:00)。
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)。
    -   `data`: 一个字典，key 为证券代码，value 为该周期的 [SecurityUnitData对象](objects.md#SecurityUnitData)。
-   **返回**: `None`

### `after_trading_end(context, data)`

-   **说明**: 在每个交易日收盘后调用一次，用于执行当日的收盘后任务。
-   **调用时机**: 每个交易日 15:30 (默认)。
-   **常用操作**:
    -   分析当日成交记录。
    -   保存当日策略状态，为次日做准备。
    -   生成当日交易报告。
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)。
    -   `data`: 保留字段，暂无数据。
-   **返回**: `None`

### `tick_data(context, data)`

-   **说明**: 用于处理 Tick 级别的策略逻辑，每 3 秒执行一次。
-   **使用场景**: 仅在交易模块可用。
-   **注意事项**:
    -   执行时间为 09:30 - 14:59。
    -   `data` 参数的结构与 `handle_data` 不同，包含更详细的盘口和逐笔数据。
    -   L2 行情数据需额外开通。
    -   如果策略逻辑执行时间超过 3 秒，中间的 Tick 数据会被丢弃。
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)。
    -   `data`: 包含 `order`, `tick`, `transaction` 的字典。
-   **返回**: `None`

### `on_order_response(context, order_list)`

-   **说明**: 当有委托回报时触发，比轮询 `get_orders()` 更快。
-   **使用场景**: 仅在交易模块可用。
-   **注意事项**: 在此函数内下单需小心处理，避免造成无限循环委托。
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)。
    -   `order_list`: 变化的委托单列表，每个元素是一个包含委托信息的字典。
-   **返回**: `None`

### `on_trade_response(context, trade_list)`

-   **说明**: 当有成交回报时触发，比轮询 `get_trades()` 更快。
-   **使用场景**: 仅在交易模块可用。
-   **注意事项**: 同 `on_order_response`，需注意避免循环下单。
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)。
    -   `trade_list`: 变化的成交单列表，每个元素是一个包含成交信息的字典。
-   **返回**: `None`

---

## 定时周期性函数

### `run_daily(context, func, time='9:31')`

-   **说明**: 注册一个在每个交易日指定时间执行一次的函数。
-   **注意事项**:
    -   只能在 `initialize()` 中调用。
    -   可以注册多个不同的定时任务。
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)。
    -   `func`: 要执行的函数，该函数必须接收 `context` 作为参数。
    -   `time` (str): "HH:MM" 格式的时间字符串。

### `run_interval(context, func, seconds=10)`

-   **说明**: 注册一个按指定秒数间隔循环执行的函数。
-   **使用场景**: 仅在交易模块可用。
-   **注意事项**:
    -   只能在 `initialize()` 中调用。
    -   最小间隔为 3 秒。
    -   多个 `run_interval` 会以多线程方式并行运行，需注意逻辑间的同步问题。
-   **参数**:
    -   `context`: [Context对象](objects.md#Context)。
    -   `func`: 要执行的函数，该函数必须接收 `context` 作为参数。
    -   `seconds` (int): 时间间隔（秒）。
