# Ptrade API 接口分类汇总

基于三个版本API文档整理的完整接口分类。

## 🔧 设置函数

### 基础设置
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `set_universe()` | ✅ | ✅ | ✅ | 设置股票池 |
| `set_benchmark()` | ✅ | ✅ | ✅ | 设置基准 |
| `set_commission()` | ✅ | ✅ | ✅ | 设置佣金费率 |
| `set_fixed_slippage()` | ✅ | ✅ | ✅ | 设置固定滑点 |
| `set_slippage()` | ✅ | ✅ | ✅ | 设置滑点 |
| `set_volume_ratio()` | ✅ | ✅ | ✅ | 设置成交比例 |
| `set_limit_mode()` | ✅ | ✅ | ✅ | 设置回测成交数量限制模式 |
| `set_yesterday_position()` | ✅ | ✅ | ✅ | 设置底仓(股票) |
| `set_parameters()` | ✅ | ✅ | ✅ | 设置策略配置参数 |

### 期货设置 (V016/V041)
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `set_future_commission()` | ❌ | ✅ | ✅ | 设置期货手续费 |
| `set_margin_rate()` | ❌ | ✅ | ✅ | 设置期货保证金比例 |

## 📊 获取信息函数

### 基础信息
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_trading_day()` | ✅ | ✅ | ✅ | 获取交易日期 |
| `get_all_trades_days()` | ✅ | ✅ | ✅ | 获取全部交易日期 |
| `get_trade_days()` | ✅ | ✅ | ✅ | 获取指定范围交易日期 |

### 市场信息
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_market_list()` | ✅ | ✅ | ✅ | 获取市场列表 |
| `get_market_detail()` | ✅ | ✅ | ✅ | 获取市场详细信息 |
| `get_cb_list()` | ✅ | ❌ | ✅ | 获取可转债市场代码表 |

### 行情信息
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_history()` | ✅ | ✅ | ✅ | 获取历史行情 |
| `get_price()` | ✅ | ✅ | ✅ | 获取历史数据 |
| `get_individual_entrust()` | ✅ | ✅ | ✅ | 获取逐笔委托行情 |
| `get_individual_transcation()` | ✅ | ✅ | ✅ | 获取逐笔成交行情 |
| `get_tick_direction()` | ✅ | ✅ | ✅ | 获取分时成交行情 |
| `get_sort_msg()` | ✅ | ✅ | ✅ | 获取板块、行业的涨幅排名 |
| `get_etf_info()` | ✅ | ✅ | ✅ | 获取ETF信息 |
| `get_etf_stock_info()` | ✅ | ✅ | ✅ | 获取ETF成分券信息 |
| `get_gear_price()` | ✅ | ✅ | ✅ | 获取指定代码的档位行情价格 |
| `get_snapshot()` | ✅ | ✅ | ✅ | 取行情快照 |

### 股票信息
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_stock_name()` | ✅ | ✅ | ✅ | 获取股票名称 |
| `get_stock_info()` | ✅ | ✅ | ✅ | 获取股票基础信息 |
| `get_stock_status()` | ✅ | ✅ | ✅ | 获取股票状态信息 |
| `get_stock_exrights()` | ✅ | ✅ | ✅ | 获取股票除权除息信息 |
| `get_stock_blocks()` | ✅ | ✅ | ✅ | 获取股票所属板块信息 |
| `get_index_stocks()` | ✅ | ✅ | ✅ | 获取指数成份股 |
| `get_etf_stock_list()` | ✅ | ✅ | ✅ | 获取ETF成分券列表 |
| `get_industry_stocks()` | ✅ | ✅ | ✅ | 获取行业成份股 |
| `get_fundamentals()` | ✅ | ✅ | ✅ | 获取财务数据信息 |
| `get_Ashares()` | ✅ | ✅ | ✅ | 获取指定日期A股代码列表 |
| `get_etf_list()` | ✅ | ✅ | ✅ | 获取ETF代码 |

