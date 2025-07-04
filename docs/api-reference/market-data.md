# 行情数据API

本文档介绍获取行情数据的API函数，包括历史行情、实时行情、逐笔数据等。

## get_history - 获取历史行情

```python
get_history(count, frequency='1d', field='close', security_list=None, fq=None, include=False, fill='nan', is_dict=False)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

该接口用于获取最近N条历史行情K线数据。支持多股票、多行情字段获取。

注意事项：

该接口只能获取2005年后的数据。

针对停牌场景，我们没有跳过停牌的日期，无论对单只股票还是多只股票进行调用，时间轴均为二级市场交易日日历，停牌时使用停牌前的数据填充，成交量为0，日K线可使用成交量为0的逻辑进行停牌日过滤。

### 参数

count： K线数量，大于0，返回指定数量的K线行情；必填参数；入参类型：int；

frequency：K线周期，现有支持1分钟线(1m)、5分钟线(5m)、15分钟线(15m)、30分钟线(30m)、60分钟线(60m)、120分钟线(120m)、日线(1d)、周线(1w/weekly)、月线(mo/monthly)、季度线(1q/quarter)和年线(1y/yearly)频率的数据；选填参数，默认为'1d'；入参类型：str；

field：指明数据结果集中所支持输出的行情字段；选填参数，默认为['open','high','low','close','volume','money','price']；入参类型：list[str,str]或str；输出字段包括：

- open -- 开盘价，字段返回类型：numpy.float64；
- high -- 最高价，字段返回类型：numpy.float64；
- low --最低价，字段返回类型：numpy.float64；
- close -- 收盘价，字段返回类型：numpy.float64；
- volume -- 交易量，字段返回类型：numpy.float64；
- money -- 交易金额，字段返回类型：numpy.float64；
- price -- 最新价，字段返回类型：numpy.float64；
- preclose -- 昨收盘价，字段返回类型：numpy.float64(仅日线返回)；
- high_limit -- 涨停价，字段返回类型：numpy.float64(仅日线返回)；
- low_limit -- 跌停价，字段返回类型：numpy.float64(仅日线返回)；
- unlimited -- 判断查询日是否是无涨跌停限制(1:该日无涨跌停限制;0:该日不是无涨跌停限制)，字段返回类型：numpy.float64(仅日线返回)；

security_list：要获取数据的股票列表；选填参数，None表示在上下文中的universe中选中的所有股票；入参类型：list[str,str]或str；

fq：数据复权选项，支持包括，pre-前复权，post-后复权，dypre-动态前复权，None-不复权；选填参数，默认为None；入参类型：str；

include：是否包含当前周期，True –包含，False-不包含；选填参数，默认为False；入参类型：bool；

fill：行情获取不到某一时刻的分钟数据时，是否用上一分钟的数据进行填充该时刻数据，'pre'–用上一分钟数据填充，'nan'–NaN进行填充(仅交易有效)；选填参数，默认为'nan'；入参类型：str；

is_dict：返回是否是字典(dict)格式{str: array()}，True –是，False-不是；选填参数，默认为False；返回为字典格式取数速度相对较快；入参类型：bool；

### 返回

根据不同的输入参数，返回不同格式的数据：

1. **单支股票**：返回pandas.DataFrame对象，行索引是datetime.datetime对象，列索引是行情字段
2. **多支股票+单个字段**：返回pandas.DataFrame对象，行索引是datetime.datetime对象，列索引是股票代码
3. **多支股票+多个字段**：返回pandas.Panel对象，items索引是行情字段

### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    # 获取股票池中全部股票过去5天的每日收盘价
    his = get_history(5, '1d', 'close', security_list=g.security)
    log.info(his)
    
    # 获取恒生电子的过去5天的每天的收盘价
    his2 = get_history(5, '1d', 'close', security_list='600570.SS')
    log.info(his2)
    
    # 获取恒生电子的过去5天的每天的后复权收盘价
    his3 = get_history(5, '1d', 'close', security_list='600570.SS', fq='post')
    log.info(his3)
```

## get_price - 获取历史数据

