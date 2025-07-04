# 融资融券API

本文档介绍融资融券交易相关的API函数，包括担保品买卖、融资买入、融券卖出等功能。

## 担保品交易

### margin_trade - 担保品买卖

```python
margin_trade(security, amount, limit_price=None, market_type=None)
```

#### 使用场景

该函数仅支持Ptrade客户端可用，仅在两融回测、两融交易模块可用

#### 接口说明

该接口用于担保品买卖。

注意事项：

1. 限价和市价委托类型都不传时默认取当前最新价进行限价委托，限价和市价委托类型都传入时以limit_price为委托限价进行市价委托。
2. 当market_type传入且委托上证股票时，limit_price为保护限价字段，必传字段。

#### 参数

security：股票代码(str)；

amount：交易数量(int)，正数表示买入，负数表示卖出；

limit_price：买卖限价/保护限价(float)；

market_type：市价委托类型(int)，上证股票支持参数0、1、2、4，深证股票支持参数0、2、3、4、5；

市价委托类型说明：
- 0：对手方最优价格；
- 1：最优五档即时成交剩余转限价；
- 2：本方最优价格；
- 3：即时成交剩余撤销；
- 4：最优五档即时成交剩余撤销；
- 5：全额成交或撤单；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)

#### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def before_trading_start(context, data):
    g.flag = False

def handle_data(context, data):
    if not g.flag:
        # 以系统最新价委托
        margin_trade(g.security, 100)
        # 以46块价格下一个限价单
        margin_trade(g.security, 100, limit_price=46)

        # 以46保护限价按最优五档即时成交剩余转限价买入100股
        margin_trade(g.security, 100, limit_price=46, market_type=1)
        # 按全额成交或撤单买入100股
        margin_trade("000001.SZ", 100, market_type=5)
        g.flag = True
```

## 融资交易

### margincash_open - 融资买入

```python
margincash_open(security, amount, limit_price=None, market_type=None)
```

#### 使用场景

该函数仅支持Ptrade客户端可用，仅在两融交易模块可用

#### 接口说明

该接口用于融资买入。

注意事项：

1. 限价和市价委托类型都不传时默认取当前最新价进行限价委托，限价和市价委托类型都传入时以limit_price为委托限价进行市价委托。
2. 当market_type传入且委托上证股票时，limit_price为保护限价字段，必传字段。

#### 参数

security：股票代码(str)；

amount：交易数量，输入正数(int)；

limit_price：买卖限价(float)；

market_type：市价委托类型(int)，上证股票支持参数0、1、2、4，深证股票支持参数0、2、3、4、5；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)

#### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)

def handle_data(context, data):
    # 融资买入100股
    margincash_open(g.security, 100)
    # 以指定价格融资买入
    margincash_open(g.security, 100, limit_price=46)
```

### margincash_close - 卖券还款

```python
margincash_close(security, amount, limit_price=None)
```

#### 使用场景

该函数仅支持Ptrade客户端可用，仅在两融交易模块可用

#### 接口说明

该接口用于卖券还款。

#### 参数

security：股票代码(str)；

amount：交易数量，输入正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 卖100股还款
    margincash_close(g.security, 100)
```

### margincash_direct_refund - 直接还款

```python
margincash_direct_refund(value)
```

#### 使用场景

该函数仅支持Ptrade客户端可用，仅在两融交易模块可用

#### 接口说明

该接口用于直接还款。

#### 参数

value：还款金额(float)；

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 获取负债总额
    fin_compact_balance = get_margin_assert().get('fin_compact_balance')
    # 还款
    margincash_direct_refund(fin_compact_balance)
```

## 融券交易

### marginsec_open - 融券卖出

```python
marginsec_open(security, amount, limit_price=None)
```

#### 使用场景

该函数仅支持Ptrade客户端可用，仅在两融交易模块可用

#### 接口说明

该接口用于融券卖出。

#### 参数

security：股票代码(str)；

amount：交易数量，输入正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)

#### 示例

```python
def initialize(context):
    g.security = '600030.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 融券卖出100股
    marginsec_open(g.security, 100)
```

### marginsec_close - 买券还券

```python
marginsec_close(security, amount, limit_price=None)
```

#### 使用场景

该函数仅支持Ptrade客户端可用，仅在两融交易模块可用

#### 接口说明

该接口用于买券还券。

#### 参数

security：股票代码(str)；

amount：交易数量，输入正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None(str)

#### 示例

```python
def initialize(context):
    g.security = '600030.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 买券还券100股
    marginsec_close(g.security, 100)
```

## 融资融券策略示例

### 双均线融资融券策略

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 获取历史数据
    hist = get_history(20, '1d', 'close', g.security)
    
    # 计算移动平均线
    ma5 = hist['close'][-5:].mean()
    ma10 = hist['close'][-10:].mean()
    
    # 获取当前持仓
    position = get_position(g.security)
    
    # 多头信号：5日均线上穿10日均线
    if ma5 > ma10 and position.amount <= 0:
        if position.amount < 0:
            # 先平空头仓位
            marginsec_close(g.security, abs(position.amount))
            log.info('平空头仓位')
        # 融资买入
        margincash_open(g.security, 1000)
        log.info('融资买入')
    
    # 空头信号：5日均线下穿10日均线
    elif ma5 < ma10 and position.amount >= 0:
        if position.amount > 0:
            # 先平多头仓位
            margincash_close(g.security, position.amount)
            log.info('平多头仓位')
        # 融券卖出
        marginsec_open(g.security, 1000)
        log.info('融券卖出')
```

## 注意事项

1. **权限要求**: 融资融券交易需要开通相应权限
2. **保证金要求**: 需要维持足够的保证金比例
3. **风险控制**: 注意控制杠杆比例，避免强制平仓
4. **费用成本**: 融资融券有利息和费用成本
5. **市场限制**: 部分股票可能不支持融资融券交易

## 相关文档

- [股票交易API](stock-trading.md) - 普通股票交易功能
- [对象说明](objects.md) - Order、Position等对象详解
- [策略示例](../getting-started/examples.md) - 更多策略示例
