恒生投研平台

* [首页](/start)
* [研究](/home)
* [策略](/strategys)
* [交易](/trades)
* [数据](/data)
* [帮助](/help/api)

- [财务数据的API接口说明](#财务数据的API接口说明)
- [valuation](#valuation)
- [balance\_statement](#balance_statement)
- [income\_statement](#income_statement)
- [cashflow\_statement](#cashflow_statement)
- [growth\_ability](#growth_ability)
- [profit\_ability](#profit_ability)
- [eps](#eps)
- [operating\_ability](#operating_ability)
- [debt\_paying\_ability](#debt_paying_ability)

# 财务数据的API接口说明

## valuation-估值数据

```python
get_fundamentals(security, 'valuation', fields=None, date=None)
```

注意事项：

一、该接口只支持按天查询模式，返回查询日期对应股票相关数据。查询此表不支持输入的参数有：start\_year, end\_year, report\_types, date\_type, merge\_type。

二、换手率（turnover\_rate）和滚动股息率（dividend\_ratio）两个字段数据源返回的是带%的字符串。比如turnover\_rate：20%，用户需要自行转换成0.2的float格式。

关于date字段的说明

场景一：date字段不入参。回测中默认是获取context.blotter.current\_dt交易日收盘后更新的数据，因此会产生未来函数，交易和研究会返回当日数据，若在盘中时间由于数据未更新将返回字段为NAN的数据，因此建议获取最新数据的场景都使用date参数入参上一个交易日日期。

场景二：date字段入参日期。回测和交易中若date为非交易日，将返回字段为NAN的数据；研究中若date为非交易日，将返回往前最近一个交易日的数据，注意回测和交易中是可以取到未来的数据，需要规避。

```python

               turnover_rate     pb    total_value   trading_day    pe_dynamic
secu_code
600570.SS         4.20%        11.89   3.748224e+10   2018-04-24      163.38
000001.SZ         0.86%         0.91   2.036411e+11   2018-04-24        7.72
```

### 示例

```python
# 获取股票池
stocks = get_index_stocks('000906.XBHS')
# 指定股票池
stocks = ['600570.SS','000001.SZ']

# 获取估值数据，默认会返回context.blotter.current_dt前一交易日的数据(在实际生活中，我们只能看到前一交易日的估值数据)。仅在回测中返回前一交易日的估值数据，在研究和交易中返回当前时间的估值数据。
get_fundamentals(stocks, 'valuation')

#获取股票池中对应上市公司2018年04月10日前一交易日的市净率
get_fundamentals(stocks, 'valuation', date = '20180410', fields = 'pb')

# 获取股票池中对应上市公司2018年04月24日前一交易日的A股总市值(元)、动态市盈率、换手率和市净率数据
get_fundamentals(stocks, 'valuation', date = '2018-04-24', fields = ['total_value', 'pe_dynamic', 'turnover_rate', 'pb'])
```

估值数据valuation具体字段

| 字段名称            | 字段类型          | 字段说明        | 属性   |
| --------------- | ------------- | ----------- | ---- |
| trading\_day    | str           | 交易日期        | 固定返回 |
| total\_value    | str           | A股总市值(元)    | 固定返回 |
| float\_value    | str           | A股流通市值(元)   | 自选返回 |
| naps            | numpy.float64 | 每股净资产/(元/股) | 自选返回 |
| pcf             | str           | 市现率         | 自选返回 |
| secu\_abbr      | str           | 证券简称        | 自选返回 |
| secu\_code      | str           | 证券代码        | 固定返回 |
| ps              | numpy.float64 | 市销率PS       | 自选返回 |
| ps\_ttm         | numpy.float64 | 市销率PS(TTM)  | 自选返回 |
| pe\_ttm         | numpy.float64 | 市盈率PE(TTM)  | 自选返回 |
| a\_shares       | str           | A股股本        | 自选返回 |
| a\_floats       | numpy.float64 | 可流通A股       | 自选返回 |
| pe\_dynamic     | str           | 动态市盈率       | 自选返回 |
| pe\_static      | str           | 静态市盈率       | 自选返回 |
| b\_floats       | str           | 可流通B股       | 自选返回 |
| b\_shares       | numpy.float64 | B股股本        | 自选返回 |
| h\_shares       | numpy.float64 | H股股本        | 自选返回 |
| total\_shares   | int           | 总股本         | 自选返回 |
| turnover\_rate  | str           | 换手率         | 自选返回 |
| dividend\_ratio | str           | 滚动股息率       | 自选返回 |
| pb              | numpy.float64 | 市净率         | 自选返回 |
| roe             | numpy.float64 | 净资产收益率      | 自选返回 |

## balance\_statement-资产负债表

```python
get_fundamentals(security, 'balance_statement',fields, date = None, start_year = None, end_year = None, report_types = None, date_type = None, merge_type = None)
```

```python

               company_type   publ_date   secu_abbr    total_assets
end_date
2013-03-31            1       2013-04-19   恒生电子     1.76795e+09
2014-03-31            1       2014-04-29   恒生电子     2.20999e+09
2015-03-31            1       2015-04-25   恒生电子     3.09674e+09
```

### 示例

```python
# 获取数据的两种模式
# 1. 按日期查询模式（默认以发布日期为参考时间）：返回输入日期之前对应的财务数据
# 在回测中获取单一股票中对应回测日期资产负债表中资产总计（total_assets）数据
get_fundamentals('600570.SS','balance_statement','total_assets','20160628')

# 2. 按年份查询模式：返回输入年份范围内对应季度的财务数据
# 获取恒生电子(600570.SS)从2013年至2015年第一季度资产负债表中资产总计
#（total_assets）数据
get_fundamentals('600570.SS','balance_statement','total_assets',start_year='2013',end_year='2015', report_types='1')
```

资产负债表- balance\_statement具体字段

| 字段名称                                   | 字段类型          | 字段说明           |
| -------------------------------------- | ------------- | -------------- |
| secu\_code                             | str           | 股票代码           |
| secu\_abbr                             | str           | 股票简称           |
| company\_type                          | str           | 公司类型           |
| end\_date                              | str           | 截止日期           |
| publ\_date                             | str           | 公告日期           |
| total\_assets                          | numpy.float64 | 资产总计           |
| total\_liability                       | numpy.float64 | 负债合计           |
| total\_liability\_and\_equity          | numpy.float64 | 负债和股东权益总计      |
| settlement\_provi                      | numpy.float64 | 结算备付金          |
| client\_provi                          | numpy.float64 | 客户备付金          |
| deposit\_in\_interbank                 | numpy.float64 | 存放同业款项         |
| r\_metal                               | numpy.float64 | 贵金属            |
| lend\_capital                          | numpy.float64 | 拆出资金           |
| derivative\_assets                     | numpy.float64 | 衍生金融资产         |
| bought\_sellback\_assets               | numpy.float64 | 买入返售金融资产       |
| loan\_and\_advance                     | numpy.float64 | 发放贷款和垫款        |
| insurance\_receivables                 | numpy.float64 | 应收保费           |
| receivable\_subrogation\_fee           | numpy.float64 | 应收代位追偿款        |
| reinsurance\_receivables               | numpy.float64 | 应收分保账款         |
| receivable\_unearned\_r                | numpy.float64 | 应收分保未到期责任准备金   |
| receivable\_claims\_r                  | numpy.float64 | 应收分保未决赔款准备金    |
| receivable\_life\_r                    | numpy.float64 | 应收分保寿险责任准备金    |
| receivable\_lt\_health\_r              | numpy.float64 | 应收分保长期健康险责任准备金 |
| insurer\_impawn\_loan                  | numpy.float64 | 保户质押贷款         |
| fixed\_deposit                         | numpy.float64 | 定期存款           |
| refundable\_capital\_deposit           | numpy.float64 | 存出资本保证金        |
| refundable\_deposit                    | numpy.float64 | 存出保证金          |
| independence\_account\_assets          | numpy.float64 | 独立账户资产         |
| other\_assets                          | numpy.float64 | 其他资产           |
| borrowing\_from\_centralbank           | numpy.float64 | 向中央银行借款        |
| deposit\_of\_interbank                 | numpy.float64 | 同业及其他金融机构存放款项  |
| borrowing\_capital                     | numpy.float64 | 拆入资金           |
| derivative\_liability                  | numpy.float64 | 衍生金融负债         |
| sold\_buyback\_secu\_proceeds          | numpy.float64 | 卖出回购金融资产款      |
| deposit                                | numpy.float64 | 吸收存款           |
| proxy\_secu\_proceeds                  | numpy.float64 | 代理买卖证券款        |
| sub\_issue\_secu\_proceeds             | numpy.float64 | 代理承销证券款        |
| deposits\_received                     | numpy.float64 | 存入保证金          |
| advance\_insurance                     | numpy.float64 | 预收保费           |
| commission\_payable                    | numpy.float64 | 应付手续费及佣金       |
| reinsurance\_payables                  | numpy.float64 | 应付分保账款         |
| compensation\_payable                  | numpy.float64 | 应付赔付款          |
| policy\_dividend\_payable              | numpy.float64 | 应付保单红利         |
| insurer\_deposit\_investment           | numpy.float64 | 保户储金及投资款       |
| unearned\_premium\_reserve             | numpy.float64 | 未到期责任准备金       |
| outstanding\_claim\_reserve            | numpy.float64 | 未决赔款准备金        |
| life\_insurance\_reserve               | numpy.float64 | 寿险责任准备金        |
| lt\_health\_insurance\_lr              | numpy.float64 | 长期健康险责任准备金     |
| independence\_liability                | numpy.float64 | 独立账户负债         |
| other\_liability                       | numpy.float64 | 其他负债           |
| cash\_equivalents                      | numpy.float64 | 货币资金           |
| client\_deposit                        | numpy.float64 | 客户资金存款         |
| trading\_assets                        | numpy.float64 | 交易性金融资产        |
| bill\_receivable                       | numpy.float64 | 应收票据           |
| dividend\_receivable                   | numpy.float64 | 应收股利           |
| interest\_receivable                   | numpy.float64 | 应收利息           |
| account\_receivable                    | numpy.float64 | 应收账款           |
| other\_receivable                      | numpy.float64 | 其他应收款          |
| advance\_payment                       | numpy.float64 | 预付款项           |
| inventories                            | numpy.float64 | 存货             |
| non\_current\_asset\_in\_one\_year     | numpy.float64 | 一年内到期的非流动资产    |
| other\_current\_assets                 | numpy.float64 | 其他流动资产         |
| total\_current\_assets                 | numpy.float64 | 流动资产合计         |
| shortterm\_loan                        | numpy.float64 | 短期借款           |
| impawned\_loan                         | numpy.float64 | 质押借款           |
| trading\_liability                     | numpy.float64 | 交易性金融负债        |
| notes\_payable                         | numpy.float64 | 应付票据           |
| accounts\_payable                      | numpy.float64 | 应付账款           |
| advance\_receipts                      | numpy.float64 | 预收款项           |
| salaries\_payable                      | numpy.float64 | 应付职工薪酬         |
| dividend\_payable                      | numpy.float64 | 应付股利           |
| taxs\_payable                          | numpy.float64 | 应交税费           |
| interest\_payable                      | numpy.float64 | 应付利息           |
| other\_payable                         | numpy.float64 | 其他应付款          |
| non\_current\_liability\_in\_one\_year | numpy.float64 | 一年内到期的非流动负债    |
| other\_current\_liability              | numpy.float64 | 其他流动负债         |
| total\_current\_liability              | numpy.float64 | 流动负债合计         |
| hold\_for\_sale\_assets                | numpy.float64 | 可供出售金融资产       |
| hold\_to\_maturity\_investments        | numpy.float64 | 持有至到期投资        |
| investment\_property                   | numpy.float64 | 投资性房地产         |
| longterm\_equity\_invest               | numpy.float64 | 长期股权投资         |
| longterm\_receivable\_account          | numpy.float64 | 长期应收款          |
| fixed\_assets                          | numpy.float64 | 固定资产           |
| construction\_materials                | numpy.float64 | 工程物资           |
| constru\_in\_process                   | numpy.float64 | 在建工程           |
| fixed\_assets\_liquidation             | numpy.float64 | 固定资产清理         |
| biological\_assets                     | numpy.float64 | 生产性生物资产        |
| oil\_gas\_assets                       | numpy.float64 | 油气资产           |
| intangible\_assets                     | numpy.float64 | 无形资产           |
| seat\_costs                            | numpy.float64 | 交易席位费          |
| development\_expenditure               | numpy.float64 | 开发支出           |
| good\_will                             | numpy.float64 | 商誉             |
| long\_deferred\_expense                | numpy.float64 | 长期待摊费用         |
| deferred\_tax\_assets                  | numpy.float64 | 递延所得税资产        |
| other\_non\_current\_assets            | numpy.float64 | 其他非流动资产        |
| total\_non\_current\_assets            | numpy.float64 | 非流动资产合计        |
| longterm\_loan                         | numpy.float64 | 长期借款           |
| bonds\_payable                         | numpy.float64 | 应付债券           |
| longterm\_account\_payable             | numpy.float64 | 长期应付款          |
| long\_salaries\_pay                    | numpy.float64 | 长期应付职工薪酬       |
| specific\_account\_payable             | numpy.float64 | 专项应付款          |
| estimate\_liability                    | numpy.float64 | 预计负债           |
| deferred\_tax\_liability               | numpy.float64 | 递延所得税负债        |
| long\_defer\_income                    | numpy.float64 | 长期递延收益         |
| other\_non\_current\_liability         | numpy.float64 | 其他非流动负债        |
| total\_non\_current\_liability         | numpy.float64 | 非流动负债合计        |
| paidin\_capital                        | numpy.float64 | 实收资本（或股本）      |
| other\_equityinstruments               | numpy.float64 | 其他权益工具         |
| capital\_reserve\_fund                 | numpy.float64 | 资本公积           |
| surplus\_reserve\_fund                 | numpy.float64 | 盈余公积           |
| retained\_profit                       | numpy.float64 | 未分配利润          |
| treasury\_stock                        | numpy.float64 | 减：库存股          |
| other\_composite\_income               | numpy.float64 | 其他综合收益         |
| ordinary\_risk\_reserve\_fund          | numpy.float64 | 一般风险准备         |
| foreign\_currency\_report\_conv\_diff  | numpy.float64 | 外币报表折算差额       |
| specific\_reserves                     | numpy.float64 | 专项储备           |
| se\_without\_mi                        | numpy.float64 | 归属母公司股东权益合计    |
| minority\_interests                    | numpy.float64 | 少数股东权益         |
| total\_shareholder\_equity             | numpy.float64 | 所有者权益合计        |

## income\_statement-利润表

```python
get_fundamentals(security, 'income_statement',fields, date = None, start_year = None, end_year = None, report_types = None, date_type = None, merge_type = None)
```

```python

                company_type   net_profit   publ_date      secu_abbr
end_date
2013-03-31            1        3.71658e+07  2013-04-19      恒生电子
2014-03-31            1        5.38395e+07  2014-04-29      恒生电子
2015-03-31            1           7.22e+07  2015-04-25      恒生电子
```

### 示例

```python
# 获取数据的两种模式
# 1. 按日期查询模式（默认以发布日期为参考时间）：返回输入日期之前对应的财务数据
# 在回测中获取单一股票中对应回测日期第一季度利润表中净利润（net_profit）数据
get_fundamentals('600570.SS','income_statement','net_profit','20160628')

# 2. 按年份查询模式：返回输入年份范围内对应季度的财务数据
# 获取恒生电子(600570.SS)从2013年至2015年第一季度利润表中净利润（net_profit）# 数据
get_fundamentals('600570.SS','income_statement','net_profit',start_year='2013',end_year='2015', report_types='1')
```

利润表- income\_statement具体字段

| 字段名称                              | 字段类型          | 字段说明             |
| --------------------------------- | ------------- | ---------------- |
| secu\_code                        | str           | 股票代码             |
| secu\_abbr                        | str           | 股票简称             |
| company\_type                     | str           | 公司类型             |
| end\_date                         | str           | 截止日期             |
| publ\_date                        | str           | 公告日期             |
| basic\_eps                        | numpy.float64 | 基本每股收益           |
| diluted\_eps                      | numpy.float64 | 稀释每股收益           |
| net\_profit                       | numpy.float64 | 净利润              |
| np\_parent\_company\_owners       | numpy.float64 | 归属于母公司所有者的净利润    |
| minority\_profit                  | numpy.float64 | 少数股东损益           |
| total\_operating\_cost            | numpy.float64 | 营业总成本            |
| operating\_payout                 | numpy.float64 | 营业支出             |
| refunded\_premiums                | numpy.float64 | 退保金              |
| compensation\_expense             | numpy.float64 | 赔付支出             |
| amortization\_expense             | numpy.float64 | 减:摊回赔付支出         |
| premium\_reserve                  | numpy.float64 | 提取保险责任准备金        |
| amortization\_premium\_reserve    | numpy.float64 | 减:摊回保险责任准备金      |
| policy\_dividend\_payout          | numpy.float64 | 保单红利支出           |
| reinsurance\_cost                 | numpy.float64 | 分保费用             |
| amortization\_reinsurance\_cost   | numpy.float64 | 减:摊回分保费用         |
| insurance\_commission\_expense    | numpy.float64 | 保险手续费及佣金支出       |
| other\_operating\_cost            | numpy.float64 | 其他营业成本           |
| operating\_cost                   | numpy.float64 | 营业成本             |
| operating\_tax\_surcharges        | numpy.float64 | 营业税金及附加          |
| operating\_expense                | numpy.float64 | 销售费用             |
| administration\_expense           | numpy.float64 | 管理费用             |
| financial\_expense                | numpy.float64 | 财务费用             |
| asset\_impairment\_loss           | numpy.float64 | 资产减值损失           |
| operating\_profit                 | numpy.float64 | 营业利润             |
| non\_operating\_income            | numpy.float64 | 加：营业收入           |
| non\_operating\_expense           | numpy.float64 | 减：营业外支出          |
| non\_current\_assetss\_deal\_loss | numpy.float64 | 其中：非流动资产处置净损失    |
| total\_operating\_revenue         | numpy.float64 | 营业总收入            |
| operating\_revenue                | numpy.float64 | 营业收入             |
| net\_interest\_income             | numpy.float64 | 利息净收入            |
| interest\_income                  | numpy.float64 | 其中：利息收入          |
| interest\_expense                 | numpy.float64 | 其中:利息支出          |
| net\_commission\_income           | numpy.float64 | 手续费及佣金净收入        |
| commission\_income                | numpy.float64 | 其中：手续费及佣金收入      |
| commission\_expense               | numpy.float64 | 其中：手续费及佣金支出      |
| net\_proxy\_secu\_income          | numpy.float64 | 其中：代理买卖证券业务净收入   |
| net\_subissue\_secu\_income       | numpy.float64 | 其中：证券承销业务净收入     |
| net\_trust\_income                | numpy.float64 | 其中:受托客户资产管理业务净收入 |
| premiums\_earned                  | numpy.float64 | 已赚保费             |
| premiums\_income                  | numpy.float64 | 保险业务收入           |
| reinsurance\_income               | numpy.float64 | 其中：分保费收入         |
| reinsurance                       | numpy.float64 | 减：分出保费           |
| unearned\_premium\_reserve        | numpy.float64 | 提取未到期责任准备金       |
| other\_operating\_revenue         | numpy.float64 | 其他营业收入           |
| other\_net\_revenue               | numpy.float64 | 非营业性收入           |
| fair\_value\_change\_income       | numpy.float64 | 公允价值变动净收益        |
| invest\_income                    | numpy.float64 | 投资净收益            |
| invest\_income\_associates        | numpy.float64 | 其中:对联营合营企业的投资收益  |
| exchange\_income                  | numpy.float64 | 汇兑收益             |
| total\_profit                     | numpy.float64 | 利润总额             |
| income\_tax\_cost                 | numpy.float64 | 减：所得税费用          |
| total\_composite\_income          | numpy.float64 | 综合收益总额           |
| ci\_parent\_company\_owners       | numpy.float64 | 归属于母公司所有者的综合收益总额 |
| ci\_minority\_owners              | numpy.float64 | 归属于少数股东的综合收益总额   |

## cashflow\_statement-现金流量表

```python
get_fundamentals(security,'cashflow_statement',fields, date = None, start_year = None, end_year = None, report_types = None, date_type = None, merge_type = None)
```

```python

               company_type invest_cash_paid   publ_date      secu_abbr
end_date
2013-03-31            1        5.271e+08       2013-04-19      恒生电子
2014-03-31            1       3.9488e+08       2014-04-29      恒生电子
2015-03-31            1      9.92432e+08       2015-04-25      恒生电子
```

### 示例

```python
# 获取数据的两种模式
# 1. 按日期查询模式（默认以发布日期为参考时间）：返回输入日期之前对应的财务数据
# 在回测中获取单一股票中对应回测日期第一季度现金流量表中投资支付的现金
#（invest_cash_paid）数据
get_fundamentals('600570.SS','cashflow_statement','invest_cash_paid','20160628')

# 2. 按年份查询模式：返回输入年份范围内对应季度的财务数据
# 获取恒生电子(600570.SS)从2013年至2015年第一季度现金流量表中投资支付的现金#（invest_cash_paid）数据
get_fundamentals('600570.SS','cashflow_statement','invest_cash_paid',start_year='2013',end_year='2015', report_types='1')
```

现金流量表- income\_statement具体字段

| 字段名称                                  | 字段类型          | 字段说明                      |
| ------------------------------------- | ------------- | ------------------------- |
| secu\_code                            | str           | 股票代码                      |
| secu\_abbr                            | str           | 股票简称                      |
| company\_type                         | str           | 公司类型                      |
| end\_date                             | str           | 截止日期                      |
| publ\_date                            | str           | 公告日期                      |
| goods\_sale\_service\_render\_cash    | numpy.float64 | 销售商品、提供劳务收到的现金            |
| tax\_levy\_refund                     | numpy.float64 | 收到的税费返还                   |
| net\_deposit\_increase                | numpy.float64 | 客户存款和同业存放款项净增加额           |
| net\_borrowing\_from\_central\_bank   | numpy.float64 | 向中央银行借款净增加额               |
| net\_borrowing\_from\_finance\_co     | numpy.float64 | 向其他金融机构拆入资金净增加额           |
| interest\_and\_commission\_cashin     | numpy.float64 | 收取利息、手续费及佣金的现金            |
| net\_deal\_trading\_assets            | numpy.float64 | 处置交易性金融资产净增加额             |
| net\_buyback                          | numpy.float64 | 回购业务资金净增加额                |
| net\_original\_insurance\_cash        | numpy.float64 | 收到原保险合同保费取得的现金            |
| net\_reinsurance\_cash                | numpy.float64 | 收到再保业务现金净额                |
| net\_insurer\_deposit\_investment     | numpy.float64 | 保户储金及投资款净增加额              |
| other\_cashin\_related\_operate       | numpy.float64 | 收到其他与经营活动有关的现金            |
| subtotal\_operate\_cash\_inflow       | numpy.float64 | 经营活动现金流入小计                |
| goods\_and\_services\_cash\_paid      | numpy.float64 | 购买商品、接受劳务支付的现金            |
| staff\_behalf\_paid                   | numpy.float64 | 支付给职工以及为职工支付的现金           |
| all\_taxes\_paid                      | numpy.float64 | 支付的各项税费                   |
| net\_loan\_and\_advance\_increase     | numpy.float64 | 客户贷款及垫款净增加额               |
| net\_deposit\_in\_cb\_and\_ib         | numpy.float64 | 存放中央银行和同业款项净增加额           |
| net\_lend\_capital                    | numpy.float64 | 拆出资金净增加额                  |
| commission\_cash\_paid                | numpy.float64 | 支付手续费及佣金的现金               |
| original\_compensation\_paid          | numpy.float64 | 支付原保险合同赔付款项的现金            |
| net\_cash\_for\_reinsurance           | numpy.float64 | 支付再保业务现金净额                |
| policy\_dividend\_cash\_paid          | numpy.float64 | 支付保单红利的现金                 |
| other\_operate\_cash\_paid            | numpy.float64 | 支付其他与经营活动有关的现金            |
| subtotal\_operate\_cash\_outflow      | numpy.float64 | 经营活动现金流出小计                |
| net\_operate\_cash\_flow              | numpy.float64 | 经营活动产生的现金流量净额             |
| invest\_withdrawal\_cash              | numpy.float64 | 收回投资收到的现金                 |
| invest\_proceeds                      | numpy.float64 | 取得投资收益收到的现金               |
| fix\_intan\_other\_asset\_dispo\_cash | numpy.float64 | 处置固定资产、无形资产和其他长期资产收回的现金净额 |
| net\_cash\_deal\_sub\_company         | numpy.float64 | 处置子公司及其他营业单位收到的现金净额       |
| other\_cash\_from\_invest\_act        | numpy.float64 | 收到其他与投资活动有关的现金            |
| subtotal\_invest\_cash\_inflow        | numpy.float64 | 投资活动现金流入小计                |
| fix\_intan\_other\_asset\_acqui\_cash | numpy.float64 | 购建固定资产、无形资产和其他长期资产支付的现金   |
| invest\_cash\_paid                    | numpy.float64 | 投资支付的现金                   |
| net\_cash\_from\_sub\_company         | numpy.float64 | 取得子公司及其他营业单位支付的现金净额       |
| impawned\_loan\_net\_increase         | numpy.float64 | 质押贷款净增加额                  |
| other\_cash\_to\_invest\_act          | numpy.float64 | 支付其他与投资活动有关的现金            |
| subtotal\_invest\_cash\_outflow       | numpy.float64 | 投资活动现金流出小计                |
| net\_invest\_cash\_flow               | numpy.float64 | 投资活动产生的现金流量净额             |
| cash\_from\_invest                    | numpy.float64 | 吸收投资收到的现金                 |
| cash\_from\_bonds\_issue              | numpy.float64 | 发行债券收到的现金                 |
| cash\_from\_borrowing                 | numpy.float64 | 取得借款收到的现金                 |
| other\_finance\_act\_cash             | numpy.float64 | 收到其他与筹资活动有关的现金            |
| subtotal\_finance\_cash\_inflow       | numpy.float64 | 筹资活动现金流入小计                |
| borrowing\_repayment                  | numpy.float64 | 偿还债务支付的现金                 |
| dividend\_interest\_payment           | numpy.float64 | 分配股利、利润或偿付利息支付的现金         |
| other\_finance\_act\_payment          | numpy.float64 | 支付其他与筹资活动有关的现金            |
| subtotal\_finance\_cash\_outflow      | numpy.float64 | 筹资活动现金流出小计                |
| net\_finance\_cash\_flow              | numpy.float64 | 筹资活动产生的现金流量净额             |
| exchan\_rate\_change\_effect          | numpy.float64 | 汇率变动对现金及现金等价物的影响          |
| cash\_equivalent\_increase            | numpy.float64 | 现金及现金等价物净增加额              |
| begin\_period\_cash                   | numpy.float64 | 加：期初现金及现金等价物余额            |
| end\_period\_cash\_equivalent         | numpy.float64 | 期末现金及现金等价物余额              |
| net\_profit                           | numpy.float64 | 净利润                       |
| minority\_profit                      | numpy.float64 | 加:少数股东损益                  |
| assets\_depreciation\_reserves        | numpy.float64 | 加:资产减值准备                  |
| fixed\_asset\_depreciation            | numpy.float64 | 固定资产折旧                    |
| intangible\_asset\_amortization       | numpy.float64 | 收无形资产摊销                   |
| deferred\_expense\_amort              | numpy.float64 | 长期待摊费用摊销                  |
| deferred\_expense\_decreased          | numpy.float64 | 待摊费用减少(减:增加)              |
| accrued\_expense\_added               | numpy.float64 | 预提费用增加(减:减少)              |
| fix\_intanther\_asset\_dispo\_loss    | numpy.float64 | 处置固定资产、无形资产和其他长期资产的损失     |
| fixed\_asset\_scrap\_loss             | numpy.float64 | 固定资产报废损失                  |
| loss\_from\_fair\_value\_changes      | numpy.float64 | 公允价值变动损失                  |
| financial\_expense                    | numpy.float64 | 财务费用                      |
| invest\_loss                          | numpy.float64 | 投资损失                      |
| defered\_tax\_asset\_decrease         | numpy.float64 | 递延所得税资产减少                 |
| defered\_tax\_liability\_increase     | numpy.float64 | 递延所得税负债增加                 |
| inventory\_decrease                   | numpy.float64 | 存货的减少                     |
| operate\_receivable\_decrease         | numpy.float64 | 经营性应收项目的减少                |
| operate\_payable\_increase            | numpy.float64 | 经营性应付项目的增加                |
| others                                | numpy.float64 | 其他                        |
| net\_operate\_cash\_flow\_notes       | numpy.float64 | 经营活动产生的现金流量净额             |
| debt\_to\_captical                    | numpy.float64 | 债务转为资本                    |
| cbs\_expiring\_within\_one\_year      | numpy.float64 | 一年内到期的可转换公司债券             |
| fixed\_assets\_finance\_leases        | numpy.float64 | 融资租入固定资产                  |
| cash\_at\_end\_of\_year               | numpy.float64 | 现金的期末余额                   |
| cash\_at\_beginning\_of\_year         | numpy.float64 | 减:现金的期初余额                 |
| cash\_equivalents\_at\_end\_of\_year  | numpy.float64 | 加:现金等价物的期末余额              |
| cash\_equivalents\_at\_beginning      | numpy.float64 | 减:现金等价物的期初余额              |
| net\_incr\_in\_cash\_and\_equivalents | numpy.float64 | 现金及现金等价物净增加额              |

## growth\_ability-成长能力

```python
get_fundamentals(security,'growth_ability',fields, date = None, start_year = None, end_year = None, report_types = None, date_type = None)
```

```python

               oper_profit_grow_rate   publ_date      secu_abbr
end_date
2013-03-31               124.705       2013-04-19      恒生电子
2014-03-31                9.1946       2014-04-29      恒生电子
2015-03-31               14.2251       2015-04-25      恒生电子
```

注意: 获取此表中数据，不支持输入的参数有：merge\_type

### 示例

```python
# 获取数据的两种模式
# 1. 按日期查询模式（默认以发布日期为参考时间）：返回输入日期之前对应的财务数据
# 在回测中获取单一股票中对应回测日期第一季度成长能力指标中营业利润同比增长
#（oper_profit_grow_rate）数据
get_fundamentals('600570.SS','growth_ability','oper_profit_grow_rate','20160628')

# 2. 按年份查询模式：返回输入年份范围内对应季度的财务数据
# 获取恒生电子(600570.SS)从2013年至2015年第一季度成长能力指标中营业利润同比# 增长（oper_profit_grow_rate）数据
get_fundamentals('600570.SS','growth_ability','oper_profit_grow_rate',start_year='2013',end_year='2015', report_types='1')
```

成长能力- growth\_ability具体字段

| 字段名称                             | 字段类型          | 字段说明                   | 属性   |
| -------------------------------- | ------------- | ---------------------- | ---- |
| secu\_code                       | str           | 股票代码                   | 固定返回 |
| secu\_abbr                       | str           | 股票简称                   | 固定返回 |
| publ\_date                       | str           | 公告日期                   | 固定返回 |
| end\_date                        | str           | 截止日期                   | 固定返回 |
| basic\_eps\_yoy                  | numpy.float64 | 基本每股收益同比增长（%）          | 自选返回 |
| diluted\_eps\_yoy                | numpy.float64 | 稀释每股收益同比增长（%）          | 自选返回 |
| operating\_revenue\_grow\_rate   | numpy.float64 | 营业收入同比增长（%）            | 自选返回 |
| np\_parent\_company\_yoy         | numpy.float64 | 归属母公司股东的净利润同比增长（%）     | 自选返回 |
| net\_operate\_cash\_flow\_yoy    | numpy.float64 | 经营活动产生的现金流量净额同比增长（%）   | 自选返回 |
| oper\_profit\_grow\_rate         | numpy.float64 | 营业利润同比增长（%）            | 自选返回 |
| total\_profit\_grow\_rate        | numpy.float64 | 利润总额同比增长（%）            | 自选返回 |
| eps\_grow\_rate\_ytd             | numpy.float64 | 每股净资产相对年初增长率（%）        | 自选返回 |
| se\_without\_mi\_grow\_rate\_ytd | numpy.float64 | 归属母公司股东的权益相对年初增长率（%）   | 自选返回 |
| ta\_grow\_rate\_ytd              | numpy.float64 | 资产总计相对年初增长率（%)         | 自选返回 |
| np\_parent\_company\_cut\_yoy    | numpy.float64 | 归属母公司股东的净利润(扣除)同比增长（%） | 自选返回 |
| avg\_np\_yoy\_past\_five\_year   | numpy.float64 | 过去五年同期归属母公司净利润平均增幅（%）  | 自选返回 |
| oper\_cash\_ps\_grow\_rate       | numpy.float64 | 每股经营活动产生的现金流量净额同比增长（%） | 自选返回 |
| naor\_yoy                        | numpy.float64 | 净资产收益率(摊薄)同比增（%）       | 自选返回 |
| net\_asset\_grow\_rate           | numpy.float64 | 净资产同比增长（%）             | 自选返回 |
| total\_asset\_grow\_rate         | numpy.float64 | 总资产同比增长（%）             | 自选返回 |
| sustainable\_grow\_rate          | numpy.float64 | 可持续增长率（%）              | 自选返回 |
| net\_profit\_grow\_rate          | numpy.float64 | 净利润同比增长（%）             | 自选返回 |

## profit\_ability-盈利能力

```python
get_fundamentals(security,'profit_ability',fields, date = None, start_year = None, end_year = None, report_types = None, date_type = None)
```

```python

             publ_date     roe     secu_abbr
end_date
2013-03-31  2013-04-19  2.8127      恒生电子
2014-03-31  2014-04-29  3.3056      恒生电子
2015-03-31  2015-04-25  3.4869      恒生电子
```

注意: 获取此表中数据，不支持输入的参数有：merge\_type

### 示例

```python
# 获取数据的两种模式
# 1. 按日期查询模式（默认以发布日期为参考时间）：返回输入日期之前对应的财务数据
# 在回测中获取单一股票中对应回测日期第一季度盈利能力指标中净资产收益率（roe）数据
get_fundamentals('600570.SS','profit_ability','roe','20160628')

# 2. 按年份查询模式：返回输入年份范围内对应季度的财务数据
# 获取恒生电子(600570.SS)从2013年至2015年第一季度盈利能力指标中净资产收益率
#（roe）数据
get_fundamentals('600570.SS','profit_ability','roe',start_year='2013',end_year='2015',report_types='1')
```

盈利能力- profit\_ability具体字段

| 字段名称                             | 字段类型          | 字段说明                 | 属性   |
| -------------------------------- | ------------- | -------------------- | ---- |
| secu\_code                       | str           | 股票代码                 | 固定返回 |
| secu\_abbr                       | str           | 股票简称                 | 固定返回 |
| publ\_date                       | str           | 公告日期                 | 固定返回 |
| end\_date                        | str           | 截止日期                 | 固定返回 |
| roe\_avg                         | numpy.float64 | 净资产收益率%平均计算值（%）      | 自选返回 |
| roe\_weighted                    | numpy.float64 | 净资产收益率%加权公布值（%）      | 自选返回 |
| roe                              | numpy.float64 | 净资产收益率%摊薄公布值（%）      | 自选返回 |
| roe\_cut                         | numpy.float64 | 净资产收益率%扣除摊薄（%）       | 自选返回 |
| roe\_cut\_weighted               | numpy.float64 | 净资产收益率%扣除加权（%）       | 自选返回 |
| roe\_ttm                         | numpy.float64 | 净资产收益率\_TTM（%）       | 自选返回 |
| roa\_ebit                        | numpy.float64 | 总资产报酬率（%）            | 自选返回 |
| roa\_ebit\_ttm                   | numpy.float64 | 总资产报酬率\_TTM（%）       | 自选返回 |
| roa                              | numpy.float64 | 总资产净利率（%）            | 自选返回 |
| roa\_ttm                         | numpy.float64 | 总资产净利率\_TTM（%）       | 自选返回 |
| roic                             | numpy.float64 | 投入资本回报率（%）           | 自选返回 |
| net\_profit\_ratio               | numpy.float64 | 销售净利率（%）             | 自选返回 |
| net\_profit\_ratio\_ttm          | numpy.float64 | 销售净利率\_TTM（%）        | 自选返回 |
| gross\_income\_ratio             | numpy.float64 | 销售毛利率（%）             | 自选返回 |
| gross\_income\_ratio\_ttm        | numpy.float64 | 销售毛利率\_TTM（%）        | 自选返回 |
| sales\_cost\_ratio               | numpy.float64 | 销售成本率（%）             | 自选返回 |
| period\_costs\_rate              | numpy.float64 | 销售期间费用率（%）           | 自选返回 |
| period\_costs\_rate\_ttm         | numpy.float64 | 销售期间费用率\_TTM（%）      | 自选返回 |
| np\_to\_tor                      | numpy.float64 | 净利润／营业总收入（%）         | 自选返回 |
| np\_to\_tor\_ttm                 | numpy.float64 | 净利润／营业总收入\_TTM（%）    | 自选返回 |
| operating\_profit\_to\_tor       | numpy.float64 | 营业利润／营业总收入（%）        | 自选返回 |
| operating\_profit\_to\_tor\_ttm  | numpy.float64 | 营业利润／营业总收入\_TTM（%）   | 自选返回 |
| ebit\_to\_tor                    | numpy.float64 | 息税前利润／营业总收入（%）       | 自选返回 |
| ebit\_to\_tor\_ttm               | numpy.float64 | 息税前利润／营业总收入\_TTM（%）  | 自选返回 |
| t\_operating\_cost\_to\_tor      | numpy.float64 | 营业总成本／营业总收入（%）       | 自选返回 |
| t\_operating\_cost\_to\_tor\_ttm | numpy.float64 | 营业总成本／营业总收入\_TTM（%）  | 自选返回 |
| operating\_expense\_rate         | numpy.float64 | 销售费用／营业总收入（%）        | 自选返回 |
| operating\_expense\_rate\_ttm    | numpy.float64 | 销售费用／营业总收入\_TTM（%）   | 自选返回 |
| admini\_expense\_rate            | numpy.float64 | 管理费用／营业总收入（%）        | 自选返回 |
| admini\_expense\_rate\_ttm       | numpy.float64 | 管理费用／营业总收入\_TTM（%）   | 自选返回 |
| financial\_expense\_rate         | numpy.float64 | 财务费用／营业总收入（%）        | 自选返回 |
| financial\_expense\_rate\_ttm    | numpy.float64 | 财务费用／营业总收入\_TTM（%）   | 自选返回 |
| asset\_impa\_loss\_to\_tor       | numpy.float64 | 资产减值损失／营业总收入（%）      | 自选返回 |
| asset\_impa\_loss\_to\_tor\_ttm  | numpy.float64 | 资产减值损失／营业总收入\_TTM（%） | 自选返回 |
| net\_profit                      | numpy.float64 | 归属母公司净利润（元）          | 自选返回 |
| net\_profit\_cut                 | numpy.float64 | 扣除非经常性损益后的净利润（元）     | 自选返回 |
| ebit                             | numpy.float64 | 息税前利润（元）             | 自选返回 |
| ebitda                           | numpy.float64 | 息税折旧摊销前利润（元）         | 自选返回 |
| operating\_profit\_ratio         | numpy.float64 | 营业利润率（%）             | 自选返回 |
| total\_profit\_cost\_ratio       | numpy.float64 | 成本费用利润率              | 自选返回 |

## eps-每股指标

```python
get_fundamentals(security,'eps',fields, date = None, start_year = None, end_year = None, report_types = None, date_type = None)
```

注意: 获取此表中数据，不支持输入的参数有：merge\_type

```python

           basic_eps   publ_date      secu_abbr
end_date
2013-03-31      0.06   2013-04-19      恒生电子
2014-03-31      0.09   2014-04-29      恒生电子
2015-03-31      0.11   2015-04-25      恒生电子
```

### 示例

```python
# 获取数据的两种模式
# 1. 按日期查询模式（默认以发布日期为参考时间）：返回输入日期之前对应的财务数据
# 在回测中获取单一股票中对应回测日期第一季度每股指标中基本每股收益（basic_eps）# 数据
get_fundamentals('600570.SS','eps','basic_eps','20160628')

# 2. 按年份查询模式：返回输入年份范围内对应季度的财务数据
# 获取恒生电子(600570.SS)从2013年至2015年第一季度每股指标中基本每股收益
#（basic_eps）数据
get_fundamentals('600570.SS','eps','basic_eps',start_year='2013',end_year='2015',report_types='1')
```

每股指标- eps具体字段

| 字段名称                              | 字段类型          | 字段说明                      | 属性   |
| --------------------------------- | ------------- | ------------------------- | ---- |
| secu\_code                        | str           | 股票代码                      | 固定返回 |
| secu\_abbr                        | str           | 股票简称                      | 固定返回 |
| publ\_date                        | str           | 公告日期                      | 固定返回 |
| end\_date                         | str           | 截止日期                      | 固定返回 |
| basic\_eps                        | numpy.float64 | 基本每股收益（元/股）               | 自选返回 |
| diluted\_eps                      | numpy.float64 | 稀释每股收益（元/股）               | 自选返回 |
| eps                               | numpy.float64 | 每股收益\_期末股本摊薄（元/股）         | 自选返回 |
| eps\_ttm                          | numpy.float64 | 每股收益\_TTM（元/股）            | 自选返回 |
| naps                              | numpy.float64 | 每股净资产（元/股）                | 自选返回 |
| total\_operating\_revenue\_ps     | numpy.float64 | 每股营业总收入（元/股）              | 自选返回 |
| main\_income\_ps                  | numpy.float64 | 每股营业收入（元/股）               | 自选返回 |
| operating\_revenue\_ps\_ttm       | numpy.float64 | 每股营业收入\_TTM（元/股）          | 自选返回 |
| oper\_profit\_ps                  | numpy.float64 | 每股营业利润（元/股）               | 自选返回 |
| ebitps                            | numpy.float64 | 每股息税前利润（元/股）              | 自选返回 |
| capital\_surplus\_fund\_ps        | numpy.float64 | 每股资本公积金（元/股）              | 自选返回 |
| surplus\_reserve\_fund\_ps        | numpy.float64 | 每股盈余公积（元/股）               | 自选返回 |
| accumulation\_fund\_ps            | numpy.float64 | 每股公积金（元/股）                | 自选返回 |
| undivided\_profit                 | numpy.float64 | 每股未分配利润（元/股）              | 自选返回 |
| retained\_earnings\_ps            | numpy.float64 | 每股留存收益（元/股）               | 自选返回 |
| net\_operate\_cash\_flow\_ps      | numpy.float64 | 每股经营活动产生的现金流量净额（元/股）      | 自选返回 |
| net\_operate\_cash\_flow\_ps\_ttm | numpy.float64 | 每股经营活动产生的现金流量净额\_TTM（元/股） | 自选返回 |
| cash\_flow\_ps                    | numpy.float64 | 每股现金流量净额（元/股）             | 自选返回 |
| cash\_flow\_ps\_ttm               | numpy.float64 | 每股现金流量净额\_TTM（元/股）        | 自选返回 |
| enterprise\_fcf\_ps               | numpy.float64 | 每股企业自由现金流量（元/股）           | 自选返回 |
| shareholder\_fcf\_ps              | numpy.float64 | 每股股东自由现金流量（元/股）           | 自选返回 |

## operating\_ability-营运能力

```python
get_fundamentals(security,'operating_ability',fields, date = None, start_year = None, end_year = None, report_types = None, date_type = None)
```

注意: 获取此表中数据，不支持输入的参数有：merge\_type

```python

           current_assets_turnover_rate   publ_date     secu_abbr
end_date
2013-03-31                       0.1803   2013-04-19     恒生电子
2014-03-31                       0.1518   2014-04-29     恒生电子
2015-03-31                       0.1568   2015-04-25     恒生电子
```

### 示例

```python
# 获取数据的两种模式
# 1. 按日期查询模式（默认以发布日期为参考时间）：返回输入日期之前对应的财务数据
# 在回测中获取单一股票中对应回测日期第一季度营运能力指标中流动资产周转率
#（current_assets_turnover_rate）数据
get_fundamentals('600570.SS','operating_ability','current_assets_turnover_rate','20160628')

# 2. 按年份查询模式：返回输入年份范围内对应季度的财务数据
# 获取恒生电子(600570.SS)从2013年至2015年第一季度营运能力指标中流动资产周转# 率（current_assets_turnover_rate）数据
get_fundamentals('600570.SS','operating_ability','current_assets_turnover_rate',start_year='2013',end_year='2015', report_types='1')
```

营运能力- operating\_ability具体字段

| 字段名称                                  | 字段类型          | 字段说明          | 属性   |
| ------------------------------------- | ------------- | ------------- | ---- |
| secu\_code                            | str           | 股票代码          | 固定返回 |
| secu\_abbr                            | str           | 股票简称          | 固定返回 |
| publ\_date                            | str           | 公告日期          | 固定返回 |
| end\_date                             | str           | 截止日期          | 固定返回 |
| oper\_cycle                           | numpy.float64 | 营业周期（天/次）     | 自选返回 |
| inventory\_turnover\_rate             | numpy.float64 | 存货周转率（次）      | 自选返回 |
| inventory\_turnover\_days             | numpy.float64 | 存货周转天数（天/次）   | 自选返回 |
| accounts\_receivables\_turnover\_rate | numpy.float64 | 应收帐款周转率（次）    | 自选返回 |
| accounts\_receivables\_turnover\_days | numpy.float64 | 应收帐款周转天数（天/次） | 自选返回 |
| accounts\_payables\_turnover\_rate    | numpy.float64 | 应付帐款周转率（次）    | 自选返回 |
| accounts\_payables\_turnover\_days    | numpy.float64 | 应付帐款周转天数（天/次） | 自选返回 |
| current\_assets\_turnover\_rate       | numpy.float64 | 流动资产周转率（次）    | 自选返回 |
| fixed\_asset\_turnover\_rate          | numpy.float64 | 固定资产周转率（次）    | 自选返回 |
| equity\_turnover\_rate                | numpy.float64 | 股东权益周转率（次）    | 自选返回 |
| total\_asset\_turnover\_rate          | numpy.float64 | 总资产周转率（次）     | 自选返回 |

## debt\_paying\_ability-偿债能力

```python
get_fundamentals(security,'debt_paying_ability',fields, date = None, start_year = None, end_year = None, report_types = None, date_type = None)
```

注意: 获取此表中数据，不支持输入的参数有：merge\_type

```python

           current_ratio   publ_date      secu_abbr
end_date
2013-03-31        3.4234   2013-04-19      恒生电子
2014-03-31        3.4941   2014-04-29      恒生电子
2015-03-31        1.8332   2015-04-25      恒生电子
```

### 示例

```python
# 获取数据的两种模式
# 1. 按日期查询模式（默认以发布日期为参考时间）：返回输入日期之前对应的财务数据
# 在回测中获取单一股票中对应回测日期第一季度偿债能力指标中流动比率（current_ratio）
# 数据
get_fundamentals('600570.SS','debt_paying_ability','current_ratio','20160628')

# 2. 按年份查询模式：返回输入年份范围内对应季度的财务数据
# 获取恒生电子(600570.SS)从2013年至2015年第一季度偿债能力指标中流动比率
#（current_ratio）数据
get_fundamentals('600570.SS','debt_paying_ability','current_ratio',start_year='2013',end_year='2015', report_types='1')
```

偿债能力- debt\_paying\_ability具体字段

| 字段名称                                  | 字段类型          | 字段说明               | 属性   |
| ------------------------------------- | ------------- | ------------------ | ---- |
| secu\_code                            | str           | 股票代码               | 固定返回 |
| secu\_abbr                            | str           | 股票简称               | 固定返回 |
| publ\_date                            | str           | 公告日期               | 固定返回 |
| end\_date                             | str           | 截止日期               | 固定返回 |
| current\_ratio                        | numpy.float64 | 流动比率               | 自选返回 |
| quick\_ratio                          | numpy.float64 | 速动比率               | 自选返回 |
| super\_quick\_ratio                   | numpy.float64 | 超速动比率              | 自选返回 |
| debt\_equity\_ratio                   | numpy.float64 | 产权比率（%）            | 自选返回 |
| sewmi\_to\_total\_liability           | numpy.float64 | 归属母公司股东的权益／负债合计（%） | 自选返回 |
| sewmi\_to\_interest\_bear\_debt       | numpy.float64 | 归属母公司股东的权益／带息债务（%） | 自选返回 |
| debt\_tangible\_equity\_ratio         | numpy.float64 | 有形净值债务率（%）         | 自选返回 |
| tangible\_a\_to\_interest\_bear\_debt | numpy.float64 | 有形净值／带息债务（%）       | 自选返回 |
| tangible\_a\_to\_net\_debt            | numpy.float64 | 有形净值／净债务（%）        | 自选返回 |
| ebitda\_to\_t\_liability              | numpy.float64 | 息税折旧摊销前利润／负债合计     | 自选返回 |
| nocf\_to\_t\_liability                | numpy.float64 | 经营活动产生现金流量净额/负债合计  | 自选返回 |
| nocf\_to\_interest\_bear\_debt        | numpy.float64 | 经营活动产生现金流量净额/带息债务  | 自选返回 |
| nocf\_to\_current\_liability          | numpy.float64 | 经营活动产生现金流量净额/流动负债  | 自选返回 |
| nocf\_to\_net\_debt                   | numpy.float64 | 经营活动产生现金流量净额/净债务   | 自选返回 |
| interest\_cover                       | numpy.float64 | 利息保障倍数（倍）          | 自选返回 |
| long\_debt\_to\_working\_capital      | numpy.float64 | 长期负债与营运资金比率        | 自选返回 |
| opercashinto\_current\_debt           | numpy.float64 | 现金流动负债比            | 自选返回 |

[]()[](#)
