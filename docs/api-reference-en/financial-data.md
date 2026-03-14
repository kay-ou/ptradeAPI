# Financial Data API

Detailed financial data interface documentation based on community-maintained version.

## 📊 Financial Data Table Classification

| Data Table | Description | Main Purpose |
|---|---|---|
| `valuation` | Valuation Data | Market cap, P/E ratio, P/B ratio, etc. |
| `balance_statement` | Balance Sheet | Assets, liabilities, shareholders' equity |
| `income_statement` | Income Statement | Revenue, costs, profits |
| `cashflow_statement` | Cash Flow Statement | Cash inflows and outflows |
| `growth_ability` | Growth Ability | Growth rate indicators |
| `profit_ability` | Profitability | Profit-related indicators |
| `eps` | Per Share Indicators | EPS, net assets, etc. |
| `operating_ability` | Operating Ability | Turnover rate indicators |
| `debt_paying_ability` | Debt Paying Ability | Current ratio, debt ratio, etc. |

## 🔧 Basic Usage

### General Interface
```python
get_fundamentals(security, table_name, fields=None, date=None, 
                start_year=None, end_year=None, report_types=None, 
                date_type=None, merge_type=None)
```

### Query Modes

#### 1. Query by Date Mode
This mode uses the announcement date as the reference time by default, returning the financial data corresponding to the input date.
```python
# Get financial data for specified date
get_fundamentals('600570.SS', 'valuation', 'pb', '20180410')

# Get multiple fields
get_fundamentals(['600570.SS','000001.SZ'], 'valuation', 
                ['total_value', 'pe_dynamic', 'turnover_rate', 'pb'], 
                date='2018-04-24')
```

#### 2. Query by Year Mode
This mode returns the financial data for the corresponding quarters within the input year range.
```python
# Get quarterly data within year range
get_fundamentals('600570.SS', 'balance_statement', 'total_assets',
                start_year='2013', end_year='2015', report_types='1')
```

---

## 📈 Valuation Data (valuation)

```python
get_fundamentals(security, 'valuation', fields=None, date=None)
```

### Usage Example
```python
# Get stock pool
stocks = get_index_stocks('000906.XBHS')
# Or specify stock pool
# stocks = ['600570.SS','000001.SZ']

# Get valuation data, returns previous trading day's data by default
# Returns current time's valuation data in research and trading
get_fundamentals(stocks, 'valuation')

# Get P/B ratio for stocks in the pool for the previous trading day before 2018-04-10
get_fundamentals(stocks, 'valuation', date = '20180410', fields = 'pb')

# Get multiple fields data for stocks in the pool for the previous trading day before 2018-04-24
get_fundamentals(stocks, 'valuation', date = '2018-04-24', fields = ['total_value', 'pe_dynamic', 'turnover_rate', 'pb'])
```

---

> 🔙 **Return**: [API Documentation Home](README.md)