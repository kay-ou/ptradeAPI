# 财务数据API

基于社区维护版本的详细财务数据接口说明。

## 📊 财务数据表分类

| 数据表 | 说明 | 主要用途 |
|---|---|---|
| `valuation` | 估值数据 | 市值、市盈率、市净率等 |
| `balance_statement` | 资产负债表 | 资产、负债、股东权益 |
| `income_statement` | 利润表 | 收入、成本、利润 |
| `cashflow_statement` | 现金流量表 | 现金流入流出 |
| `growth_ability` | 成长能力 | 增长率指标 |
| `profit_ability` | 盈利能力 | 盈利相关指标 |
| `eps` | 每股指标 | 每股收益、净资产等 |
| `operating_ability` | 营运能力 | 周转率指标 |
| `debt_paying_ability` | 偿债能力 | 流动比率、负债率等 |

## 🔧 基本用法

### 通用接口
```python
get_fundamentals(security, table_name, fields=None, date=None, 
                start_year=None, end_year=None, report_types=None, 
                date_type=None, merge_type=None)
```

### 查询模式

#### 1. 按日期查询模式
该模式默认以发布日期为参考时间，返回输入日期之前对应的财务数据。
```python
# 获取指定日期的财务数据
get_fundamentals('600570.SS', 'valuation', 'pb', '20180410')

# 获取多个字段
get_fundamentals(['600570.SS','000001.SZ'], 'valuation', 
                ['total_value', 'pe_dynamic', 'turnover_rate', 'pb'], 
                date='2018-04-24')
```

#### 2. 按年份查询模式
该模式返回输入年份范围内对应季度的财务数据。
```python
# 获取年份范围内的季度数据
get_fundamentals('600570.SS', 'balance_statement', 'total_assets',
                start_year='2013', end_year='2015', report_types='1')
```

---

## 📈 估值数据 (valuation)

```python
get_fundamentals(security, 'valuation', fields=None, date=None)
```

### 使用示例
```python
# 获取股票池
stocks = get_index_stocks('000906.XBHS')
# 或者指定股票池
# stocks = ['600570.SS','000001.SZ']

# 获取估值数据，默认返回前一交易日的数据
# 在研究和交易中返回当前时间的估值数据
get_fundamentals(stocks, 'valuation')

# 获取股票池中对应上市公司2018年04月10日前一交易日的市净率
get_fundamentals(stocks, 'valuation', date = '20180410', fields = 'pb')

# 获取股票池中对应上市公司2018年04月24日前一交易日的多个字段数据
get_fundamentals(stocks, 'valuation', date = '2018-04-24', fields = ['total_value', 'pe_dynamic', 'turnover_rate', 'pb'])
```

<details>
<summary>点击查看 valuation 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 | 属性 |
|---|---|---|---|
| `trading_day` | str | 交易日期 | 固定返回 |
| `total_value` | str | A股总市值(元) | 固定返回 |
| `secu_code` | str | 证券代码 | 固定返回 |
| `float_value` | str | A股流通市值(元) | 自选返回 |
| `naps` | numpy.float64 | 每股净资产/(元/股) | 自选返回 |
| `pcf` | str | 市现率 | 自选返回 |
| `secu_abbr` | str | 证券简称 | 自选返回 |
| `ps` | numpy.float64 | 市销率PS | 自选返回 |
| `ps_ttm` | numpy.float64 | 市销率PS(TTM) | 自选返回 |
| `pe_ttm` | numpy.float64 | 市盈率PE(TTM) | 自选返回 |
| `a_shares` | str | A股股本 | 自选返回 |
| `a_floats` | numpy.float64 | 可流通A股 | 自选返回 |
| `pe_dynamic` | str | 动态市盈率 | 自选返回 |
| `pe_static` | str | 静态市盈率 | 自选返回 |
| `b_floats` | str | 可流通B股 | 自选返回 |
| `b_shares` | numpy.float64 | B股股本 | 自选返回 |
| `h_shares` | numpy.float64 | H股股本 | 自选返回 |
| `total_shares` | int | 总股本 | 自选返回 |
| `turnover_rate` | str | 换手率 | 自选返回 |
| `dividend_ratio` | str | 滚动股息率 | 自选返回 |
| `pb` | numpy.float64 | 市净率 | 自选返回 |
| `roe` | numpy.float64 | 净资产收益率 | 自选返回 |

</details>

---

## 💰 资产负债表 (balance_statement)

```python
get_fundamentals(security, 'balance_statement', fields, date=None, start_year=None, end_year=None, report_types=None, date_type=None, merge_type=None)
```

### 使用示例
```python
# 按日期查询：获取回测日期前对应的资产总计数据
get_fundamentals('600570.SS', 'balance_statement', 'total_assets', '20160628')

# 按年份查询：获取恒生电子2013-2015年第一季度的资产总计
get_fundamentals('600570.SS', 'balance_statement', 'total_assets', start_year='2013', end_year='2015', report_types='1')
```

