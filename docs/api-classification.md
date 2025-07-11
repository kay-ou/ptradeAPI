# API 接口分类汇总

> 📖 **导航**: [文档库主页](README.md) | [API参考](api-reference/) | [策略示例](examples.md) | [入门指南](getting-started/)

本文档将 Ptrade 的所有 API 接口按功能进行分类，方便您快速查找和使用。

---

## 1. 策略框架与设置函数

这类函数用于定义策略的基本行为和参数。

| 函数名 | 说明 |
| :--- | :--- |
| **核心回调函数** | |
| `initialize(context)` | **[必需]** 策略初始化函数，在启动时运行一次。 |
| `handle_data(context, data)` | **[必需]** 策略主逻辑函数，按日或分钟周期执行。 |
| `before_trading_start(context, data)` | **[可选]** 盘前处理函数，在每日开盘前执行。 |
| `after_trading_end(context, data)` | **[可选]** 盘后处理函数，在每日收盘后执行。 |
| `tick_data(context, data)` | **[可选]** Tick级别数据处理函数，仅交易环境可用。 |
| `on_order_response(context, order_list)` | **[可选]** 委托回报主推函数，仅交易环境可用。 |
| `on_trade_response(context, trade_list)` | **[可选]** 成交回报主推函数，仅交易环境可用。 |
| **定时周期性函数** | |
| `run_daily(context, func, time)` | 注册一个每日在指定时间运行的函数。 |
| `run_interval(context, func, seconds)` | 注册一个按指定秒数间隔运行的函数。 |
| **环境设置** | |
| `set_universe(security_list)` | 设置策略的证券池。 |
| `set_benchmark(security)` | 设置策略的业绩比较基准。 |
| `set_commission(commission_ratio, ...)` | **[回测]** 设置佣金费率。 |
| `set_slippage(slippage)` | **[回测]** 按比例设置滑点。 |
| `set_fixed_slippage(fixedslippage)` | **[回测]** 按固定值设置滑点。 |
| `set_volume_ratio(volume_ratio)` | **[回测]** 设置成交量比例。 |
| `set_limit_mode(limit_mode)` | **[回测]** 设置成交量限制模式。 |
| `set_yesterday_position(poslist)` | **[回测]** 设置回测初始底仓。 |
| `set_parameters(**kwargs)` | **[交易]** 设置策略运行时的特定行为参数。 |

---

## 2. 数据获取函数

这类函数用于获取市场、行情、基础信息和财务等各类数据。

| 函数名 | 说明 |
| :--- | :--- |
| **行情数据** | |
| `get_history(...)` | 获取历史K线数据。 |
| `get_price(...)` | 获取指定时间范围的历史数据。 |
| `get_snapshot(security)` | **[交易]** 获取实时行情快照。 |
| `get_individual_entrust(...)` | **[交易]** 获取L2逐笔委托数据。 |
| `get_individual_transaction(...)` | **[交易]** 获取L2逐笔成交数据。 |
| `get_tick_direction(...)` | **[交易]** 获取L2分时成交数据。 |
| `get_gear_price(sids)` | **[交易]** 获取档位行情价格。 |
| **基础信息** | |
| `get_trading_day(day)` | 获取单个交易日。 |
| `get_all_trades_days(date)` | 获取所有历史交易日。 |
| `get_trade_days(...)` | 获取区间交易日。 |
| `get_market_list()` | 获取市场列表。 |
| `get_market_detail(finance_mic)` | 获取市场详细信息。 |
| **证券信息** | |
| `get_stock_name(stocks)` | 获取证券名称。 |
| `get_stock_info(stocks, ...)` | 获取证券基础信息（如上市日期）。 |
| `get_stock_status(...)` | 获取股票状态（ST、停牌、退市）。 |
| `get_stock_exrights(...)` | 获取股票除权除息信息。 |
| `get_stock_blocks(stock_code)` | 获取股票所属板块。 |
| `get_index_stocks(index_code, ...)` | 获取指数成分股。 |
| `get_industry_stocks(industry_code)` | 获取行业成分股。 |
| `get_Ashares(date)` | 获取指定日期的所有A股列表。 |
| `get_etf_list()` | **[交易]** 获取ETF代码列表。 |
| `get_etf_stock_list(etf_code)` | **[交易]** 获取ETF成分券列表。 |
| `get_ipo_stocks()` | **[交易]** 获取当日可申购新股/新债列表。 |
| **财务数据** | |
| `get_fundamentals(...)` | 获取财务数据（估值、三大报表等）。 |

