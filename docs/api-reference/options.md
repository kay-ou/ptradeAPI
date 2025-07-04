# 期权交易API

本文档介绍期权交易相关的API函数，包括期权查询、交易、行权等功能。

## 期权查询函数

### get_opt_objects - 获取期权标的列表

```python
get_opt_objects(date=None)
```

#### 使用场景

该函数在研究、回测、交易模块可用

#### 接口说明

用于获取某日期的ETF期权标的，默认返回当前交易日的期权标的

#### 参数

date：查询日期，str类型，仅支持YYYYmmdd或者YYYY-mm-dd格式；

#### 返回

期权标的列表，list类型，调用异常返回[]

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 获取当前交易日的所有ETF期权标的列表
    opt_objects = get_opt_objects()
    log.info('期权标的: %s' % opt_objects)
    
    # 获取指定日期的期权标的列表
    opt_objects = get_opt_objects(date='20220703')
    log.info('2022-07-03期权标的: %s' % opt_objects)
```

### get_opt_last_dates - 获取期权标的到期日列表

```python
get_opt_last_dates(security, date=None)
```

#### 使用场景

该函数在研究、回测、交易模块可用

#### 接口说明

用于获取某日期的ETF期权标的到期日，默认返回当前交易日的到期日

#### 参数

security：查询标的，str类型，如'510050.SS'；

date：查询日期，str类型，仅支持YYYYmmdd或者YYYY-mm-dd格式；

#### 返回

期权标的到期日列表，list类型，调用异常返回[]

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 获取50ETF期权标的到期日列表
    last_dates = get_opt_last_dates('510050.SS')
    log.info('50ETF期权到期日: %s' % last_dates)
```

### get_opt_contracts - 获取期权标的对应合约列表

```python
get_opt_contracts(security, date=None)
```

#### 使用场景

该函数在研究、回测、交易模块可用

#### 接口说明

用于获取某期权标的某交易日处于挂牌期间的合约列表

#### 参数

security：查询标的，str类型，如'510050.SS'；

date：查询日期，str类型，仅支持YYYYmmdd或者YYYY-mm-dd格式；

#### 返回

期权标的合约列表，list类型，调用异常返回[]

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 获取50ETF期权标的对应的挂牌期合约列表
    contracts = get_opt_contracts('510050.SS')
    log.info('50ETF期权合约数量: %d' % len(contracts))
    log.info('前5个合约: %s' % contracts[:5])
```

### get_contract_info - 获取期权合约信息

```python
get_contract_info(contract)
```

#### 使用场景

该函数在研究、回测、交易模块可用

#### 接口说明

用于获取期权合约信息

#### 参数

contract：合约编号，str类型，如上证期权'10003975.XSHO'、深圳期权'90000961.XSZO'；

#### 返回

字典类型，主要返回的字段为:

- contract_code -- 合约代码，str类型；
- contract_name -- 合约名称，str类型；
- exchange -- 交易所：上交所、深交所，str类型；
- warrant_way -- 期权类型，10-欧式，20-美式，30-百慕大式，str类型；
- contract_multiplier -- 合约乘数，float类型；
- expiration_date -- 到期日，str类型；
- listing_date -- 上市日期，str类型；
- option_type -- 期权属性，'C'-看涨期权，'P'-看跌期权，str类型；
- trade_code -- 交易代码，str类型；
- littlest_changeunit -- 最小价格变动单位，float类型；
- exercise_price -- 行权价格，float类型；

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 获取期权合约的详细信息
    contract_info = get_contract_info('10003975.XSHO')
    log.info('合约名称: %s' % contract_info['contract_name'])
    log.info('行权价格: %.2f' % contract_info['exercise_price'])
    log.info('到期日: %s' % contract_info['expiration_date'])
    log.info('期权类型: %s' % contract_info['option_type'])
```

## 期权交易函数

### buy_open - 权利仓开仓