<details>
<summary>点击查看 balance_statement 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 |
|---|---|---|
| `secu_code` | str | 股票代码 |
| `secu_abbr` | str | 股票简称 |
| `company_type` | str | 公司类型 |
| `end_date` | str | 截止日期 |
| `publ_date` | str | 公告日期 |
| `total_assets` | numpy.float64 | 资产总计 |
| `total_liability` | numpy.float64 | 负债合计 |
| `total_liability_and_equity` | numpy.float64 | 负债和股东权益总计 |
| `settlement_provi` | numpy.float64 | 结算备付金 |
| `client_provi` | numpy.float64 | 客户备付金 |
| `deposit_in_interbank` | numpy.float64 | 存放同业款项 |
| `r_metal` | numpy.float64 | 贵金属 |
| `lend_capital` | numpy.float64 | 拆出资金 |
| `derivative_assets` | numpy.float64 | 衍生金融资产 |
| `bought_sellback_assets` | numpy.float64 | 买入返售金融资产 |
| `loan_and_advance` | numpy.float64 | 发放贷款和垫款 |
| `insurance_receivables` | numpy.float64 | 应收保费 |
| `receivable_subrogation_fee` | numpy.float64 | 应收代位追偿款 |
| `reinsurance_receivables` | numpy.float64 | 应收分保账款 |
| `receivable_unearned_r` | numpy.float64 | 应收分保未到期责任准备金 |
| `receivable_claims_r` | numpy.float64 | 应收分保未决赔款准备金 |
| `receivable_life_r` | numpy.float64 | 应收分保寿险责任准备金 |
| `receivable_lt_health_r` | numpy.float64 | 应收分保长期健康险责任准备金 |
| `insurer_impawn_loan` | numpy.float64 | 保户质押贷款 |
| `fixed_deposit` | numpy.float64 | 定期存款 |
| `refundable_capital_deposit` | numpy.float64 | 存出资本保证金 |
| `refundable_deposit` | numpy.float64 | 存出保证金 |
| `independence_account_assets` | numpy.float64 | 独立账户资产 |
| `other_assets` | numpy.float64 | 其他资产 |
| `borrowing_from_centralbank` | numpy.float64 | 向中央银行借款 |
| `deposit_of_interbank` | numpy.float64 | 同业及其他金融机构存放款项 |
| `borrowing_capital` | numpy.float64 | 拆入资金 |
| `derivative_liability` | numpy.float64 | 衍生金融负债 |
| `sold_buyback_secu_proceeds` | numpy.float64 | 卖出回购金融资产款 |
| `deposit` | numpy.float64 | 吸收存款 |
| `proxy_secu_proceeds` | numpy.float64 | 代理买卖证券款 |
| `sub_issue_secu_proceeds` | numpy.float64 | 代理承销证券款 |
| `deposits_received` | numpy.float64 | 存入保证金 |
| `advance_insurance` | numpy.float64 | 预收保费 |
| `commission_payable` | numpy.float64 | 应付手续费及佣金 |
| `reinsurance_payables` | numpy.float64 | 应付分保账款 |
| `compensation_payable` | numpy.float64 | 应付赔付款 |
| `policy_dividend_payable` | numpy.float64 | 应付保单红利 |
| `insurer_deposit_investment` | numpy.float64 | 保户储金及投资款 |
| `unearned_premium_reserve` | numpy.float64 | 未到期责任准备金 |
| `outstanding_claim_reserve` | numpy.float64 | 未决赔款准备金 |
| `life_insurance_reserve` | numpy.float64 | 寿险责任准备金 |
| `lt_health_insurance_lr` | numpy.float64 | 长期健康险责任准备金 |
| `independence_liability` | numpy.float64 | 独立账户负债 |
| `other_liability` | numpy.float64 | 其他负债 |
| `cash_equivalents` | numpy.float64 | 货币资金 |
| `client_deposit` | numpy.float64 | 客户资金存款 |
| `trading_assets` | numpy.float64 | 交易性金融资产 |
| `bill_receivable` | numpy.float64 | 应收票据 |
| `dividend_receivable` | numpy.float64 | 应收股利 |
| `interest_receivable` | numpy.float64 | 应收利息 |
| `account_receivable` | numpy.float64 | 应收账款 |
| `other_receivable` | numpy.float64 | 其他应收款 |
| `advance_payment` | numpy.float64 | 预付款项 |
| `inventories` | numpy.float64 | 存货 |
| `non_current_asset_in_one_year` | numpy.float64 | 一年内到期的非流动资产 |
| `other_current_assets` | numpy.float64 | 其他流动资产 |
| `total_current_assets` | numpy.float64 | 流动资产合计 |
| `shortterm_loan` | numpy.float64 | 短期借款 |
| `impawned_loan` | numpy.float64 | 质押借款 |
| `trading_liability` | numpy.float64 | 交易性金融负债 |
| `notes_payable` | numpy.float64 | 应付票据 |
| `accounts_payable` | numpy.float64 | 应付账款 |
| `advance_receipts` | numpy.float64 | 预收款项 |
| `salaries_payable` | numpy.float64 | 应付职工薪酬 |
| `dividend_payable` | numpy.float64 | 应付股利 |
| `taxs_payable` | numpy.float64 | 应交税费 |
| `interest_payable` | numpy.float64 | 应付利息 |
| `other_payable` | numpy.float64 | 其他应付款 |
| `non_current_liability_in_one_year` | numpy.float64 | 一年内到期的非流动负债 |
| `other_current_liability` | numpy.float64 | 其他流动负债 |
| `total_current_liability` | numpy.float64 | 流动负债合计 |
| `hold_for_sale_assets` | numpy.float64 | 可供出售金融资产 |
| `hold_to_maturity_investments` | numpy.float64 | 持有至到期投资 |
| `investment_property` | numpy.float64 | 投资性房地产 |
| `longterm_equity_invest` | numpy.float64 | 长期股权投资 |
| `longterm_receivable_account` | numpy.float64 | 长期应收款 |
| `fixed_assets` | numpy.float64 | 固定资产 |
| `construction_materials` | numpy.float64 | 工程物资 |
| `constru_in_process` | numpy.float64 | 在建工程 |
| `fixed_assets_liquidation` | numpy.float64 | 固定资产清理 |
| `biological_assets` | numpy.float64 | 生产性生物资产 |
| `oil_gas_assets` | numpy.float64 | 油气资产 |
| `intangible_assets` | numpy.float64 | 无形资产 |
| `seat_costs` | numpy.float64 | 交易席位费 |
| `development_expenditure` | numpy.float64 | 开发支出 |
| `good_will` | numpy.float64 | 商誉 |
| `long_deferred_expense` | numpy.float64 | 长期待摊费用 |
| `deferred_tax_assets` | numpy.float64 | 递延所得税资产 |
| `other_non_current_assets` | numpy.float64 | 其他非流动资产 |
| `total_non_current_assets` | numpy.float64 | 非流动资产合计 |
| `longterm_loan` | numpy.float64 | 长期借款 |
| `bonds_payable` | numpy.float64 | 应付债券 |
| `longterm_account_payable` | numpy.float64 | 长期应付款 |
| `long_salaries_pay` | numpy.float64 | 长期应付职工薪酬 |
| `specific_account_payable` | numpy.float64 | 专项应付款 |
| `estimate_liability` | numpy.float64 | 预计负债 |
| `deferred_tax_liability` | numpy.float64 | 递延所得税负债 |
| `long_defer_income` | numpy.float64 | 长期递延收益 |
| `other_non_current_liability` | numpy.float64 | 其他非流动负债 |
| `total_non_current_liability` | numpy.float64 | 非流动负债合计 |
| `paidin_capital` | numpy.float64 | 实收资本（或股本） |
| `other_equityinstruments` | numpy.float64 | 其他权益工具 |
| `capital_reserve_fund` | numpy.float64 | 资本公积 |
| `surplus_reserve_fund` | numpy.float64 | 盈余公积 |
| `retained_profit` | numpy.float64 | 未分配利润 |
| `treasury_stock` | numpy.float64 | 减：库存股 |
| `other_composite_income` | numpy.float64 | 其他综合收益 |
| `ordinary_risk_reserve_fund` | numpy.float64 | 一般风险准备 |
| `foreign_currency_report_conv_diff` | numpy.float64 | 外币报表折算差额 |
| `specific_reserves` | numpy.float64 | 专项储备 |
| `se_without_mi` | numpy.float64 | 归属母公司股东权益合计 |
| `minority_interests` | numpy.float64 | 少数股东权益 |
| `total_shareholder_equity` | numpy.float64 | 所有者权益合计 |