### 其他信息
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_trades_file()` | ✅ | ✅ | ✅ | 获取对账数据文件 |
| `convert_position_from_csv()` | ✅ | ✅ | ✅ | 获取设置底仓的参数列表(股票) |
| `get_user_name()` | ✅ | ✅ | ✅ | 获取登录终端的资金账号 |
| `get_deliver()` | ✅ | ✅ | ✅ | 获取历史交割单信息 |
| `get_fundjour()` | ✅ | ✅ | ✅ | 获取历史资金流水信息 |
| `get_research_path()` | ✅ | ✅ | ✅ | 获取研究路径 |
| `get_trade_name()` | ✅ | ✅ | ✅ | 获取交易名称 |

## 💰 交易相关函数

### 股票交易函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `order()` | ✅ | ✅ | ✅ | 按数量买卖 |
| `order_target()` | ✅ | ✅ | ✅ | 指定目标数量买卖 |
| `order_value()` | ✅ | ✅ | ✅ | 指定目标价值买卖 |
| `order_target_value()` | ✅ | ✅ | ✅ | 指定持仓市值买卖 |
| `order_market()` | ✅ | ✅ | ✅ | 按市价进行委托 |
| `ipo_stocks_order()` | ✅ | ✅ | ✅ | 新股一键申购 |
| `after_trading_order()` | ✅ | ✅ | ✅ | 盘后固定价委托 |
| `after_trading_cancel_order()` | ✅ | ✅ | ✅ | 盘后固定价委托撤单 |
| `etf_basket_order()` | ✅ | ✅ | ✅ | ETF成分券篮子下单 |
| `etf_purchase_redemption()` | ✅ | ✅ | ✅ | ETF基金申赎接口 |
| `get_positions()` | ✅ | ✅ | ✅ | 获取多支股票持仓信息 |

### 公共交易函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `order_tick()` | ✅ | ✅ | ✅ | tick行情触发买卖 |
| `cancel_order()` | ✅ | ✅ | ✅ | 撤单 |
| `cancel_order_ex()` | ✅ | ✅ | ✅ | 撤单 |
| `debt_to_stock_order()` | ✅ | ✅ | ✅ | 债转股委托 |
| `get_open_orders()` | ✅ | ✅ | ✅ | 获取未完成订单 |
| `get_order()` | ✅ | ✅ | ✅ | 获取指定订单 |
| `get_orders()` | ✅ | ✅ | ✅ | 获取全部订单 |
| `get_all_orders()` | ✅ | ✅ | ✅ | 获取账户当日全部订单 |
| `get_trades()` | ✅ | ✅ | ✅ | 获取当日成交订单 |
| `get_position()` | ✅ | ✅ | ✅ | 获取持仓信息 |

## 🏦 融资融券专用函数

### 融资融券交易类函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `margin_trade()` | ✅ | ✅ | ✅ | 担保品买卖 |
| `margincash_open()` | ✅ | ✅ | ✅ | 融资买入 |
| `margincash_close()` | ✅ | ✅ | ✅ | 卖券还款 |
| `margincash_direct_refund()` | ✅ | ✅ | ✅ | 直接还款 |
| `marginsec_open()` | ✅ | ✅ | ✅ | 融券卖出 |
| `marginsec_close()` | ✅ | ✅ | ✅ | 买券还券 |
| `marginsec_direct_refund()` | ✅ | ✅ | ✅ | 直接还券 |

### 融资融券查询类函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_margincash_stocks()` | ✅ | ✅ | ✅ | 获取融资标的列表 |
| `get_marginsec_stocks()` | ✅ | ✅ | ✅ | 获取融券标的列表 |
| `get_margin_contract()` | ✅ | ✅ | ✅ | 合约查询 |
| `get_margin_contractreal()` | ✅ | ✅ | ✅ | 实时合约查询 |
| `get_margin_assert()` | ✅ | ✅ | ✅ | 信用资产查询 |
| `get_assure_security_list()` | ✅ | ✅ | ✅ | 担保券查询 |
| `get_margincash_open_amount()` | ✅ | ✅ | ✅ | 融资标的最大可买数量查询 |
| `get_margincash_close_amount()` | ✅ | ✅ | ✅ | 卖券还款标的最大可卖数量查询 |
| `get_marginsec_open_amount()` | ✅ | ✅ | ✅ | 融券标的最大可卖数量查询 |
| `get_marginsec_close_amount()` | ✅ | ✅ | ✅ | 买券还券标的最大可买数量查询 |
| `get_margin_entrans_amount()` | ✅ | ✅ | ✅ | 现券还券数量查询 |

## 📈 期货专用函数 (V016/V041)

### 期货交易类函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `buy_open()` | ❌ | ✅ | ✅ | 开多 |
| `sell_close()` | ❌ | ✅ | ✅ | 多平 |
| `sell_open()` | ❌ | ✅ | ✅ | 空开 |
| `buy_close()` | ❌ | ✅ | ✅ | 空平 |

### 期货查询类函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_margin_rate()` | ❌ | ✅ | ✅ | 获取用户设置的保证金比例 |
| `get_instruments()` | ❌ | ✅ | ✅ | 获取合约信息 |

## 📊 期权专用函数 (V016/V041)

### 期权查询类函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_opt_objects()` | ❌ | ✅ | ✅ | 获取期权标的列表 |
| `get_opt_last_dates()` | ❌ | ✅ | ✅ | 获取期权标的到期日列表 |
| `get_opt_contracts()` | ❌ | ✅ | ✅ | 获取期权标的对应合约列表 |
| `get_contract_info()` | ❌ | ✅ | ✅ | 获取期权合约信息 |
| `get_covered_lock_amount()` | ❌ | ✅ | ✅ | 获取期权标的可备兑锁定数量 |
| `get_covered_unlock_amount()` | ❌ | ✅ | ✅ | 获取期权标的允许备兑解锁数量 |

