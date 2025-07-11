# Ptrade API 参考文档

欢迎来到 Ptrade API 完整参考文档。本文档涵盖了 Ptrade 量化交易平台的所有API接口，按功能模块进行分类组织。

## 📋 文档导航

### 🏗️ 核心框架
- [**框架基础**](framework.md) - 策略框架、生命周期、事件处理
- [**数据对象**](objects.md) - Order、Position、Security等核心对象定义
- [**工具函数**](utilities.md) - 日志、时间、数据转换等辅助工具

### 📈 交易接口
- [**股票交易**](stock-trading.md) - 股票、ETF、可转债等现货交易接口
- [**期货交易**](futures.md) - 期货合约交易、持仓管理接口
- [**期权交易**](options.md) - 期权合约交易、行权等接口
- [**融资融券**](margin-trading.md) - 融资买入、融券卖出、担保品管理

### 📊 数据接口
- [**行情数据**](market-data.md) - K线、实时行情、L2数据获取
- [**股票信息**](stock-info.md) - 股票基本信息、财务数据查询
- [**财务数据**](financial-data.md) - 财务报表、财务指标数据
- [**基础信息**](basic-info.md) - 交易日历、股票列表等基础数据

### 🔧 分析工具
- [**技术指标**](technical-indicators.md) - MACD、KDJ、RSI等技术指标计算
- [**系统设置**](settings.md) - 参数配置、通知设置、系统管理

## 🚀 快速查找

### 按使用频率
| 高频使用 | 中频使用 | 低频使用 |
|---------|---------|---------|
| [下单交易](stock-trading.md#基础下单函数) | [期货交易](futures.md) | [系统设置](settings.md) |
| [获取行情](market-data.md#历史行情) | [期权交易](options.md) | [财务数据](financial-data.md) |
| [查询持仓](stock-trading.md#持仓查询) | [融资融券](margin-trading.md) | [基础信息](basic-info.md) |
| [技术指标](technical-indicators.md) | [股票信息](stock-info.md) | [工具函数](utilities.md) |

### 按交易类型
- **现货交易**: [股票交易](stock-trading.md) → [行情数据](market-data.md) → [技术指标](technical-indicators.md)
- **衍生品交易**: [期货交易](futures.md) / [期权交易](options.md) → [行情数据](market-data.md)
- **信用交易**: [融资融券](margin-trading.md) → [股票交易](stock-trading.md)

### 按开发阶段
- **策略开发**: [框架基础](framework.md) → [数据对象](objects.md) → [工具函数](utilities.md)
- **数据获取**: [行情数据](market-data.md) → [股票信息](stock-info.md) → [财务数据](financial-data.md)
- **交易执行**: [股票交易](stock-trading.md) → [期货交易](futures.md) → [期权交易](options.md)
- **系统配置**: [系统设置](settings.md) → [基础信息](basic-info.md)

## 📖 版本说明

本API文档基于三个主要版本整理：
- **东莞证券版本** (V041) - 功能最全，包含最新特性
- **国盛证券版本** (V016) - 稳定标准版本
- **社区维护版本** (V005) - 社区增强版本

> 💡 **提示**: 不同版本间存在接口差异，详见 [版本差异对比](../version-differences.md)

## 🔗 相关文档

- [**API分类索引**](../api-classification.md) - 按功能分类的完整API列表
- [**策略示例**](../examples.md) - 实际使用案例和最佳实践
- [**版本对比**](../versions/) - 详细的版本功能对比
- [**常见问题**](../advanced/faq.md) - 开发中的常见问题解答

## 📝 使用建议

1. **新手用户**: 建议从 [框架基础](framework.md) 开始，了解整体架构
2. **有经验用户**: 可直接查看具体的交易或数据接口文档
3. **版本迁移**: 请参考 [版本差异对比](../version-differences.md) 了解兼容性

---

> 📚 **文档维护**: 本文档持续更新中，如发现错误或需要补充，欢迎提交Issue或PR
