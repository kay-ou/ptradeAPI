# Ptrade API Reference Documentation

Welcome to the complete Ptrade API reference documentation. This documentation covers all API interfaces of the Ptrade quantitative trading platform, organized by functional modules.

## 📋 Documentation Navigation

### 🏗️ Core Framework
- [**Framework Basics**](framework.md) - Strategy framework, lifecycle, event handling
- [**Data Objects**](objects.md) - Core object definitions like Order, Position, Security
- [**Utility Functions**](utilities.md) - Logging, time, data conversion and other auxiliary tools

### 📈 Trading Interfaces
- [**Stock Trading**](stock-trading.md) - Spot trading interfaces for stocks, ETFs, convertible bonds
- [**Futures Trading**](futures.md) - Futures contract trading, position management interfaces
- [**Options Trading**](options.md) - Options contract trading, exercise interfaces
- [**Margin Trading**](margin-trading.md) - Margin buying, short selling, collateral management

### 📊 Data Interfaces
- [**Market Data**](market-data.md) - K-line, real-time quotes, Level 2 data acquisition
- [**Stock Information**](stock-info.md) - Stock basic information, financial data query
- [**Financial Data**](financial-data.md) - Financial statements, financial indicators data
- [**Basic Information**](basic-info.md) - Trading calendar, stock list and other basic data

### 🔧 Analysis Tools
- [**Technical Indicators**](technical-indicators.md) - Technical indicator calculations like MACD, KDJ, RSI
- [**System Settings**](settings.md) - Parameter configuration, notification settings, system management

## 🚀 Quick Search

### By Usage Frequency
| High Frequency | Medium Frequency | Low Frequency |
|---------------|-----------------|---------------|
| [Order Trading](stock-trading.md#basic-order-functions) | [Futures Trading](futures.md) | [System Settings](settings.md) |
| [Market Data](market-data.md#historical-data) | [Options Trading](options.md) | [Financial Data](financial-data.md) |
| [Position Query](stock-trading.md#position-query) | [Margin Trading](margin-trading.md) | [Basic Information](basic-info.md) |
| [Technical Indicators](technical-indicators.md) | [Stock Information](stock-info.md) | [Utility Functions](utilities.md) |

### By Trading Type
- **Spot Trading**: [Stock Trading](stock-trading.md) → [Market Data](market-data.md) → [Technical Indicators](technical-indicators.md)
- **Derivatives Trading**: [Futures Trading](futures.md) / [Options Trading](options.md) → [Market Data](market-data.md)
- **Credit Trading**: [Margin Trading](margin-trading.md) → [Stock Trading](stock-trading.md)

### By Development Phase
- **Strategy Development**: [Framework Basics](framework.md) → [Data Objects](objects.md) → [Utility Functions](utilities.md)
- **Data Acquisition**: [Market Data](market-data.md) → [Stock Information](stock-info.md) → [Financial Data](financial-data.md)
- **Trading Execution**: [Stock Trading](stock-trading.md) → [Futures Trading](futures.md) → [Options Trading](options.md)
- **System Configuration**: [System Settings](settings.md) → [Basic Information](basic-info.md)

## 📖 Version Notes

This API documentation is based on three main versions:
- **Dongguan Securities version** (V041) - Most complete, includes latest features
- **Guosheng Securities version** (V016) - Stable standard version
- **Community-maintained version** (V005) - Community-enhanced version

> 💡 **Tip**: There are interface differences between different versions, see [Version Differences Comparison](../version-differences.md)

## 🔗 Related Documentation

- [**API Classification Index**](../api-classification.md) - Complete API list by function category
- [**Strategy Examples**](../examples.md) - Practical use cases and best practices
- [**Version Comparison**](../versions/) - Detailed version feature comparison
- [**Frequently Asked Questions**](../advanced/faq.md) - Common questions during development

## 📝 Usage Suggestions

1. **New users**: Start with [Framework Basics](framework.md) to understand the overall architecture
2. **Experienced users**: Directly view specific trading or data interface documentation
3. **Version migration**: Refer to [Version Differences Comparison](../version-differences.md) for compatibility information

---

> 📚 **Documentation Maintenance**: This documentation is continuously updated. If you find errors or need additions, please submit an Issue or PR