### 期权交易类函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `buy_open()` | ❌ | ✅ | ✅ | 权利仓开仓 |
| `sell_close()` | ❌ | ✅ | ✅ | 权利仓平仓 |
| `sell_open()` | ❌ | ✅ | ✅ | 义务仓开仓 |
| `buy_close()` | ❌ | ✅ | ✅ | 义务仓平仓 |
| `open_prepared()` | ❌ | ✅ | ✅ | 备兑开仓 |
| `close_prepared()` | ❌ | ✅ | ✅ | 备兑平仓 |
| `option_exercise()` | ❌ | ✅ | ✅ | 行权 |

### 期权其他函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `option_covered_lock()` | ❌ | ✅ | ✅ | 期权标的备兑锁定 |
| `option_covered_unlock()` | ❌ | ✅ | ✅ | 期权标的备兑解锁 |

## 📊 计算函数

### 技术指标计算函数 (V016/V041)
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_MACD()` | ❌ | ✅ | ✅ | 异同移动平均线 |
| `get_KDJ()` | ❌ | ✅ | ✅ | 随机指标 |
| `get_RSI()` | ❌ | ✅ | ✅ | 相对强弱指标 |
| `get_CCI()` | ❌ | ✅ | ✅ | 顺势指标 |

## 🔧 其他函数

### 通用工具函数
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `log()` | ✅ | ✅ | ✅ | 日志记录 |
| `is_trade()` | ✅ | ✅ | ✅ | 业务代码场景判断 |
| `check_limit()` | ✅ | ✅ | ✅ | 代码涨跌停状态判断 |
| `send_email()` | ✅ | ✅ | ✅ | 发送邮箱信息 |
| `permission_test()` | ✅ | ✅ | ✅ | 权限校验 |
| `create_dir()` | ✅ | ✅ | ✅ | 创建文件路径 |

### V005 独有功能
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `send_qywx()` | ✅ | ❌ | ✅ | 发送企业微信信息 |
| `get_frequency()` | ✅ | ❌ | ❌ | 获取当前业务代码周期 |
| `fund_transfer()` | ✅ | ❌ | ❌ | 资金调拨 |
| `set_email_info()` | ✅ | ❌ | ❌ | 设置邮件信息 |

### V041 独有功能
| 函数名 | V005 | V016 | V041 | 说明 |
|--------|------|------|------|------|
| `get_cb_info()` | ✅ | ❌ | ✅ | 获取可转债基础信息 |
| `get_enslo_security_info()` | ✅ | ❌ | ✅ | 融券头寸信息查询 |
| `get_ipo_stocks()` | ✅ | ❌ | ✅ | 获取当日IPO申购标的 |

## 📊 统计总结

| 版本 | 总函数数 | 独有函数数 | 覆盖率 |
|------|----------|-----------|--------|
| **V005 (社区维护)** | ~120 | 4 | 85% |
| **V016 (国盛证券)** | ~130 | 0 | 90% |
| **V041 (东莞证券)** | ~140 | 3 | 100% |

## ⚠️ 交易注意事项

### 委托处理最佳实践

#### 1. 委托失败处理
```python
def safe_order(security, amount, limit_price=None):
    """安全委托函数，包含错误处理"""
    try:
        # 检查委托数量
        if not isinstance(amount, int):
            log.error(f"委托数量必须为整数: {amount}")
            return None

        # 检查行情数据
        if limit_price is None:
            snapshot = get_snapshot(security)
            if not snapshot[security]:
                log.error(f"获取行情失败: {security}")
                return None

            limit_price = snapshot[security].get('last_px', 0)
            if limit_price == 0:
                log.error(f"行情数据异常: {security}")
                return None

        # 执行委托
        order_id = order(security, amount, limit_price=limit_price)
        if order_id is None:
            log.error(f"委托失败: {security}, amount: {amount}, price: {limit_price}")

        return order_id

    except Exception as e:
        log.error(f"委托异常: {e}")
        return None
```

#### 2. 委托状态监控
```python
def monitor_orders(context):
    """监控委托状态"""
    open_orders = get_open_orders()

    for order_id, order_info in open_orders.items():
        # 检查委托时间
        order_time = order_info.add_time
        current_time = context.current_dt

        # 超过5分钟未成交，考虑撤单
        if (current_time - order_time).seconds > 300:
            cancel_result = cancel_order(order_id)
            if cancel_result:
                log.info(f"撤销超时委托: {order_id}")
            else:
                log.warning(f"撤单失败: {order_id}")

