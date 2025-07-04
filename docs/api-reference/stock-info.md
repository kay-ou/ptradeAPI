# 股票信息API

本文档介绍获取股票基础信息的API函数，包括股票名称、基础信息、状态、除权除息、板块信息等。

## get_stock_name - 获取股票名称

```python
get_stock_name(stocks)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该接口可获取股票、可转债、ETF等名称。

### 参数

stocks：股票代码(list[str]/str)；

### 返回

股票名称字典，dict类型，key为股票代码，value为股票名称，当没有查询到相关数据或者输入有误时value为None(dict[str:str])；

```python
{'600570.SS': '恒生电子'}
```

### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '600571.SS']
    set_universe(g.security)

def handle_data(context, data):
    #获取600570.SS股票名称
    stock_name = get_stock_name(g.security[0])
    log.info(stock_name)
    #获取股票池所有的股票名称
    stock_names = get_stock_name(g.security)
    log.info(stock_names)
```

## get_stock_info - 获取股票基础信息

```python
get_stock_info(stocks, field=None)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该接口可获取股票、可转债、ETF等基础信息。

注意事项：

field不做入参时默认只返回stock_name字段

### 参数

stocks：股票代码(list[str]/str)；

field：指明数据结果集中所支持输出字段(list[str]/str)，输出字段包括：

- stock_name -- 股票代码对应公司名(str:str)；
- listed_date -- 股票上市日期(str:str)；
- de_listed_date -- 股票退市日期，若未退市，返回2900-01-01(str:str)；

### 返回

嵌套dict类型，包含内容为field中指定内容，若field=None，返回股票基础信息仅包含对应公司名(dict[str:dict[str:str,...],...]）

```python
{'600570.SS': {'stock_name': '恒生电子', 'listed_date': '2003-12-16', 'de_listed_date': '2900-01-01'}}
```

### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '600571.SS']
    set_universe(g.security)

def handle_data(context, data):
    #获取单支股票的基础信息
    stock_info = get_stock_info(g.security[0])
    log.info(stock_info)
    #获取多支股票的基础信息
    stock_infos = get_stock_info(g.security, ['stock_name','listed_date','de_listed_date'])
    log.info(stock_infos)
```

## get_stock_status - 获取股票状态信息

