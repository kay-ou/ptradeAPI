# Ptrade API 文档项目

> **Ptrade量化交易API的完整文档库** - 基于三个主要版本的详细对比分析和使用指南

> **用这个邀请码注册我得50你得100美金Claude Code额度：https://anyrouter.top/register?aff=5UV9**

## 🎯 项目简介

Ptrade是由恒生电子开发的量化交易API平台，被多家券商采用并进行定制化部署。本项目整理了三个主要版本的完整文档，包括：

- **东莞证券版本** (PBOXQT1.0V202202.01.041) - 最新功能版本
- **国盛证券版本** (PBOXQT1.0V202202.01.016) - 稳定标准版本
- **社区维护版本** (PBOXQT1.0V202202.00.005) - 社区增强版本

## ✨ 项目特色

### 📊 基于实际API文档的版本对比
- 通过对比三个版本的真实API文档发现技术差异
- 详细分析函数调用和返回值的具体差异
- 提供升级指南和兼容性建议

### 🔍 完整的功能分类和索引
- 按功能分类整理所有API接口
- 清晰标注各版本的支持情况
- 提供完整的策略示例库

### 💡 实用的最佳实践
- 基于官方QA文档的最佳实践
- 性能优化和稳定性建议
- 错误处理和调试技巧

### 📚 丰富的学习资源
- 从基础到高级的完整策略示例
- 详细的财务数据API文档
- 有用链接和学习资源汇总

## 🚀 快速开始

### 1. 选择您的版本
根据您使用的券商环境选择对应版本：

| 券商 | 版本号 | 特点 | 推荐用途 |
|------|--------|------|----------|
| **东莞证券** | V041 | 最新功能，完整支持 | 专业交易，需要最新特性 |
| **国盛证券** | V016 | 稳定可靠，标准功能 | 生产环境，追求稳定性 |
| **社区维护** | V005 | 学习友好，示例丰富 | 学习研究，功能探索 |

👉 **不确定选哪个？** 查看 [版本选择指南](docs/getting-started/README.md) 或 [详细版本对比](docs/versions/version-comparison-table.md)

### 2. 根据您的需求选择入口

#### 🎓 我是新手，想学习
- [入门指南](docs/getting-started/) - 从零开始学习
- [策略示例](docs/examples.md) - 看实际代码学习

#### 🔍 我要查API接口
- [API参考文档](docs/api-reference/) - 完整接口说明
- [API分类索引](docs/api-classification.md) - 按功能查找

#### ⚖️ 我要对比版本差异
- [版本差异详细对比](docs/version-differences.md) - 技术差异分析
- [功能对比表](docs/versions/version-comparison-table.md) - 功能支持对比

#### 📊 我要查数据分类
- [行业概念数据](docs/industry-concept-data.md) - 行业分类代码
- [财务数据对比](docs/versions/financial-data-comparison.md) - 财务数据差异

#### ❓ 我遇到了问题
- [常见问题解答](docs/advanced/faq.md) - 问题排查指南

## 📁 文档结构

```
docs/
├── getting-started/        # 入门指南
├── api-reference/         # API参考文档
├── examples.md           # 策略示例
├── api-classification.md  # API分类
├── industry-concept-data.md # 行业概念分类数据
├── versions/              # 版本信息和对比
├── version-differences.md # 版本差异对比
└── advanced/              # 高级功能
```

## 🔍 主要发现

### 关键技术差异
通过对比三个版本的实际API文档，我们发现了以下重要差异：

#### 1. 委托状态字段类型变化 ⚠️ (最重要)
```python
# V005: int类型
if order.status == 8:

# V016/V041: str类型
if order.status == '8':
```

#### 2. 版本独有功能
- **V005独有**: 企业微信推送、资金调拨、邮件设置
- **V016缺少**: 企业微信、可转债专门接口、融券信息查询
- **V041最全**: 包含所有新功能和最新字段更新

#### 3. 技术指标支持
- **V005**: 需手动计算MACD等指标
- **V016/V041**: 内置`get_MACD()`, `get_KDJ()`, `get_RSI()`, `get_CCI()`

## 📖 使用指南

### 🎯 按角色导航

#### 新手用户
1. **了解基础** → [入门指南](docs/getting-started/)
2. **看代码学习** → [策略示例](docs/examples.md)
3. **查找接口** → [API参考](docs/api-reference/)

#### 开发者
1. **查看完整API** → [API参考文档](docs/api-reference/)
2. **学习最佳实践** → [策略示例](docs/examples.md)
3. **处理版本兼容** → [版本差异对比](docs/version-differences.md)

#### 运维人员
1. **了解平台限制** → [版本差异说明](docs/version-differences.md)
2. **解决常见问题** → [FAQ问答](docs/advanced/faq.md)
3. **查看支持库** → [高级功能](docs/advanced/)

## 📚 学习资源

- [策略示例库](docs/examples.md) - 从基础到高级的完整示例
- [高级功能](docs/advanced/) - 常见问题、支持库、版本变动

## 🤝 贡献指南

本项目基于公开的API文档整理，欢迎贡献：

1. **发现错误**: 提交Issue报告文档错误
2. **补充内容**: 提交PR添加新的策略示例或最佳实践
3. **版本更新**: 帮助更新新版本的API差异

## ⚠️ 免责声明

- 本项目仅用于学习和研究目的
- 所有策略示例仅供参考，实盘交易请充分测试
- 具体API功能以各券商实际部署为准
- 投资有风险，交易需谨慎

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

> **最后更新**: 2024年
> **维护状态**: 活跃维护中
> **文档版本**: 基于三个主要版本的实际API文档整理
