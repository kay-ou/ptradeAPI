# 设置函数

本文档介绍用于配置策略参数的设置函数。

## set_universe - 设置股票池

```python
set_universe(security_list)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

该函数用于设置或者更新此策略要操作的股票池。

注意事项：

股票策略中，该函数只用于设定get_history函数的默认security_list入参, 除此之外并无其他用处，因此为非必须设定的函数。

### 参数

security_list: 股票列表，支持单支或者多支股票(list[str]/str)

### 返回

None

### 示例

```python
def initialize(context):
    g.security = ['600570.SS','600571.SS']
    # 将g.security中的股票设置为股票池
    set_universe(g.security)

def handle_data(context, data):
    # 获取初始化设定的股票池行情数据
    his = get_history(5, '1d', 'close', security_list=None)
```

## set_benchmark - 设置基准

```python
set_benchmark(sids)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

该函数用于设置策略的比较基准，前端展现的策略评价指标都基于此处设置的基准标的。

注意事项：

此函数只能在initialize使用。

### 参数

security：股票/指数/ETF代码(str)

### 默认设置

如果不做基准设置，默认选定沪深300指数(000300.SS)的每日价格作为判断策略好坏和一系列风险值计算的基准。如果要指定其他股票/指数/ETF的价格作为基准，就需要使用set_benchmark。

### 返回

None

### 示例

```python
def initialize(context):
    g.security = '000001.SZ'
    set_universe(g.security)
    #将上证50（000016.SS）设置为参考基准
    set_benchmark('000016.SS')

def handle_data(context, data):
    order('000001.SZ',100)
```

## set_commission - 设置佣金费率

```python
set_commission(commission_ratio=0.0003, min_commission=5.0, type="STOCK")
```

### 使用场景

该函数仅在回测模块可用

### 接口说明

该函数用于设置佣金费率。

注意事项：

关于回测手续费计算：手续费=佣金费+经手费

佣金费=佣金费率*交易总金额(若佣金费计算后小于设置的最低佣金，则佣金费取最小佣金)

经手费=经手费率(万分之0.487)*交易总金额

### 参数

commission_ratio：佣金费率，默认股票每笔交易的佣金费率是万分之三，ETF基金、LOF基金每笔交易的佣金费率是万分之八。(float)

min_commission：最低交易佣金，默认每笔交易最低扣5元佣金。(float)

type：交易类型，不传参默认为STOCK(目前只支持STOCK, ETF, LOF)。(string)

### 返回

None

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    #将佣金费率设置为万分之三，将最低手续费设置为3元
    set_commission(commission_ratio =0.0003, min_commission=3.0)

def handle_data(context, data):
    pass
```

## set_fixed_slippage - 设置固定滑点

```python
set_fixed_slippage(fixedslippage=0.0)
```

### 使用场景

该函数仅在回测模块可用

### 接口说明

该函数用于设置固定滑点，滑点在真实交易场景是不可避免的，因此回测中设置合理的滑点有利于让回测逼近真实场景。

### 参数

fixedslippage：固定滑点，委托价格与最后的成交价格的价差设置，这个价差是一个固定的值(比如0.02元，撮合成交时委托价格±0.01元)。最终的成交价格=委托价格±float(fixedslippage)/2。

### 返回

None

### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)
    # 将滑点设置为固定的0.2元，即原本买入交易的成交价为10元，则设置之后成交价将变成10.1元
    set_fixed_slippage(fixedslippage=0.2)

def handle_data(context, data):
    pass
```

## set_slippage - 设置滑点

```python
set_slippage(slippage=0.001)
```

### 使用场景

该函数仅在回测模块可用

### 接口说明

该函数用于设置滑点比例，滑点在真实交易场景是不可避免的，因此回测中设置合理的滑点有利于让回测逼近真实场景。

### 参数

slippage：滑点比例，委托价格与最后的成交价格的价差设置，这个价差是当时价格的一个百分比(比如设置0.002时，撮合成交时委托价格±当前周期价格*0.001)。最终成交价格=委托价格±委托价格*float(slippage)/2。

### 返回

None

### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)
    # 将滑点设置为0.002
    set_slippage(slippage=0.002)

def handle_data(context, data):
    pass
```