def handle_data(context, data):
    # 在每次handle_data中监控委托
    monitor_orders(context)
```

#### 3. 隔夜单处理
```python
def handle_after_trading_end(context, data):
    """盘后处理，准备隔夜单"""
    # 15:00后的委托会成为隔夜单
    current_time = context.current_dt.time()

    if current_time >= datetime.time(15, 0):
        # 准备次日开盘的委托
        for security in context.universe:
            # 计算次日开盘价预期
            expected_price = calculate_expected_open_price(security)

            # 下隔夜单
            order_id = order(security, 100, limit_price=expected_price)
            log.info(f"隔夜单: {security}, 预期价格: {expected_price}")

def calculate_expected_open_price(security):
    """计算预期开盘价"""
    # 获取最新收盘价
    latest_price = get_history(1, '1d', 'close', security).iloc[-1]

    # 简单预测：使用收盘价
    return latest_price
```

### 账户数据同步

#### 1. 账户数据更新频率
```python
def initialize(context):
    g.last_account_update = None
    g.account_cache = {}

def get_account_info_safe(context):
    """安全获取账户信息，考虑6秒更新频率"""
    current_time = context.current_dt

    # 检查是否需要更新（6秒间隔）
    if (g.last_account_update is None or
        (current_time - g.last_account_update).seconds >= 6):

        # 更新账户信息
        g.account_cache = {
            'cash': context.portfolio.cash,
            'total_value': context.portfolio.total_value,
            'positions': dict(context.portfolio.positions)
        }
        g.last_account_update = current_time

    return g.account_cache
```

#### 2. 防止重复交易
```python
def initialize(context):
    g.trade_flags = {}  # 交易标志
    g.last_trade_time = {}  # 最后交易时间

def safe_trade_with_flag(context, security, amount):
    """带标志的安全交易，防止重复"""
    current_time = context.current_dt

    # 检查交易标志
    if g.trade_flags.get(security, False):
        log.info(f"股票 {security} 已有交易标志，跳过")
        return None

    # 检查最后交易时间（避免频繁交易）
    last_time = g.last_trade_time.get(security)
    if last_time and (current_time - last_time).seconds < 60:
        log.info(f"股票 {security} 交易过于频繁，跳过")
        return None

    # 执行交易
    order_id = safe_order(security, amount)

    if order_id:
        g.trade_flags[security] = True
        g.last_trade_time[security] = current_time

        # 设置定时清除标志
        run_daily(context, lambda ctx: clear_trade_flag(security),
                 time='15:30')

    return order_id

def clear_trade_flag(security):
    """清除交易标志"""
    if security in g.trade_flags:
        del g.trade_flags[security]
```

### 模拟交易稳定性

#### 1. 行情数据保护
```python
def get_safe_snapshot(securities):
    """安全获取行情快照"""
    max_retries = 3

    for attempt in range(max_retries):
        try:
            snapshots = get_snapshot(securities)

            # 验证数据完整性
            valid_snapshots = {}
            for security in securities:
                if (security in snapshots and
                    snapshots[security] and
                    snapshots[security].get('last_px', 0) > 0):
                    valid_snapshots[security] = snapshots[security]
                else:
                    log.warning(f"行情数据异常: {security}")

            if valid_snapshots:
                return valid_snapshots

        except Exception as e:
            log.error(f"获取行情失败，第{attempt + 1}次重试: {e}")

        if attempt < max_retries - 1:
            time.sleep(1)

    log.error("获取行情最终失败")
    return {}
```

#### 2. 交易模块运行顺序控制
```python
def initialize(context):
    g.before_trading_done = False
    g.handle_data_enabled = False

def before_trading_start(context, data):
    """开盘前处理"""
    try:
        # 执行开盘前逻辑
        prepare_daily_data(context)

        # 标记完成
        g.before_trading_done = True
        g.handle_data_enabled = True

        log.info("开盘前处理完成")

    except Exception as e:
        log.error(f"开盘前处理失败: {e}")
        g.handle_data_enabled = False

def handle_data(context, data):
    """主交易逻辑"""
    # 检查前置条件
    if not g.handle_data_enabled:
        log.info("handle_data未启用，跳过")
        return

    try:
        # 执行交易逻辑
        execute_trading_logic(context, data)

    except Exception as e:
        log.error(f"交易逻辑执行失败: {e}")

def tick_data(context):
    """Tick数据处理"""
    # 检查前置条件
    if not g.before_trading_done:
        log.info("开盘前处理未完成，跳过tick处理")
        return

    try:
        # 执行tick逻辑
        execute_tick_logic(context)

    except Exception as e:
        log.error(f"Tick逻辑执行失败: {e}")
```

---

> **说明**: 此分类基于三个版本的实际API文档对比整理
> **更新**: 定期更新以反映最新版本差异