</details>

---

## 📊 利润表 (income_statement)

```python
get_fundamentals(security, 'income_statement', fields, date=None, start_year=None, end_year=None, report_types=None, date_type=None, merge_type=None)
```

### 使用示例
```python
# 按日期查询：获取回测日期前对应的净利润数据
get_fundamentals('600570.SS', 'income_statement', 'net_profit', '20160628')

# 按年份查询：获取恒生电子2013-2015年第一季度的净利润
get_fundamentals('600570.SS', 'income_statement', 'net_profit', start_year='2013', end_year='2015', report_types='1')
```

<details>
<summary>点击查看 income_statement 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 |
|---|---|---|
| `secu_code` | str | 股票代码 |
| `secu_abbr` | str | 股票简称 |
| `company_type` | str | 公司类型 |
| `end_date` | str | 截止日期 |
| `publ_date` | str | 公告日期 |
| `basic_eps` | numpy.float64 | 基本每股收益 |
| `diluted_eps` | numpy.float64 | 稀释每股收益 |
| `net_profit` | numpy.float64 | 净利润 |
| `np_parent_company_owners` | numpy.float64 | 归属于母公司所有者的净利润 |
| `minority_profit` | numpy.float64 | 少数股东损益 |
| `total_operating_cost` | numpy.float64 | 营业总成本 |
| `operating_payout` | numpy.float64 | 营业支出 |
| `refunded_premiums` | numpy.float64 | 退保金 |
| `compensation_expense` | numpy.float64 | 赔付支出 |
| `amortization_expense` | numpy.float64 | 减:摊回赔付支出 |
| `premium_reserve` | numpy.float64 | 提取保险责任准备金 |
| `amortization_premium_reserve` | numpy.float64 | 减:摊回保险责任准备金 |
| `policy_dividend_payout` | numpy.float64 | 保单红利支出 |
| `reinsurance_cost` | numpy.float64 | 分保费用 |
| `amortization_reinsurance_cost` | numpy.float64 | 减:摊回分保费用 |
| `insurance_commission_expense` | numpy.float64 | 保险手续费及佣金支出 |
| `other_operating_cost` | numpy.float64 | 其他营业成本 |
| `operating_cost` | numpy.float64 | 营业成本 |
| `operating_tax_surcharges` | numpy.float64 | 营业税金及附加 |
| `operating_expense` | numpy.float64 | 销售费用 |
| `administration_expense` | numpy.float64 | 管理费用 |
| `financial_expense` | numpy.float64 | 财务费用 |
| `asset_impairment_loss` | numpy.float64 | 资产减值损失 |
| `operating_profit` | numpy.float64 | 营业利润 |
| `non_operating_income` | numpy.float64 | 加：营业收入 |
| `non_operating_expense` | numpy.float64 | 减：营业外支出 |
| `non_current_assetss_deal_loss` | numpy.float64 | 其中：非流动资产处置净损失 |
| `total_operating_revenue` | numpy.float64 | 营业总收入 |
| `operating_revenue` | numpy.float64 | 营业收入 |
| `net_interest_income` | numpy.float64 | 利息净收入 |
| `interest_income` | numpy.float64 | 其中：利息收入 |
| `interest_expense` | numpy.float64 | 其中:利息支出 |
| `net_commission_income` | numpy.float64 | 手续费及佣金净收入 |
| `commission_income` | numpy.float64 | 其中：手续费及佣金收入 |
| `commission_expense` | numpy.float64 | 其中：手续费及佣金支出 |
| `net_proxy_secu_income` | numpy.float64 | 其中：代理买卖证券业务净收入 |
| `net_subissue_secu_income` | numpy.float64 | 其中：证券承销业务净收入 |
| `net_trust_income` | numpy.float64 | 其中:受托客户资产管理业务净收入 |
| `premiums_earned` | numpy.float64 | 已赚保费 |
| `premiums_income` | numpy.float64 | 保险业务收入 |
| `reinsurance_income` | numpy.float64 | 其中：分保费收入 |
| `reinsurance` | numpy.float64 | 减：分出保费 |
| `unearned_premium_reserve` | numpy.float64 | 提取未到期责任准备金 |
| `other_operating_revenue` | numpy.float64 | 其他营业收入 |
| `other_net_revenue` | numpy.float64 | 非营业性收入 |
| `fair_value_change_income` | numpy.float64 | 公允价值变动净收益 |
| `invest_income` | numpy.float64 | 投资净收益 |
| `invest_income_associates` | numpy.float64 | 其中:对联营合营企业的投资收益 |
| `exchange_income` | numpy.float64 | 汇兑收益 |
| `total_profit` | numpy.float64 | 利润总额 |
| `income_tax_cost` | numpy.float64 | 减：所得税费用 |
| `total_composite_income` | numpy.float64 | 综合收益总额 |
| `ci_parent_company_owners` | numpy.float64 | 归属于母公司所有者的综合收益总额 |
| `ci_minority_owners` | numpy.float64 | 归属于少数股东的综合收益总额 |

