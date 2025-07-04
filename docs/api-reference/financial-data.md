# 财务数据API

基于社区维护版本的详细财务数据接口说明。

## 📊 财务数据表分类

| 数据表 | 说明 | 主要用途 |
|--------|------|----------|
| valuation | 估值数据 | 市值、市盈率、市净率等 |
| balance_statement | 资产负债表 | 资产、负债、股东权益 |
| income_statement | 利润表 | 收入、成本、利润 |
| cashflow_statement | 现金流量表 | 现金流入流出 |
| growth_ability | 成长能力 | 增长率指标 |
| profit_ability | 盈利能力 | 盈利相关指标 |
| eps | 每股指标 | 每股收益、净资产等 |
| operating_ability | 营运能力 | 周转率指标 |
| debt_paying_ability | 偿债能力 | 流动比率、负债率等 |

## 🔧 基本用法

### 通用接口
```python
get_fundamentals(security, table_name, fields=None, date=None, 
                start_year=None, end_year=None, report_types=None, 
                date_type=None, merge_type=None)
```

### 查询模式

#### 1. 按日期查询模式
```python
# 获取指定日期的财务数据
get_fundamentals('600570.SS', 'valuation', 'pb', '20180410')

# 获取多个字段
get_fundamentals(['600570.SS','000001.SZ'], 'valuation', 
                ['total_value', 'pe_dynamic', 'turnover_rate', 'pb'], 
                date='2018-04-24')
```

#### 2. 按年份查询模式
```python
# 获取年份范围内的季度数据
get_fundamentals('600570.SS', 'balance_statement', 'total_assets',
                start_year='2013', end_year='2015', report_types='1')
```

## 📈 估值数据 (valuation)

### 重要字段
| 字段名 | 类型 | 说明 | 注意事项 |
|--------|------|------|----------|
| total_value | str | A股总市值(元) | 固定返回 |
| pe_dynamic | str | 动态市盈率 | 自选返回 |
| pb | float64 | 市净率 | 自选返回 |
| turnover_rate | str | 换手率 | 带%字符串，需转换 |
| dividend_ratio | str | 滚动股息率 | 带%字符串，需转换 |

### 使用示例
```python
# 获取股票池估值数据
stocks = get_index_stocks('000906.XBHS')
valuation = get_fundamentals(stocks, 'valuation')

# 获取特定字段
pb_data = get_fundamentals(stocks, 'valuation', fields='pb', date='20180410')
```

## 💰 资产负债表 (balance_statement)

### 核心字段
| 字段名 | 说明 |
|--------|------|
| total_assets | 资产总计 |
| total_current_assets | 流动资产合计 |
| total_non_current_assets | 非流动资产合计 |
| total_current_liability | 流动负债合计 |
| total_shareholder_equity | 所有者权益合计 |

### 使用示例
```python
# 获取资产总计
assets = get_fundamentals('600570.SS', 'balance_statement', 
                         'total_assets', '20160628')
```

## 📊 利润表 (income_statement)

### 核心字段
| 字段名 | 说明 |
|--------|------|
| operating_revenue | 营业收入 |
| operating_cost | 营业成本 |
| operating_profit | 营业利润 |
| net_profit | 净利润 |
| np_parent_company_owners | 归属于母公司所有者的净利润 |

### 使用示例
```python
# 获取净利润数据
profit = get_fundamentals('600570.SS', 'income_statement', 
                         'net_profit', start_year='2013', 
                         end_year='2015', report_types='1')
```

## 💸 现金流量表 (cashflow_statement)

### 核心字段
| 字段名 | 说明 |
|--------|------|
| net_operate_cash_flow | 经营活动产生的现金流量净额 |
| net_invest_cash_flow | 投资活动产生的现金流量净额 |
| net_finance_cash_flow | 筹资活动产生的现金流量净额 |
| cash_equivalent_increase | 现金及现金等价物净增加额 |

## 📈 成长能力 (growth_ability)

### 核心字段
| 字段名 | 说明 |
|--------|------|
| operating_revenue_grow_rate | 营业收入同比增长（%） |
| np_parent_company_yoy | 归属母公司股东的净利润同比增长（%） |
| oper_profit_grow_rate | 营业利润同比增长（%） |
| net_operate_cash_flow_yoy | 经营活动现金流量净额同比增长（%） |

## 💹 盈利能力 (profit_ability)

### 核心字段
| 字段名 | 说明 |
|--------|------|
| roe | 净资产收益率%摊薄公布值（%） |
| roe_weighted | 净资产收益率%加权公布值（%） |
| roa | 总资产净利率（%） |
| net_profit_ratio | 销售净利率（%） |
| gross_income_ratio | 销售毛利率（%） |

## 💰 每股指标 (eps)

### 核心字段
| 字段名 | 说明 |
|--------|------|
| basic_eps | 基本每股收益（元/股） |
| eps_ttm | 每股收益_TTM（元/股） |
| naps | 每股净资产（元/股） |
| net_operate_cash_flow_ps | 每股经营活动现金流量净额（元/股） |

## 🔄 营运能力 (operating_ability)

### 核心字段
| 字段名 | 说明 |
|--------|------|
| inventory_turnover_rate | 存货周转率（次） |
| accounts_receivables_turnover_rate | 应收帐款周转率（次） |
| total_asset_turnover_rate | 总资产周转率（次） |
| current_assets_turnover_rate | 流动资产周转率（次） |

## 💳 偿债能力 (debt_paying_ability)

### 核心字段
| 字段名 | 说明 |
|--------|------|
| current_ratio | 流动比率 |
| quick_ratio | 速动比率 |
| debt_equity_ratio | 产权比率（%） |
| interest_cover | 利息保障倍数（倍） |

## ⚠️ 重要注意事项

### 数据类型处理
```python
# 换手率和股息率需要手动转换
turnover_rate = "20%"  # 原始数据
turnover_float = float(turnover_rate.replace('%', '')) / 100  # 转换为0.2
```

### 日期参数说明
- **不传date**: 回测中获取前一交易日数据，交易中获取当日数据
- **传入date**: 获取指定日期数据，非交易日在回测中返回NAN

### 查询限制
- valuation表不支持年份查询参数
- growth_ability、profit_ability、eps、operating_ability、debt_paying_ability表不支持merge_type参数

---

> **说明**: 此文档基于社区维护版本的财务数据接口，其他版本可能存在差异。
