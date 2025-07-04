# 接口版本变动

本文档记录了 Ptrade API 的版本更新历史和接口变动情况。

## 当前版本

**版本号**: PBOXQT1.0V202202.01.041

## 版本更新历史

### PBOXQT1.0V202101.08.000

1. [initialize](../api-reference/framework.md#initialize)对部分API接口调用进行限制，仅initialize可调用接口说明中的API可在initialize函数内使用；
2. [before_trading_start](../api-reference/framework.md#before_trading_start)和[after_trading_end](../api-reference/framework.md#after_trading_end)对两融委托API接口调用进行限制；
3. 新增[get_cb_info](../api-reference/market-data.md#get_cb_info)API接口，用于获取可转债基础信息；
4. 新增[get_enslo_security_info](../api-reference/margin-trading.md#get_enslo_security_info)API接口，用于获取融券头寸信息；

### PBOXQT1.0V202101.07.000

1. [get_snapshot](../api-reference/market-data.md#get_snapshot)新增wavg_px(加权平均价)、px_change_rate(涨跌幅)出参；
2. 可转债回测业务新增支持T+0；
3. 新增支持融资融券回测业务，[融资融券专用函数](../api-reference/margin-trading.md)中暂只支持[margin_trade](../api-reference/margin-trading.md#margin_trade)接口；

### PBOXQT1.0V202101.06.000

1. 新增[get_user_name](../api-reference/utilities.md#get_user_name)API接口，用于获取登录终端的资金账号；
2. 研究中[get_price](../api-reference/market-data.md#get_price)新增支持获取周线数据；
3. [get_snapshot](../api-reference/market-data.md#get_snapshot)新增支持获取XBHS行业版块市场数据；
4. [send_qywx](../api-reference/utilities.md#send_qywx)新增toparty(发送对象为部门)、touser(发送内容为个人)、totag(发送内容为分组)入参；

### PBOXQT1.0V202101.05.000

1. 信用账户支持[ipo_stocks_order](../api-reference/stock-trading.md#ipo_stocks_order)接口调用；
2. 由于行情源返回信息不包含，[get_fundamentals](../api-reference/stock-info.md#get_fundamentals)获取growth_ability、profit_ability、eps、operating_ability、debt_paying_ability表不再返回company_type字段；
3. 由于上交所债券业务规则变更，调用[debt_to_stock_order](../api-reference/stock-trading.md#debt_to_stock_order)接口对上海市场可转债进行转股操作时需传入可转债代码，不再传入转股代码；

### PBOXQT1.0V202101.04.000

1. 修复[get_all_orders](../api-reference/stock-trading.md#get_all_orders)获取特定委托状态报错问题，status字段返回数据类型从int改为str；
2. [on_order_response](../api-reference/framework.md#on_order_response)、[on_trade_response](../api-reference/framework.md#on_trade_response)支持获取非本策略交易的主推信息(需券商配置默认不推送)，且on_order_response推送非本策略交易的主推信息时不包含order_id字段；
3. 相关功能优化；

### PBOXQT1.0V202101.03.000

1. [on_order_response](../api-reference/framework.md#on_order_response)主推信息中新增entrust_type、entrust_prop字段；
2. 修复信用交易接口兼容问题；
3. [get_price](../api-reference/market-data.md#get_price)、[get_history](../api-reference/market-data.md#get_history)支持周频(1w)行情获取；
4. 由于行情源不再更新维护，[get_fundamentals](../api-reference/stock-info.md#get_fundamentals)接口去除share_change表；

## 重要变更说明

### 数据类型变更

- **get_all_orders**: status字段返回类型从int改为str
- **get_fundamentals**: 部分表格去除company_type字段

### 新增功能

- **周线数据支持**: get_price和get_history支持1w频率
- **可转债T+0**: 回测支持可转债T+0交易
- **融资融券回测**: 新增融资融券回测功能
- **主推信息增强**: 支持获取非本策略交易的主推信息

### 接口限制

- **initialize函数**: 限制可调用的API接口范围
- **盘前盘后函数**: 限制融资融券接口调用

### 业务规则变更

- **可转债转股**: 上海市场需传入可转债代码而非转股代码

## 兼容性说明

### 向后兼容

大部分API接口保持向后兼容，现有策略无需修改即可继续使用。

### 不兼容变更

以下变更可能影响现有策略：

1. **get_all_orders状态字段**: 如果策略中对status字段进行了类型判断，需要修改为字符串比较
2. **可转债转股**: 上海市场的转股操作需要修改传入参数
3. **get_fundamentals**: 如果使用了被移除的字段，需要调整代码

## 升级建议

### 检查清单

在升级到新版本前，请检查以下项目：

1. **数据类型**: 确认status字段的使用方式
2. **可转债转股**: 检查转股代码的使用
3. **财务数据**: 确认get_fundamentals的字段使用
4. **函数调用位置**: 确认API调用是否在正确的函数中

### 测试建议

1. **回测验证**: 在新版本上重新运行历史回测
2. **模拟交易**: 先在模拟环境测试策略
3. **逐步升级**: 分批升级策略，观察运行情况

## 未来规划

### 即将推出

- 更多技术指标支持
- 期权交易功能增强
- 性能优化改进

### 长期规划

- 多市场支持扩展
- 实时数据源优化
- 策略回测性能提升

## 获取更新

### 更新通知

- 关注版本发布公告
- 订阅技术更新邮件
- 查看官方文档更新

### 技术支持

如果在版本升级过程中遇到问题，请：

1. 查看[常见问题](faq.md)
2. 联系技术支持团队
3. 参考[API文档](../api-reference/)

---

> **注意**: 建议在生产环境使用前，先在测试环境验证新版本的兼容性。