</details>

---

## 💸 现金流量表 (cashflow_statement)

```python
get_fundamentals(security, 'cashflow_statement', fields, date=None, start_year=None, end_year=None, report_types=None, date_type=None, merge_type=None)
```

### 使用示例
```python
# 按日期查询：获取回测日期前对应的投资支付现金数据
get_fundamentals('600570.SS', 'cashflow_statement', 'invest_cash_paid', '20160628')

# 按年份查询：获取恒生电子2013-2015年第一季度的投资支付现金数据
get_fundamentals('600570.SS', 'cashflow_statement', 'invest_cash_paid', start_year='2013', end_year='2015', report_types='1')
```

<details>
<summary>点击查看 cashflow_statement 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 |
|---|---|---|
| `secu_code` | str | 股票代码 |
| `secu_abbr` | str | 股票简称 |
| `company_type` | str | 公司类型 |
| `end_date` | str | 截止日期 |
| `publ_date` | str | 公告日期 |
| `goods_sale_service_render_cash` | numpy.float64 | 销售商品、提供劳务收到的现金 |
| `tax_levy_refund` | numpy.float64 | 收到的税费返还 |
| `net_deposit_increase` | numpy.float64 | 客户存款和同业存放款项净增加额 |
| `net_borrowing_from_central_bank` | numpy.float64 | 向中央银行借款净增加额 |
| `net_borrowing_from_finance_co` | numpy.float64 | 向其他金融机构拆入资金净增加额 |
| `interest_and_commission_cashin` | numpy.float64 | 收取利息、手续费及佣金的现金 |
| `net_deal_trading_assets` | numpy.float64 | 处置交易性金融资产净增加额 |
| `net_buyback` | numpy.float64 | 回购业务资金净增加额 |
| `net_original_insurance_cash` | numpy.float64 | 收到原保险合同保费取得的现金 |
| `net_reinsurance_cash` | numpy.float64 | 收到再保业务现金净额 |
| `net_insurer_deposit_investment` | numpy.float64 | 保户储金及投资款净增加额 |
| `other_cashin_related_operate` | numpy.float64 | 收到其他与经营活动有关的现金 |
| `subtotal_operate_cash_inflow` | numpy.float64 | 经营活动现金流入小计 |
| `goods_and_services_cash_paid` | numpy.float64 | 购买商品、接受劳务支付的现金 |
| `staff_behalf_paid` | numpy.float64 | 支付给职工以及为职工支付的现金 |
| `all_taxes_paid` | numpy.float64 | 支付的各项税费 |
| `net_loan_and_advance_increase` | numpy.float64 | 客户贷款及垫款净增加额 |
| `net_deposit_in_cb_and_ib` | numpy.float64 | 存放中央银行和同业款项净增加额 |
| `net_lend_capital` | numpy.float64 | 拆出资金净增加额 |
| `commission_cash_paid` | numpy.float64 | 支付手续费及佣金的现金 |
| `original_compensation_paid` | numpy.float64 | 支付原保险合同赔付款项的现金 |
| `net_cash_for_reinsurance` | numpy.float64 | 支付再保业务现金净额 |
| `policy_dividend_cash_paid` | numpy.float64 | 支付保单红利的现金 |
| `other_operate_cash_paid` | numpy.float64 | 支付其他与经营活动有关的现金 |
| `subtotal_operate_cash_outflow` | numpy.float64 | 经营活动现金流出小计 |
| `net_operate_cash_flow` | numpy.float64 | 经营活动产生的现金流量净额 |
| `invest_withdrawal_cash` | numpy.float64 | 收回投资收到的现金 |
| `invest_proceeds` | numpy.float64 | 取得投资收益收到的现金 |
| `fix_intan_other_asset_dispo_cash` | numpy.float64 | 处置固定资产、无形资产和其他长期资产收回的现金净额 |
| `net_cash_deal_sub_company` | numpy.float64 | 处置子公司及其他营业单位收到的现金净额 |
| `other_cash_from_invest_act` | numpy.float64 | 收到其他与投资活动有关的现金 |
| `subtotal_invest_cash_inflow` | numpy.float64 | 投资活动现金流入小计 |
| `fix_intan_other_asset_acqui_cash` | numpy.float64 | 购建固定资产、无形资产和其他长期资产支付的现金 |
| `invest_cash_paid` | numpy.float64 | 投资支付的现金 |
| `net_cash_from_sub_company` | numpy.float64 | 取得子公司及其他营业单位支付的现金净额 |
| `impawned_loan_net_increase` | numpy.float64 | 质押贷款净增加额 |
| `other_cash_to_invest_act` | numpy.float64 | 支付其他与投资活动有关的现金 |
| `subtotal_invest_cash_outflow` | numpy.float64 | 投资活动现金流出小计 |
| `net_invest_cash_flow` | numpy.float64 | 投资活动产生的现金流量净额 |
| `cash_from_invest` | numpy.float64 | 吸收投资收到的现金 |
| `cash_from_bonds_issue` | numpy.float64 | 发行债券收到的现金 |
| `cash_from_borrowing` | numpy.float64 | 取得借款收到的现金 |
| `other_finance_act_cash` | numpy.float64 | 收到其他与筹资活动有关的现金 |
| `subtotal_finance_cash_inflow` | numpy.float64 | 筹资活动现金流入小计 |
| `borrowing_repayment` | numpy.float64 | 偿还债务支付的现金 |
| `dividend_interest_payment` | numpy.float64 | 分配股利、利润或偿付利息支付的现金 |
| `other_finance_act_payment` | numpy.float64 | 支付其他与筹资活动有关的现金 |
| `subtotal_finance_cash_outflow` | numpy.float64 | 筹资活动现金流出小计 |
| `net_finance_cash_flow` | numpy.float64 | 筹资活动产生的现金流量净额 |
| `exchan_rate_change_effect` | numpy.float64 | 汇率变动对现金及现金等价物的影响 |
| `cash_equivalent_increase` | numpy.float64 | 现金及现金等价物净增加额 |
| `begin_period_cash` | numpy.float64 | 加：期初现金及现金等价物余额 |
| `end_period_cash_equivalent` | numpy.float64 | 期末现金及现金等价物余额 |
| `net_profit` | numpy.float64 | 净利润 |
| `minority_profit` | numpy.float64 | 加:少数股东损益 |
| `assets_depreciation_reserves` | numpy.float64 | 加:资产减值准备 |
| `fixed_asset_depreciation` | numpy.float64 | 固定资产折旧 |
| `intangible_asset_amortization` | numpy.float64 | 收无形资产摊销 |
| `deferred_expense_amort` | numpy.float64 | 长期待摊费用摊销 |
| `deferred_expense_decreased` | numpy.float64 | 待摊费用减少(减:增加) |
| `accrued_expense_added` | numpy.float64 | 预提费用增加(减:减少) |
| `fix_intanther_asset_dispo_loss` | numpy.float64 | 处置固定资产、无形资产和其他长期资产的损失 |
| `fixed_asset_scrap_loss` | numpy.float64 | 固定资产报废损失 |
| `loss_from_fair_value_changes` | numpy.float64 | 公允价值变动损失 |
| `financial_expense` | numpy.float64 | 财务费用 |
| `invest_loss` | numpy.float64 | 投资损失 |
| `defered_tax_asset_decrease` | numpy.float64 | 递延所得税资产减少 |
| `defered_tax_liability_increase` | numpy.float64 | 递延所得税负债增加 |
| `inventory_decrease` | numpy.float64 | 存货的减少 |
| `operate_receivable_decrease` | numpy.float64 | 经营性应收项目的减少 |
| `operate_payable_increase` | numpy.float64 | 经营性应付项目的增加 |
| `others` | numpy.float64 | 其他 |
| `net_operate_cash_flow_notes` | numpy.float64 | 经营活动产生的现金流量净额 |
| `debt_to_captical` | numpy.float64 | 债务转为资本 |
| `cbs_expiring_within_one_year` | numpy.float64 | 一年内到期的可转换公司债券 |
| `fixed_assets_finance_leases` | numpy.float64 | 融资租入固定资产 |
| `cash_at_end_of_year` | numpy.float64 | 现金的期末余额 |
| `cash_at_beginning_of_year` | numpy.float64 | 减:现金的期初余额 |
| `cash_equivalents_at_end_of_year` | numpy.float64 | 加:现金等价物的期末余额 |
| `cash_equivalents_at_beginning` | numpy.float64 | 减:现金等价物的期初余额 |
| `net_incr_in_cash_and_equivalents` | numpy.float64 | 现金及现金等价物净增加额 |