```python
buy_open(contract, amount, limit_price=None)
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

权利仓开仓（买入期权）

#### 参数

contract：期权合约代码(str)；

amount：交易数量，正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 买入开仓期权
    buy_open('10003975.XSHO', 1)
    # 指定价格买入开仓
    buy_open('10003975.XSHO', 1, limit_price=0.1)
```

### sell_close - 权利仓平仓

```python
sell_close(contract, amount, limit_price=None)
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

权利仓平仓（卖出期权）

#### 参数

contract：期权合约代码(str)；

amount：交易数量，正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 卖出平仓期权
    sell_close('10003975.XSHO', 1)
```

### sell_open - 义务仓开仓

```python
sell_open(contract, amount, limit_price=None)
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

义务仓开仓（卖出期权）

#### 参数

contract：期权合约代码(str)；

amount：交易数量，正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 卖出开仓期权
    sell_open('10003975.XSHO', 1)
```

### buy_close - 义务仓平仓

```python
buy_close(contract, amount, limit_price=None)
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

义务仓平仓（买入期权）

#### 参数

contract：期权合约代码(str)；

amount：交易数量，正数(int)；

limit_price：买卖限价(float)；

#### 返回

[Order对象](objects.md#Order)中的id或者None。如果创建订单成功，则返回Order对象的id，失败则返回None

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 买入平仓期权
    buy_close('10003975.XSHO', 1)
```

### option_exercise - 行权

```python
option_exercise(contract, amount)
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

期权行权

#### 参数

contract：期权合约代码(str)；

amount：行权数量，正数(int)；

#### 返回

None

#### 示例

```python
def initialize(context):
    pass

def handle_data(context, data):
    # 行权期权
    option_exercise('10003975.XSHO', 1)
```

## 期权策略示例

### 简单的期权买入策略

```python
def initialize(context):
    g.underlying = '510050.SS'  # 50ETF
    g.option_contract = None

def handle_data(context, data):
    # 获取期权合约列表
    contracts = get_opt_contracts(g.underlying)
    
    if contracts and not g.option_contract:
        # 选择第一个合约作为示例
        g.option_contract = contracts[0]
        
        # 获取合约信息
        contract_info = get_contract_info(g.option_contract)
        log.info('选择合约: %s' % contract_info['contract_name'])
        
        # 买入期权
        buy_open(g.option_contract, 1)
        log.info('买入期权')
    
    # 检查是否需要行权或平仓
    if g.option_contract:
        position = get_position(g.option_contract)
        if position.long_amount > 0:
            # 获取合约信息检查到期日
            contract_info = get_contract_info(g.option_contract)
            # 这里可以添加行权或平仓的逻辑
```

### 备兑开仓策略

```python
def initialize(context):
    g.underlying = '510050.SS'  # 50ETF
    g.option_contract = None

def handle_data(context, data):
    # 检查是否有足够的标的资产进行备兑
    lock_amount = get_covered_lock_amount(g.underlying)
    
    if lock_amount >= 10000:  # 假设需要1万份ETF
        # 获取看涨期权合约
        contracts = get_opt_contracts(g.underlying)
        
        # 筛选看涨期权
        for contract in contracts:
            contract_info = get_contract_info(contract)
            if contract_info['option_type'] == 'C':  # 看涨期权
                g.option_contract = contract
                break
        
        if g.option_contract:
            # 备兑锁定标的
            option_covered_lock(g.underlying, 10000)
            
            # 卖出看涨期权
            sell_open(g.option_contract, 1)
            log.info('备兑开仓')
```

## 注意事项

1. **权限要求**: 期权交易需要开通相应权限
2. **保证金要求**: 卖出期权需要缴纳保证金
3. **到期日管理**: 注意期权的到期日，及时处理持仓
4. **行权风险**: 卖出期权面临被行权的风险
5. **时间价值**: 期权具有时间价值，会随时间衰减
6. **波动率影响**: 期权价格受标的资产波动率影响较大

## 相关文档

- [股票交易API](stock-trading.md) - 股票交易功能
- [期货交易API](futures.md) - 期货交易功能
- [对象说明](objects.md) - Order、Position等对象详解
