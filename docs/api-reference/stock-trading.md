# 股票交易API

本文档介绍股票交易相关的API函数，包括下单、撤单、查询持仓等功能。

## 基础交易函数

### order - 按数量买卖

```python
order(security, amount, limit_price=None)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于买卖指定数量为amount的股票，同时支持国债逆回购

注意事项：

1. 支持交易场景的逆回购交易。委托方向为卖出(amount必须为负数)，逆回购最小申购金额为1000元(10张)，因此本接口amount入参应大于等于10(10张)，否则会导致委托失败。
2. 回测场景，amount有最小下单数量校验，股票、ETF、LOF：100股，可转债：10张；交易场景接口不做amount校验，直接报柜台。
3. 交易场景如果limit_price字段不入参，系统会默认用行情快照数据最新价报单，假如行情快照获取失败会导致委托失败，系统会在日志中增加提醒。

#### 参数

security: 股票代码(str)；

amount: 交易数量，正数表示买入，负数表示卖出(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)。

#### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    #以系统最新价委托
    order('600570.SS', 100)
    # 逆回购1000元
    order('131810.SZ', -10)
    #以39块价格下一个限价单
    order('600570.SS', 100, limit_price=39)
```

### order_target - 指定目标数量买卖

```python
order_target(security, amount, limit_price=None)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于买卖股票，直到股票最终数量达到指定的amount

注意事项：

1. 该函数不支持逆回购交易。
2. 该函数在委托股票时取整100股，委托可转债时取整10张。
3. 交易场景如果limit_price字段不入参，系统会默认用行情快照数据最新价报单，假如行情快照获取失败会导致委托失败，系统会在日志中增加提醒。
4. 因可能造成重复下单，因此建议在交易中谨慎使用该接口。

#### 参数

security: 股票代码(str)；

amount: 期望的最终数量(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)。

#### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    #买卖恒生电子股票数量到100股
    order_target('600570.SS', 100)
    #卖出恒生电子所有股票
    if data['600570.SS']['close'] > 39:
        order_target('600570.SS', 0)
```

### order_value - 指定目标价值买卖

```python
order_value(security, value, limit_price=None)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于买卖指定价值为value的股票

注意事项：

1. 该函数不支持逆回购交易。
2. 该函数在委托股票时取整100股，委托可转债时取整10张。
3. 交易场景如果limit_price字段不入参，系统会默认用行情快照数据最新价报单，假如行情快照获取失败会导致委托失败，系统会在日志中增加提醒。

#### 参数

security：股票代码(str)；

value：股票价值(float)

limit_price：买卖限价(float)

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)。

#### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    #买入价值为10000元的恒生电子股票
    order_value('600570.SS', 10000)

    if data['600570.SS']['close'] > 39:
        #卖出价值为10000元的恒生电子股票
        order_value('600570.SS', -10000)
```

### order_target_value - 指定持仓市值买卖

```python
order_target_value(security, value, limit_price=None)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于调整股票持仓市值到value价值

注意事项：

1. 该函数不支持逆回购交易。
2. 该函数在委托股票时取整100股，委托可转债时取整10张。
3. 交易场景如果limit_price字段不入参，系统会默认用行情快照数据最新价报单，假如行情快照获取失败会导致委托失败，系统会在日志中增加提醒。
4. 因可能造成重复下单，因此建议在交易中谨慎使用该接口。

#### 参数

security: 股票代码(str)；

value: 期望的股票最终价值(float)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)。

#### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    #买卖股票到指定价值
    order_target_value('600570.SS', 10000)

    #卖出当前所有恒生电子的股票
    if data['600570.SS']['close'] > 39:
        order_target_value('600570.SS', 0)
```

### order_market - 按市价进行委托

```python
order_market(security, amount, market_type, limit_price=None)
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

该接口用于使用多种市价类型进行委托

注意事项：

1. 支持逆回购交易。委托方向为卖出(amount必须为负数)，逆回购最小申购金额为1000元(10张)，因此本接口amount入参应大于等于10(10张)，否则会导致委托失败。
2. 不支持可转债交易.
3. 该函数中market_type是必传字段，如不传入参数会出现报错。
4. 该函数委托上证股票时limit_price是必传字段，如不传入参数会出现报错。

#### 参数

security：股票代码(str)；

amount：交易数量(int)，正数表示买入，负数表示卖出；

market_type：市价委托类型(int)，上证股票支持参数0、1、2、4，深证股票支持参数0、2、3、4、5，必传参数；

limit_price：保护限价(float)，委托上证股票时必传参数；

市价委托类型说明：
- 0：对手方最优价格；
- 1：最优五档即时成交剩余转限价；
- 2：本方最优价格；
- 3：即时成交剩余撤销；
- 4：最优五档即时成交剩余撤销；
- 5：全额成交或撤单；

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def handle_data(context, data):
    # 以35保护限价按对手方最优价格买入100股
    order_market(g.security, 100, 0, 35)
    # 按对手方最优价格买入100股
    order_market("000001.SZ", 100, 0)
```

## 查询函数

### get_position - 获取持仓信息

```python
get_position(security)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于获取某只股票的持仓信息

#### 参数

security: 股票代码(str)

#### 返回

[Position对象](objects.md#Position)，包含持仓数量、成本等信息

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    position = get_position(g.security)
    log.info('持仓数量: %d' % position.amount)
```

### get_positions - 获取多支股票持仓信息

```python
get_positions()
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于获取所有股票的持仓信息

#### 参数

无

#### 返回

字典类型，key为股票代码，value为[Position对象](objects.md#Position)

#### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    positions = get_positions()
    for stock, pos in positions.items():
        log.info('%s 持仓: %d' % (stock, pos.amount))
```

### cancel_order - 撤单

```python
cancel_order(order_id)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于撤销指定的订单

#### 参数

order_id: 订单ID(str)

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 下单后获取订单ID
    order_id = order(g.security, 100)
    # 撤销订单
    if order_id:
        cancel_order(order_id)
```

## 相关文档

- [基础信息API](basic-info.md) - 获取交易日期、市场信息
- [行情数据API](market-data.md) - 获取历史和实时行情数据
- [股票信息API](stock-info.md) - 获取股票基础信息
- [对象说明](objects.md) - Context、Portfolio、Order等对象详解