</details>

---

## 📈 成长能力 (growth_ability)

```python
get_fundamentals(security, 'growth_ability', fields, date=None, start_year=None, end_year=None, report_types=None, date_type=None)
```

### 使用示例
```python
# 按日期查询：获取回测日期前对应的营业利润同比增长率
get_fundamentals('600570.SS', 'growth_ability', 'oper_profit_grow_rate', '20160628')

# 按年份查询：获取恒生电子2013-2015年第一季度的营业利润同比增长率
get_fundamentals('600570.SS', 'growth_ability', 'oper_profit_grow_rate', start_year='2013', end_year='2015', report_types='1')
```

<details>
<summary>点击查看 growth_ability 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 | 属性 |
|---|---|---|---|
| `secu_code` | str | 股票代码 | 固定返回 |
| `secu_abbr` | str | 股票简称 | 固定返回 |
| `publ_date` | str | 公告日期 | 固定返回 |
| `end_date` | str | 截止日期 | 固定返回 |
| `basic_eps_yoy` | numpy.float64 | 基本每股收益同比增长（%） | 自选返回 |
| `diluted_eps_yoy` | numpy.float64 | 稀释每股收益同比增长（%） | 自选返回 |
| `operating_revenue_grow_rate` | numpy.float64 | 营业收入同比增长（%） | 自选返回 |
| `np_parent_company_yoy` | numpy.float64 | 归属母公司股东的净利润同比增长（%） | 自选返回 |
| `net_operate_cash_flow_yoy` | numpy.float64 | 经营活动产生的现金流量净额同比增长（%） | 自选返回 |
| `oper_profit_grow_rate` | numpy.float64 | 营业利润同比增长（%） | 自选返回 |
| `total_profit_grow_rate` | numpy.float64 | 利润总额同比增长（%） | 自选返回 |
| `eps_grow_rate_ytd` | numpy.float64 | 每股净资产相对年初增长率（%） | 自选返回 |
| `se_without_mi_grow_rate_ytd` | numpy.float64 | 归属母公司股东的权益相对年初增长率（%） | 自选返回 |
| `ta_grow_rate_ytd` | numpy.float64 | 资产总计相对年初增长率（%) | 自选返回 |
| `np_parent_company_cut_yoy` | numpy.float64 | 归属母公司股东的净利润(扣除)同比增长（%） | 自选返回 |
| `avg_np_yoy_past_five_year` | numpy.float64 | 过去五年同期归属母公司净利润平均增幅（%） | 自选返回 |
| `oper_cash_ps_grow_rate` | numpy.float64 | 每股经营活动产生的现金流量净额同比增长（%） | 自选返回 |
| `naor_yoy` | numpy.float64 | 净资产收益率(摊薄)同比增（%） | 自选返回 |
| `net_asset_grow_rate` | numpy.float64 | 净资产同比增长（%） | 自选返回 |
| `total_asset_grow_rate` | numpy.float64 | 总资产同比增长（%） | 自选返回 |
| `sustainable_grow_rate` | numpy.float64 | 可持续增长率（%） | 自选返回 |
| `net_profit_grow_rate` | numpy.float64 | 净利润同比增长（%） | 自选返回 |