```python
get_stock_status(stocks, query_type='ST', query_date=None)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该接口用于获取指定日期股票的ST、停牌、退市属性。

注意事项：

退市整理期股票不包含在退市状态内，可通过get_stock_name函数判断股票名称是否包含【退】确认退市整理期代码

### 参数

stocks: 例如 ['000001.SZ','000003.SZ']。该字段必须输入，否则返回None(list[str]/str)；

query_type: 支持以下三种类型属性的查询，默认为'ST'(str)；

具体支持输入的字段包括：

- 'ST' – 查询是否属于ST股票
- 'HALT' – 查询是否停牌
- 'DELISTING' – 查询是否退市

query_date: 格式为YYYYmmdd，默认为None,表示当前日期（回测为回测当前周期，研究与交易则取系统当前时间）(str)；

### 返回

返回dict类型，每支股票对应的值为True或False，当没有查询到相关数据或者输入有误时返回None(dict[str:bool,...])；

### 示例

```python
def initialize(context):
    g.security = ['600397.SS', '600701.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    stocks_list = g.security
    filter_stocks = []
    # 判断股票是否为ST、停牌或者退市的股票
    st_status = get_stock_status(stocks_list, 'ST')
    # 将不是ST的股票筛选出来
    for i in stocks_list:
        if st_status[i] is not True:
            filter_stocks.append(i)
    log.info('筛选不是ST的股票列表: %s' % filter_stocks)
```

## get_stock_exrights - 获取股票除权除息信息

```python
get_stock_exrights(stock_code, date=None)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该接口用于获取股票除权除息信息。

### 参数

stock_code; str类型, 股票代码(str)；

date: 查询该日期的除权除息信息，默认获取该股票历史上所有除权除息信息，e.g. '20180228'/20180228/datetime.date(2018,2,28)(str/int/datetime.date)

### 返回

输入日期若没有除权除息信息则返回None,有相关数据则返回pandas.DataFrame类型数据

返回结果字段介绍：

- date -- 日期(索引列，类型为int64)；
- allotted_ps -- 每股送股(str:numpy.float64)；
- rationed_ps -- 每股配股(str:numpy.float64)；
- rationed_px -- 配股价(str:numpy.float64)；
- bonus_ps -- 每股分红(str:numpy.float64)；
- exer_forward_a -- 前复权除权因子A；用于计算前复权价格(前复权价格=A*价格+B)(str:numpy.float64)
- exer_forward_b -- 前复权除权因子B；用于计算前复权价格(前复权价格=A*价格+B)(str:numpy.float64)
- exer_backward_a -- 后复权除权因子A；用于计算后复权价格(后复权价格=A*价格+B)(str:numpy.float64)
- exer_backward_b -- 后复权除权因子B；用于计算后复权价格(后复权价格=A*价格+B)(str:numpy.float64)

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    stock_exrights = get_stock_exrights(g.security)
    log.info('the stock exrights info of security %s:\n%s' % (g.security, stock_exrights))
```

## get_stock_blocks - 获取股票所属板块信息

```python
get_stock_blocks(stock_code)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该接口用于获取股票所属板块。

注意事项：

该函数获取的是当下的数据，因此回测不能取到真正匹配回测日期的数据，注意未来函数

已退市股票无法成功获取数据，接口会返回None

### 参数

stock_code: 股票代码(str)；

### 返回

获取成功返回dict类型，包含所属行业、板块等详细信息(dict[str:list[list[str,str],...],...]），获取失败返回None。

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    blocks = get_stock_blocks(g.security)
    log.info('security %s in these blocks:\n%s' % (g.security, blocks))
```

## get_index_stocks - 获取指数成分股

```python
get_index_stocks(index_code, date)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该接口用于获取一个指数在平台可交易的成分股列表。

注意事项：

1. 在回测中，date不入参默认取当前回测周期所属历史日期
2. 在研究中，date不入参默认取的是当前日期
3. 在交易中，date不入参默认取的是当前日期

### 参数

index_code：指数代码，尾缀必须是.SS 如沪深300：000300.SS(str)

date：日期，输入形式必须为'YYYYMMDD'，如'20170620'，不输入默认为当前日期(str)；

### 返回

返回股票代码的list(list[str,...])。

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def before_trading_start(context, data):
    # 获取当前所有沪深300的股票
    g.stocks = get_index_stocks('000300.XBHS')
    log.info(g.stocks)
    # 获取2016年6月20日所有沪深300的股票, 设为股票池
    g.stocks = get_index_stocks('000300.XBHS','20160620')
    set_universe(g.stocks)
    log.info(g.stocks)

def handle_data(context, data):
    pass
```

## get_industry_stocks - 获取行业成份股

```python
get_industry_stocks(industry_code)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该接口用于获取一个行业的所有股票。

注意事项：

该函数获取的是当下的数据，因此回测不能取到真正匹配回测日期的数据，注意未来函数

### 参数

industry_code: 行业编码，尾缀必须是.XBHS 如农业股：A01000.XBHS(str)

### 返回

返回股票代码的list(list[str,...])。

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def before_trading_start(context, data):
    # 获取农业行业的所有股票
    industry_stocks = get_industry_stocks('A01000.XBHS')
    log.info(industry_stocks)

def handle_data(context, data):
    pass
```

## 相关文档

- [基础信息API](basic-info.md) - 获取交易日期、市场信息
- [行情数据API](market-data.md) - 获取历史和实时行情数据
- [股票交易API](stock-trading.md) - 股票交易相关功能