---

## 3. 交易与查询函数

这类函数用于执行交易委托、查询订单、持仓和账户信息。

| 函数名 | 说明 |
| :--- | :--- |
| **普通交易** | |
| `order(security, amount, ...)` | 按数量下单。 |
| `order_target(security, amount, ...)` | 下单到目标数量。 |
| `order_value(security, value, ...)` | 按价值下单。 |
| `order_target_value(security, value, ...)` | 下单到目标价值。 |
| `order_market(security, amount, ...)` | **[交易]** 市价单委托。 |
| `cancel_order(order_param)` | 撤销订单。 |
| `cancel_order_ex(order_param)` | **[交易]** 撤销账户内的任意订单。 |
| **高级交易** | |
| `ipo_stocks_order(...)` | **[交易]** 一键申购新股/新债。 |
| `after_trading_order(...)` | **[交易]** 盘后固定价委托。 |
| `after_trading_cancel_order(...)` | **[交易]** 撤销盘后固定价委托。 |
| `etf_basket_order(...)` | **[交易]** ETF一篮子下单。 |
| `etf_purchase_redemption(...)` | **[交易]** ETF申购/赎回。 |
| `debt_to_stock_order(...)` | **[交易]** 可转债转股。 |
| **查询** | |
| `get_position(security)` | 获取单个标的的持仓信息。 |
| `get_positions()` | 获取所有持仓信息。 |
| `get_order(order_id)` | 获取本策略的单个订单。 |
| `get_orders(security=None)` | 获取本策略的所有订单。 |
| `get_open_orders(security=None)` | 获取本策略所有未完成的订单。 |
| `get_all_orders(security=None)` | **[交易]** 获取账户当日所有订单。 |
| `get_trades()` | 获取本策略当日所有成交记录。 |
| `get_deliver(start_date, end_date)` | **[交易]** 获取历史交割单。 |
| `get_fundjour(start_date, end_date)` | **[交易]** 获取历史资金流水。 |

---

## 4. 融资融券、期货、期权函数

请参考各自的专题文档：
-   **[融资融券API](api-reference/margin-trading.md)**
-   **[期货交易API](api-reference/futures.md)**
-   **[期权交易API](api-reference/options.md)**

---

## 5. 其他工具函数

| 函数名 | 说明 |
| :--- | :--- |
| `log(content)` | 打印日志信息。 |
| `is_trade()` | 判断当前是回测还是交易环境。 |
| `check_limit(security, ...)` | 检查证券的涨跌停状态。 |
| `send_email(...)` | **[交易]** 发送邮件。 |
| `send_qywx(...)` | **[交易]** 发送企业微信消息。 |
| `permission_test(...)` | **[交易]** 策略授权校验。 |
| `create_dir(user_path)` | 创建文件目录。 |
| `get_research_path()` | 获取研究环境根目录路径。 |
| `get_user_name()` | 获取当前资金账号。 |
| `get_trade_name()` | **[交易]** 获取当前交易实例名称。 |

---

## 📚 相关文档

- [**API详细参考**](api-reference/) - 查看每个接口的详细说明和参数
- [**策略示例**](examples.md) - 查看API接口的实际使用示例
- [**入门指南**](getting-started/) - 学习如何使用这些API接口
- [**版本差异**](version-differences.md) - 了解不同版本中API的差异

> 🔙 **返回**: [文档库主页](README.md) | [API参考文档](api-reference/)
