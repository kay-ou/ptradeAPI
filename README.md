# Ptrade API 文档

欢迎使用 Ptrade API！这是一个功能强大的量化交易API，支持股票、期货、期权等多种金融产品的程序化交易。

## 🚀 快速开始

- [使用说明](docs/getting-started/usage.md) - 了解如何新建策略、回测和交易
- [快速入门](docs/getting-started/quick-start.md) - 从简单示例开始学习
- [策略示例](docs/getting-started/examples.md) - 查看完整的策略示例

## 📚 API 参考文档

### 核心框架
- [策略引擎框架](docs/api-reference/framework.md) - initialize、handle_data等核心函数
- [设置函数](docs/api-reference/settings.md) - 股票池、基准、佣金等设置

### 数据获取
- [基础信息API](docs/api-reference/basic-info.md) - 交易日、市场信息等
- [行情数据API](docs/api-reference/market-data.md) - 历史行情、实时数据等
- [股票信息API](docs/api-reference/stock-info.md) - 股票基础信息、财务数据等

### 交易功能
- [股票交易API](docs/api-reference/stock-trading.md) - 股票买卖、订单管理
- [融资融券API](docs/api-reference/margin-trading.md) - 融资融券交易
- [期货交易API](docs/api-reference/futures.md) - 期货交易相关功能
- [期权交易API](docs/api-reference/options.md) - 期权交易相关功能

### 工具函数
- [技术指标](docs/api-reference/technical-indicators.md) - MACD、KDJ、RSI等技术指标
- [工具函数](docs/api-reference/utilities.md) - 日志、邮件、权限等工具
- [对象说明](docs/api-reference/objects.md) - Context、Portfolio、Order等对象

## 🔧 高级功能

- [常见问题](docs/advanced/faq.md) - 常见问题解答
- [支持的三方库](docs/advanced/supported-libraries.md) - 可用的Python库
- [版本变动](docs/advanced/version-changes.md) - API版本更新记录

## 📋 支持的业务类型

### 回测支持
- 普通股票买卖（单位：股）
- 可转债买卖（单位：张，T+0）
- 融资融券担保品买卖（单位：股）
- 期货投机类型交易（单位：手，T+0）
- LOF基金买卖（单位：股）
- ETF基金买卖（单位：股）

### 交易支持
- 普通股票买卖（单位：股）
- 可转债买卖（T+0）
- 融资融券交易（单位：股）
- ETF申赎、套利（单位：份）
- 国债逆回购（单位：份）
- 期货投机类型交易（单位：手，T+0）
- LOF基金买卖（单位：股）
- ETF基金买卖（单位：股）
- 期权交易（单位：手）

## 🏢 多版本支持

本文档支持多个版本和不同券商的API：

- [当前版本文档](docs/api-reference/) - 通用API文档
- [历史版本](docs/versions/) - 查看历史版本文档（预留）
- [券商特定说明](docs/brokers/) - 不同券商的特殊配置（预留）

## 📖 文档导航

### 按使用场景
- **新手入门**: [使用说明](docs/getting-started/usage.md) → [快速入门](docs/getting-started/quick-start.md)
- **API查询**: [API参考文档](#-api-参考文档)
- **问题解决**: [常见问题](docs/advanced/faq.md)

### 按交易类型
- **股票交易**: [股票交易API](docs/api-reference/stock-trading.md)
- **融资融券**: [融资融券API](docs/api-reference/margin-trading.md)
- **期货交易**: [期货交易API](docs/api-reference/futures.md)
- **期权交易**: [期权交易API](docs/api-reference/options.md)

## 🔄 版本信息

- **当前版本**: v1.0
- **最后更新**: 2024年
- **兼容性**: 支持Python 3.6+

## 📞 技术支持

如果您在使用过程中遇到问题，请：

1. 首先查看 [常见问题](docs/advanced/faq.md)
2. 查阅相关的API文档
3. 联系技术支持团队

---

> **注意**: 本文档结构经过优化，将原来的大文档拆分为多个小文档，提高加载速度和维护效率。所有API功能保持不变。