</details>

---

## 💹 盈利能力 (profit_ability)

```python
get_fundamentals(security, 'profit_ability', fields, date=None, start_year=None, end_year=None, report_types=None, date_type=None)
```

### 使用示例
```python
# 按日期查询：获取回测日期前对应的净资产收益率
get_fundamentals('600570.SS', 'profit_ability', 'roe', '20160628')

# 按年份查询：获取恒生电子2013-2015年第一季度的净资产收益率
get_fundamentals('600570.SS', 'profit_ability', 'roe', start_year='2013', end_year='2015', report_types='1')
```

<details>
<summary>点击查看 profit_ability 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 | 属性 |
|---|---|---|---|
| `secu_code` | str | 股票代码 | 固定返回 |
| `secu_abbr` | str | 股票简称 | 固定返回 |
| `publ_date` | str | 公告日期 | 固定返回 |
| `end_date` | str | 截止日期 | 固定返回 |
| `roe_avg` | numpy.float64 | 净资产收益率%平均计算值（%） | 自选返回 |
| `roe_weighted` | numpy.float64 | 净资产收益率%加权公布值（%） | 自选返回 |
| `roe` | numpy.float64 | 净资产收益率%摊薄公布值（%） | 自选返回 |
| `roe_cut` | numpy.float64 | 净资产收益率%扣除摊薄（%） | 自选返回 |
| `roe_cut_weighted` | numpy.float64 | 净资产收益率%扣除加权（%） | 自选返回 |
| `roe_ttm` | numpy.float64 | 净资产收益率_TTM（%） | 自选返回 |
| `roa_ebit` | numpy.float64 | 总资产报酬率（%） | 自选返回 |
| `roa_ebit_ttm` | numpy.float64 | 总资产报酬率_TTM（%） | 自选返回 |
| `roa` | numpy.float64 | 总资产净利率（%） | 自选返回 |
| `roa_ttm` | numpy.float64 | 总资产净利率_TTM（%） | 自选返回 |
| `roic` | numpy.float64 | 投入资本回报率（%） | 自选返回 |
| `net_profit_ratio` | numpy.float64 | 销售净利率（%） | 自选返回 |
| `net_profit_ratio_ttm` | numpy.float64 | 销售净利率_TTM（%） | 自选返回 |
| `gross_income_ratio` | numpy.float64 | 销售毛利率（%） | 自选返回 |
| `gross_income_ratio_ttm` | numpy.float64 | 销售毛利率_TTM（%） | 自选返回 |
| `sales_cost_ratio` | numpy.float64 | 销售成本率（%） | 自选返回 |
| `period_costs_rate` | numpy.float64 | 销售期间费用率（%） | 自选返回 |
| `period_costs_rate_ttm` | numpy.float64 | 销售期间费用率_TTM（%） | 自选返回 |
| `np_to_tor` | numpy.float64 | 净利润／营业总收入（%） | 自选返回 |
| `np_to_tor_ttm` | numpy.float64 | 净利润／营业总收入_TTM（%） | 自选返回 |
| `operating_profit_to_tor` | numpy.float64 | 营业利润／营业总收入（%） | 自选返回 |
| `operating_profit_to_tor_ttm` | numpy.float64 | 营业利润／营业总收入_TTM（%） | 自选返回 |
| `ebit_to_tor` | numpy.float64 | 息税前利润／营业总收入（%） | 自选返回 |
| `ebit_to_tor_ttm` | numpy.float64 | 息税前利润／营业总收入_TTM（%） | 自选返回 |
| `t_operating_cost_to_tor` | numpy.float64 | 营业总成本／营业总收入（%） | 自选返回 |
| `t_operating_cost_to_tor_ttm` | numpy.float64 | 营业总成本／营业总收入_TTM（%） | 自选返回 |
| `operating_expense_rate` | numpy.float64 | 销售费用／营业总收入（%） | 自选返回 |
| `operating_expense_rate_ttm` | numpy.float64 | 销售费用／营业总收入_TTM（%） | 自选返回 |
| `admini_expense_rate` | numpy.float64 | 管理费用／营业总收入（%） | 自选返回 |
| `admini_expense_rate_ttm` | numpy.float64 | 管理费用／营业总收入_TTM（%） | 自选返回 |
| `financial_expense_rate` | numpy.float64 | 财务费用／营业总收入（%） | 自选返回 |
| `financial_expense_rate_ttm` | numpy.float64 | 财务费用／营业总收入_TTM（%） | 自选返回 |
| `asset_impa_loss_to_tor` | numpy.float64 | 资产减值损失／营业总收入（%） | 自选返回 |
| `asset_impa_loss_to_tor_ttm` | numpy.float64 | 资产减值损失／营业总收入_TTM（%） | 自选返回 |
| `net_profit` | numpy.float64 | 归属母公司净利润（元） | 自选返回 |
| `net_profit_cut` | numpy.float64 | 扣除非经常性损益后的净利润（元） | 自选返回 |
| `ebit` | numpy.float64 | 息税前利润（元） | 自选返回 |
| `ebitda` | numpy.float64 | 息税折旧摊销前利润（元） | 自选返回 |
| `operating_profit_ratio` | numpy.float64 | 营业利润率（%） | 自选返回 |
| `total_profit_cost_ratio` | numpy.float64 | 成本费用利润率 | 自选返回 |

