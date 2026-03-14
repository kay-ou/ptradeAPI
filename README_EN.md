# Ptrade API Documentation Project

**Complete documentation library for Ptrade quantitative trading API** - Detailed comparative analysis and usage guide based on three main versions

> **Recommended: SimTradeDesk** - A professional desktop environment designed for Ptrade strategy developers, providing Ptrade-compatible APIs, strategy editor, backtesting system, parameter optimizer, and more. No Python environment setup required - just download, install, and start using. For details, visit **[SimTradeDesk](http://github.com/kay-ou/SimTradeDesk)**.

> For official access instructions and processes related to Ptrade interfaces, please send a private message, and I will provide a reference path "containing only official information sources".
> Ptrade Developer QQ Group: 590529320

## 📑 Language Versions

- [English](README_EN.md) - This page
- [中文 (Chinese)](README.md) - Chinese version

## 🌐 API Documentation Language Versions

- [Chinese API Documentation](docs/api-reference/README.md)
- [English API Documentation](docs/api-reference-en/README.md)

## 🎯 Project Introduction

Ptrade is a quantitative trading API platform developed by Hundsun Electronics, adopted and customized by multiple securities firms. This project organizes complete documentation for three main versions, including:

- **Dongguan Securities version** (PBOXQT1.0V202202.01.041) - Latest feature version
- **Guosheng Securities version** (PBOXQT1.0V202202.01.016) - Stable standard version
- **Community-maintained version** (PBOXQT1.0V202202.00.005) - Community-enhanced version

## ✨ Project Features

### 📊 Version Comparison Based on Actual API Documentation
- Discover technical differences by comparing real API documentation of three versions
- Detailed analysis of specific differences in function calls and return values
- Provide upgrade guides and compatibility recommendations

### 🔍 Complete Function Classification and Index
- Organize all API interfaces by function category
- Clearly mark support status for each version
- Provide a complete strategy example library

### 💡 Practical Best Practices
- Best practices based on official QA documentation
- Performance optimization and stability suggestions
- Error handling and debugging techniques

### 📚 Rich Learning Resources
- Complete strategy examples from basic to advanced
- Detailed financial data API documentation
- Useful links and learning resource summaries

## 🚀 Quick Start

### 1. Choose Your Version
Select the corresponding version based on your brokerage environment:

| Brokerage | Version | Features | Recommended Use |
|-----------|---------|----------|----------------|
| **Dongguan Securities** | V041 | Latest features, full support | Professional trading, requires latest features |
| **Guosheng Securities** | V016 | Stable and reliable, standard features | Production environment, pursuing stability |
| **Community-maintained** | V005 | Learning-friendly, rich examples | Learning research, feature exploration |

👉 **Unsure which to choose?** Check the [Version Selection Guide](docs/getting-started/README.md) or [Detailed Version Comparison](docs/versions/version-comparison-table.md)

### 2. Choose Your Entry Point Based on Your Needs

#### 🎓 I'm a beginner, want to learn
- [📖 Getting Started Guide](docs/getting-started/) - Learn Ptrade from scratch
- [💡 Strategy Examples](docs/examples.md) - Learn from actual code
- [📚 Complete Documentation Navigation](docs/) - Documentation library main entry

#### 🔍 I need to check API interfaces
- [📋 API Reference Documentation](docs/api-reference/) - Complete API interface descriptions and navigation
- [🔖 API Classification Index](docs/api-classification.md) - Function-based interface quick reference
- [📊 Industry Concept Data](docs/industry-concept-data.md) - Industry classification and concept sector data

#### ⚖️ I need to compare version differences
- [🔍 Version Difference Comparison](docs/version-differences.md) - Main technical difference analysis
- [📊 Version Details](docs/versions/) - Complete version feature comparison and selection guide
- [📄 Original Documentation](docs/original/) - Complete original API documentation for all three versions

#### ❓ I encountered a problem
- [🔧 Advanced Features and FAQ](docs/advanced/) - Common questions, support libraries, version changes, etc.
- [❓ Frequently Asked Questions](docs/advanced/faq.md) - Detailed problem troubleshooting guide

## 📁 Documentation Structure

```
docs/
├── README.md              # 📚 Documentation library main entry
├── getting-started/       # 🎓 Getting started guide
│   ├── README.md          # Getting started navigation
│   ├── quick-start.md     # Quick start
│   └── ...               # Other getting started documents
├── api-reference/         # 📋 API reference documentation
│   ├── README.md          # API documentation homepage and navigation
│   ├── stock-trading.md   # Stock trading interfaces
│   ├── market-data.md     # Market data interfaces
│   ├── technical-indicators.md # Technical indicator interfaces
│   └── ...               # Other API module documentation
├── examples.md           # 💡 Strategy example library
├── api-classification.md  # 🔖 API classification index
├── industry-concept-data.md # 📊 Industry concept classification data
├── versions/              # ⚖️ Version information and comparison
│   ├── README.md          # Version selection guide
│   ├── version-comparison-table.md # Feature comparison table
│   └── ...               # Other version documents
├── version-differences.md # 🔍 Version difference comparison
├── original/              # 📄 Original documentation
│   ├── README.md          # Original documentation navigation
│   ├── Ptrade社区.md      # Community version original documentation
│   ├── Ptrade国盛.md      # Guosheng version original documentation
│   └── ...               # Other original documents
└── advanced/              # 🔧 Advanced features
    ├── README.md          # Advanced features navigation
    ├── faq.md            # Frequently asked questions
    └── ...               # Other advanced documents
```

## 🔍 Key Findings

### Critical Technical Differences
By comparing the actual API documentation of the three versions, we found the following important differences:

#### 1. Order Status Field Type Change ⚠️ (Most Important)
```python
# V005: int type
if order.status == 8:

# V016/V041: str type
if order.status == '8':
```

#### 2. Version-Exclusive Features
- **V005 exclusive**: WeChat Work push, fund transfer, email settings
- **V016 missing**: WeChat Work, convertible bond dedicated interfaces, margin trading information query
- **V041 most complete**: Includes all new features and latest field updates

#### 3. Technical Indicator Support
- **V005**: Need to manually calculate MACD and other indicators
- **V016/V041**: Built-in `get_MACD()`, `get_KDJ()`, `get_RSI()`, `get_CCI()`

## 📖 Usage Guide

### 🎯 Navigation by Role

#### New Users
1. **Understand the basics** → [Getting Started Guide](docs/getting-started/)
2. **Learn from code** → [Strategy Examples](docs/examples.md)
3. **Find interfaces** → [API Reference](docs/api-reference/)

#### Developers
1. **View complete API** → [API Reference Documentation](docs/api-reference/)
2. **Learn best practices** → [Strategy Examples](docs/examples.md)
3. **Handle version compatibility** → [Version Difference Comparison](docs/version-differences.md)

#### Operations Personnel
1. **Understand platform limitations** → [Version Difference Explanation](docs/version-differences.md)
2. **Solve common problems** → [FAQ](docs/advanced/faq.md)
3. **View support libraries** → [Advanced Features](docs/advanced/)

## 📚 Learning Resources

- [Strategy Example Library](docs/examples.md) - Complete examples from basic to advanced
- [Advanced Features](docs/advanced/) - Common questions, support libraries, version changes

## 🤝 Contribution Guide

This project is based on publicly available API documentation collation. Contributions are welcome:

1. **Report errors**: Submit an Issue to report documentation errors
2. **Add content**: Submit a PR to add new strategy examples or best practices
3. **Version updates**: Help update API differences for new versions

## ⚠️ Disclaimer

- This project is for learning and research purposes only
- All strategy examples are for reference only, please fully test before live trading
- Specific API functions are subject to actual deployment by each brokerage
- Investment involves risks, trading requires caution

## 📄 License

This project uses the MIT License - see the [LICENSE](LICENSE) file for details

---

> **Last updated**: December 2024
> **Maintenance status**: Actively maintained
> **Documentation version**: Based on actual API documentation collation of three main versions