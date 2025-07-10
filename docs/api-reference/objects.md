# 对象与数据字典

本文档详细介绍了 Ptrade API 在策略运行过程中涉及的核心对象（如 `g`, `context`, `Portfolio`, `Position`, `Order`）及其属性，并提供了关键字段的数据字典。

---

## `g` - 全局对象

-   **对象说明**: 全局对象 `g` 是一个特殊的变量，用于在策略的不同函数之间传递和存储用户自定义的数据。所有在 `g` 上设置的属性都可以在策略的任何地方被访问。
-   **使用场景**:
    -   存储不随时间变化的全局配置，如证券列表、参数等。
    -   保存需要在不同时间点（如 `before_trading_start` 和 `handle_data`）共享的状态变量。
-   **注意事项**:
    -   以双下划线 `__` 开头的变量为私有变量，不会被平台的持久化机制保存。
    -   涉及到IO（如打开的文件）或无法被序列化的复杂类实例不应存储在 `g` 对象中，否则持久化会失败。
-   **示例**:
    ```python
    def initialize(context):
        # 存储证券列表
        g.security_pool = ['600570.SS', '000001.SZ']
        # 存储策略参数
        g.ma_short = 10
        g.ma_long = 20
        # 存储一个状态标志
        g.traded_today = False
    ```

---

## `context` - 上下文对象

-   **对象说明**: `context` 对象包含了策略运行时的所有上下文信息，是连接策略逻辑与账户、市场数据的桥梁。它作为参数传递给几乎所有的核心函数。
-   **核心属性**:
    -   `context.portfolio`: [Portfolio对象](#Portfolio---投资组合对象)，提供对账户资产、持仓等信息的访问。
    -   `context.blotter.current_dt`: 当前的策略时间（`datetime.datetime` 对象），在回测中是回测时间，在实盘中是实时时间。
    -   `context.previous_date`: 前一个交易日的日期 (`datetime.date` 对象)。

---

## `Portfolio` - 投资组合对象

-   **对象说明**: `portfolio` 对象代表了您的整个投资组合，包含了资金、持仓、市值、盈亏等所有账户级别的信息。
-   **核心属性**:
    -   `portfolio.cash` (float): 当前可用资金。
    -   `portfolio.positions` (dict): 一个字典，key为证券代码，value为对应的 [Position对象](#Position---持仓对象)。
    -   `portfolio.portfolio_value` (float): 账户总资产（持仓市值 + 现金）。
    -   `portfolio.positions_value` (float): 总持仓市值。
    -   `portfolio.pnl` (float): 当前账户的浮动盈亏。
    -   `portfolio.returns` (float): 当前的累计收益率。
-   **期权/期货特定属性**:
    -   `portfolio.margin` (float): (期权) 保证金。
    -   `portfolio.risk_degree` (float): (期权) 风险度。

---

## `Position` - 持仓对象

-   **对象说明**: `Position` 对象代表了您持有的单个标的的所有信息。
-   **核心属性 (股票)**:
    -   `sid` (str): 标的代码。
    -   `amount` (int): 总持仓数量。
    -   `enable_amount` (int): 可用（可卖）数量。
    -   `cost_basis` (float): 持仓成本价。
    -   `last_sale_price` (float): 最新市场价。
-   **核心属性 (期货)**:
    -   `long_amount` / `short_amount`: 多头/空头总持仓。
    -   `long_enable_amount` / `short_enable_amount`: 多头/空头可用持仓。
    -   `long_cost_basis` / `short_cost_basis`: 多头/空头持仓成本。
    -   `long_pnl` / `short_pnl`: 多头/空头浮动盈亏。
-   **核心属性 (期权)**:
    -   `long_amount` / `short_amount` / `covered_amount`: 权利仓/义务仓/备兑仓数量。
    -   `long_cost_basis` / `short_cost_basis` / `covered_cost_basis`: 对应持仓成本。
    -   `long_pnl` / `short_pnl` / `covered_pnl`: 对应浮动盈亏。

---

## `Order` - 订单对象

-   **对象说明**: `Order` 对象代表了一笔具体的委托订单，包含了订单的所有状态和信息。
-   **核心属性**:
    -   `id` (str): 订单的唯一ID。
    -   `dt` (datetime): 订单创建时间。
    -   `symbol` (str): 标的代码。
    -   `amount` (int): 委托数量（买入为正，卖出为负）。
    -   `filled` (int): 已成交数量。
    -   `status` (str): 订单状态，详见下方的**数据字典**。
    -   `entrust_no` (str): 委托编号。

---

## 数据字典

### 订单状态 (`Order.status`)

| 状态码 | 含义 | 说明 |
|:---:|---|---|
| '0' | 未报 | 订单已创建，但尚未报送至交易所。 |
| '1' | 待报 | 订单正在报送至交易所。 |
| '2' | 已报 | 订单已被交易所接受。 |
| '3' | 已报待撤 | 已发送撤单请求，等待交易所确认。 |
| '4' | 部成待撤 | 部分成交，剩余部分等待撤单确认。 |
| '5' | 部撤 | 部分成交，剩余部分已成功撤单。 |
| '6' | 已撤 | 订单已成功撤销。 |
| '7' | 部成 | 订单部分成交。 |
| '8' | 已成 | 订单已完全成交。 |
| '9' | 废单 | 订单被交易所拒绝，无效。 |
| '+' | 已受理 | (特定柜台) 订单已被受理。 |
| '-' | 已确认 | (特定柜台) 订单已被确认。 |

### 委托方向 (`entrust_bs`)

| 状态码 | 含义 |
|:---:|---|
| '1' | 买入 |
| '2' | 卖出 |

### 委托属性 (`entrust_prop`)

| 状态码 | 含义 |
|:---:|---|
| '0' | 买卖 |
| '1' | 配股 |
| '3' | 申购 |
| '7' | 转股 |
| 'N' | ETF申赎 |
| 'Q' | 对手方最优价格 |
| 'S' | 本方最优价格 |