```python
get_price(security, start_date=None, end_date=None, frequency='1d', fields=None, fq=None, count=None)
```

### 使用场景

该函数在研究、回测、交易模块可用

### 接口说明

该接口用于获取指定日期的前N条的历史行情K线数据或者指定时间段内的历史行情K线数据。支持多股票、多行情字段获取。

注意事项：

1. start_date与count必须且只能选择输入一个，不能同时输入或者同时都不输入。
2. 针对停牌场景，我们没有跳过停牌的日期，无论对单只股票还是多只股票进行调用，时间轴均为二级市场交易日日历，停牌时使用停牌前的数据填充，成交量为0，日K线可使用成交量为0的逻辑进行停牌日过滤。
3. 数据返回内容不包括当天数据。
4. 该接口只能获取2005年后的数据。

### 参数

security：一支股票代码或者一个股票代码的list(list[str]/str)

start_date：开始时间，默认为空。传入格式仅支持：YYYYmmdd、YYYY-mm-dd、YYYY-mm-dd HH:MM、YYYYmmddHHMM，如'20150601'、'2015-06-01'、'2015-06-01 10:00'、'201506011000'(str)；

end_date：结束时间，默认为空，传入格式仅支持：YYYYmmdd、YYYY-mm-dd、YYYY-mm-dd HH:MM、YYYYmmddHHMM，如'20150601'、'2015-06-01'、'2015-06-01 14:00'、'201506011400'(str)；

frequency： 单位时间长度，现有支持1分钟线(1m)、5分钟线(5m)、15分钟线(15m)、30分钟线(30m)、60分钟线(60m)、120分钟线(120m)、日线(1d)、周线(1w/weekly)、月线(mo/monthly)、季度线(1q/quarter)和年线(1y/yearly)频率数据(str)；

fields：指明数据结果集中所支持输出字段(list[str]/str)，输出字段包括：

- open -- 开盘价(str:numpy.float64)；
- high -- 最高价(str:numpy.float64)；
- low --最低价(str:numpy.float64)；
- close -- 收盘价(str:numpy.float64)；
- volume -- 交易量(str:numpy.float64)；
- money -- 交易金额(str:numpy.float64)；
- price -- 最新价(str:numpy.float64)；
- preclose -- 昨收盘价(str:numpy.float64)(仅日线返回)；
- high_limit -- 涨停价(str:numpy.float64)(仅日线返回)；
- low_limit -- 跌停价(str:numpy.float64)(仅日线返回)；
- unlimited -- 判断查询日是否无涨跌停限制(1：该日无涨跌停限制；0：该日有涨跌停限制)(str:numpy.float64)(仅日线返回)；

fq：数据复权选项，支持包括，pre-前复权，post-后复权，None-不复权(str)；

count：大于0，不能与start_date同时输入，获取end_date前count根的数据(int)；

### 返回

返回数据规则与get_history一致，根据输入参数返回不同格式的数据。

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 获得600570.SS(恒生电子)的2015年01月的天数据，只获取open字段
    price_open = get_price('600570.SS', start_date='20150101', end_date='20150131', frequency='1d')['open']
    log.info(price_open)
    
    # 获取指定结束日期前count天到结束日期的所有开盘数据
    price_open = get_price('600570.SS', end_date='20150131', frequency='daily', count=10)['open']
    log.info(price_open)
```

## 实时行情API

### get_snapshot - 取行情快照

```python
get_snapshot(security_list)
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

该函数用于获取指定股票的实时行情快照数据。

#### 参数

security_list：股票代码列表或单个股票代码(list[str]/str)

#### 返回

字典格式的实时行情数据，包含最新价、买卖档位、成交量等信息

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 获取实时行情快照
    snapshot = get_snapshot(g.security)
    price = snapshot[g.security]['last_px']
    log.info('当前价格: %s' % price)
```

## 相关文档

- [基础信息API](basic-info.md) - 获取交易日期、市场信息
- [股票信息API](stock-info.md) - 获取股票基础信息
- [股票交易API](stock-trading.md) - 股票交易相关功能