</details>

---

## 💰 每股指标 (eps)

```python
get_fundamentals(security, 'eps', fields, date=None, start_year=None, end_year=None, report_types=None, date_type=None)
```

### 使用示例
```python
# 按日期查询：获取回测日期前对应的基本每股收益
get_fundamentals('600570.SS', 'eps', 'basic_eps', '20160628')

# 按年份查询：获取恒生电子2013-2015年第一季度的基本每股收益
get_fundamentals('600570.SS', 'eps', 'basic_eps', start_year='2013', end_year='2015', report_types='1')
```

<details>
<summary>点击查看 eps 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 | 属性 |
|---|---|---|---|
| `secu_code` | str | 股票代码 | 固定返回 |
| `secu_abbr` | str | 股票简称 | 固定返回 |
| `publ_date` | str | 公告日期 | 固定返回 |
| `end_date` | str | 截止日期 | 固定返回 |
| `basic_eps` | numpy.float64 | 基本每股收益（元/股） | 自选返回 |
| `diluted_eps` | numpy.float64 | 稀释每股收益（元/股） | 自选返回 |
| `eps` | numpy.float64 | 每股收益_期末股本摊薄（元/股） | 自选返回 |
| `eps_ttm` | numpy.float64 | 每股收益_TTM（元/股） | 自选返回 |
| `naps` | numpy.float64 | 每股净资产（元/股） | 自选返回 |
| `total_operating_revenue_ps` | numpy.float64 | 每股营业总收入（元/股） | 自选返回 |
| `main_income_ps` | numpy.float64 | 每股营业收入（元/股） | 自选返回 |
| `operating_revenue_ps_ttm` | numpy.float64 | 每股营业收入_TTM（元/股） | 自选返回 |
| `oper_profit_ps` | numpy.float64 | 每股营业利润（元/股） | 自选返回 |
| `ebitps` | numpy.float64 | 每股息税前利润（元/股） | 自选返回 |
| `capital_surplus_fund_ps` | numpy.float64 | 每股资本公积金（元/股） | 自选返回 |
| `surplus_reserve_fund_ps` | numpy.float64 | 每股盈余公积（元/股） | 自选返回 |
| `accumulation_fund_ps` | numpy.float64 | 每股公积金（元/股） | 自选返回 |
| `undivided_profit` | numpy.float64 | 每股未分配利润（元/股） | 自选返回 |
| `retained_earnings_ps` | numpy.float64 | 每股留存收益（元/股） | 自选返回 |
| `net_operate_cash_flow_ps` | numpy.float64 | 每股经营活动产生的现金流量净额（元/股） | 自选返回 |
| `net_operate_cash_flow_ps_ttm` | numpy.float64 | 每股经营活动产生的现金流量净额_TTM（元/股） | 自选返回 |
| `cash_flow_ps` | numpy.float64 | 每股现金流量净额（元/股） | 自选返回 |
| `cash_flow_ps_ttm` | numpy.float64 | 每股现金流量净额_TTM（元/股） | 自选返回 |
| `enterprise_fcf_ps` | numpy.float64 | 每股企业自由现金流量（元/股） | 自选返回 |
| `shareholder_fcf_ps` | numpy.float64 | 每股股东自由现金流量（元/股） | 自选返回 |

</details>

---

## 🔄 营运能力 (operating_ability)

```python
get_fundamentals(security, 'operating_ability', fields, date=None, start_year=None, end_year=None, report_types=None, date_type=None)
```

### 使用示例
```python
# 按日期查询：获取回测日期前对应的流动资产周转率
get_fundamentals('600570.SS', 'operating_ability', 'current_assets_turnover_rate', '20160628')

# 按年份查询：获取恒生电子2013-2015年第一季度的流动资产周转率
get_fundamentals('600570.SS', 'operating_ability', 'current_assets_turnover_rate', start_year='2013', end_year='2015', report_types='1')
```

<details>
<summary>点击查看 operating_ability 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 | 属性 |
|---|---|---|---|
| `secu_code` | str | 股票代码 | 固定返回 |
| `secu_abbr` | str | 股票简称 | 固定返回 |
| `publ_date` | str | 公告日期 | 固定返回 |
| `end_date` | str | 截止日期 | 固定返回 |
| `oper_cycle` | numpy.float64 | 营业周期（天/次） | 自选返回 |
| `inventory_turnover_rate` | numpy.float64 | 存货周转率（次） | 自选返回 |
| `inventory_turnover_days` | numpy.float64 | 存货周转天数（天/次） | 自选返回 |
| `accounts_receivables_turnover_rate` | numpy.float64 | 应收帐款周转率（次） | 自选返回 |
| `accounts_receivables_turnover_days` | numpy.float64 | 应收帐款周转天数（天/次） | 自选返回 |
| `accounts_payables_turnover_rate` | numpy.float64 | 应付帐款周转率（次） | 自选返回 |
| `accounts_payables_turnover_days` | numpy.float64 | 应付帐款周转天数（天/次） | 自选返回 |
| `current_assets_turnover_rate` | numpy.float64 | 流动资产周转率（次） | 自选返回 |
| `fixed_asset_turnover_rate` | numpy.float64 | 固定资产周转率（次） | 自选返回 |
| `equity_turnover_rate` | numpy.float64 | 股东权益周转率（次） | 自选返回 |
| `total_asset_turnover_rate` | numpy.float64 | 总资产周转率（次） | 自选返回 |

</details>

---

## 💳 偿债能力 (debt_paying_ability)

```python
get_fundamentals(security, 'debt_paying_ability', fields, date=None, start_year=None, end_year=None, report_types=None, date_type=None)
```

### 使用示例```python
# 按日期查询：获取回测日期前对应的流动比率
get_fundamentals('600570.SS', 'debt_paying_ability', 'current_ratio', '20160628')

# 按年份查询：获取恒生电子2013-2015年第一季度的流动比率
get_fundamentals('600570.SS', 'debt_paying_ability', 'current_ratio', start_year='2013', end_year='2015', report_types='1')
```

<details>
<summary>点击查看 debt_paying_ability 完整字段列表</summary>

| 字段名称 | 字段类型 | 字段说明 | 属性 |
|---|---|---|---|
| `secu_code` | str | 股票代码 | 固定返回 |
| `secu_abbr` | str | 股票简称 | 固定返回 |
| `publ_date` | str | 公告日期 | 固定返回 |
| `end_date` | str | 截止日期 | 固定返回 |
| `current_ratio` | numpy.float64 | 流动比率 | 自选返回 |
| `quick_ratio` | numpy.float64 | 速动比率 | 自选返回 |
| `super_quick_ratio` | numpy.float64 | 超速动比率 | 自选返回 |
| `debt_equity_ratio` | numpy.float64 | 产权比率（%） | 自选返回 |
| `sewmi_to_total_liability` | numpy.float64 | 归属母公司股东的权益／负债合计（%） | 自选返回 |
| `sewmi_to_interest_bear_debt` | numpy.float64 | 归属母公司股东的权益／带息债务（%） | 自选返回 |
| `debt_tangible_equity_ratio` | numpy.float64 | 有形净值债务率（%） | 自选返回 |
| `tangible_a_to_interest_bear_debt` | numpy.float64 | 有形净值／带息债务（%） | 自选返回 |
| `tangible_a_to_net_debt` | numpy.float64 | 有形净值／净债务（%） | 自选返回 |
| `ebitda_to_t_liability` | numpy.float64 | 息税折旧摊销前利润／负债合计 | 自选返回 |
| `nocf_to_t_liability` | numpy.float64 | 经营活动产生现金流量净额/负债合计 | 自选返回 |
| `nocf_to_interest_bear_debt` | numpy.float64 | 经营活动产生现金流量净额/带息债务 | 自选返回 |
| `nocf_to_current_liability` | numpy.float64 | 经营活动产生现金流量净额/流动负债 | 自选返回 |
| `nocf_to_net_debt` | numpy.float64 | 经营活动产生现金流量净额/净债务 | 自选返回 |
| `interest_cover` | numpy.float64 | 利息保障倍数（倍） | 自选返回 |
| `long_debt_to_working_capital` | numpy.float64 | 长期负债与营运资金比率 | 自选返回 |
| `opercashinto_current_debt` | numpy.float64 | 现金流动负债比 | 自选返回 |

</details>

---

## ⚠️ 重要注意事项

### 数据类型处理
换手率 (`turnover_rate`) 和滚动股息率 (`dividend_ratio`) 两个字段返回的是带 `%` 的字符串，需要手动转换为浮点数。
```python
# 示例：将 "20%" 转换为 0.2
turnover_rate_str = "20%"
turnover_rate_float = float(turnover_rate_str.replace('%', '')) / 100
```

### `date` 参数说明
- **不传入 `date`**: 
  - **回测中**: 默认获取 `context.blotter.current_dt` 前一交易日收盘后更新的数据，以避免未来函数。
  - **研究/交易中**: 返回当日数据。如果在盘中查询，可能因数据未更新而返回 `NaN`。建议传入前一个交易日以获取最新稳定数据。
- **传入 `date`**:
  - **回测/交易中**: 如果 `date` 为非交易日，将返回 `NaN`。
  - **研究中**: 如果 `date` 为非交易日，将返回往前最近一个交易日的数据。
  - **注意**: 在回测和交易中，可以获取到未来的数据，使用时需注意规避。

### 查询限制
- `valuation` 表不支持按年份查询 (`start_year`, `end_year` 等参数无效)。
- `growth_ability`, `profit_ability`, `eps`, `operating_ability`, `debt_paying_ability` 表不支持 `merge_type` 参数。

---

> **说明**: 此文档基于 Ptrade 财务数据接口（东莞/国盛版本）进行整理，不同数据源或版本可能存在差异。
