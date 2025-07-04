# 对象说明

本文档介绍 Ptrade API 中的主要对象类型，包括全局对象、上下文对象、持仓对象等。

## g - 全局对象

### 使用场景

该对象仅支持回测、交易模块

### 对象说明

全局对象g，用于存储用户的各类可被不同函数（包括自定义函数）调用的全局数据，如：

```python
g.security = None  # 股票池
g.count = 0        # 计数器
g.flag = False     # 标志位
```

### 注意事项

1. 全局变量g中以'__'开头的变量为私有变量，持久化时将不会被保存
2. 涉及到IO(打开的文件，实例化的类对象等)的对象是不能被序列化的
3. 全局变量g中不能被序列化的变量将不会被保存

### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    g.count = 1
    g.flag = 0
    g.ma_short = 5
    g.ma_long = 20
    set_universe(g.security)

def handle_data(context, data):
    log.info(g.security)
    log.info(g.count)
    log.info(g.flag)
    
    # 使用全局变量进行计算
    hist = get_history(g.ma_long, '1d', 'close', g.security)
    ma_short = hist['close'][-g.ma_short:].mean()
    ma_long = hist['close'][-g.ma_long:].mean()
```

## Context - 上下文对象

### 使用场景

该对象仅支持回测、交易模块

### 对象说明

类型为业务上下文对象，包含策略运行的各种上下文信息

### 内容

```python
capital_base -- 起始资金
previous_date -- 前一个交易日
sim_params -- SimulationParameters对象
    capital_base -- 起始资金
    data_frequency -- 数据频率
portfolio -- 账户信息，可参考Portfolio对象
initialized -- 是否执行初始化
slippage -- 滑点，VolumeShareSlippage对象
    volume_limit -- 成交限量
    price_impact -- 价格影响力
commission -- 佣金费用，Commission对象
    tax -- 印花税费率
    cost -- 佣金费率
    min_trade_cost -- 最小佣金
blotter -- Blotter对象（记录）
    current_dt -- 当前单位时间的开始时间，datetime.datetime对象（北京时间）
recorded_vars -- 收益曲线值
```

### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    # 获得当前回测相关时间
    pre_date = context.previous_date
    log.info('前一交易日: %s' % pre_date)
    
    # 获取当前时间的各个部分
    current_time = context.blotter.current_dt
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    
    # 得到"年-月-日"格式
    date = current_time.strftime("%Y-%m-%d")
    log.info('当前日期: %s' % date)
    
    # 得到周几
    weekday = current_time.isoweekday()
    log.info('星期: %d' % weekday)
    
    # 获取账户信息
    cash = context.portfolio.cash
    total_value = context.portfolio.portfolio_value
    log.info('可用资金: %.2f, 总资产: %.2f' % (cash, total_value))
```

## SecurityUnitData - 证券单位数据

### 使用场景

该对象仅支持回测、交易模块

### 对象说明

一个单位时间内的股票的数据，是一个字典，根据股票代码获取BarData对象数据

### 基本属性

以下属性也能通过get_history/get_price获取到

```python
dt -- 时间
open -- 时间段开始时价格
close -- 时间段结束时价格
price -- 结束时价格
low -- 最低价
high -- 最高价
volume -- 成交的股票数量
money -- 成交的金额
```

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 获取当前股票的数据
    stock_data = data[g.security]
    
    log.info('开盘价: %.2f' % stock_data['open'])
    log.info('收盘价: %.2f' % stock_data['close'])
    log.info('最高价: %.2f' % stock_data['high'])
    log.info('最低价: %.2f' % stock_data['low'])
    log.info('成交量: %d' % stock_data['volume'])
    log.info('成交金额: %.2f' % stock_data['money'])
```

## Portfolio - 投资组合对象

### 使用场景

该对象仅支持回测、交易模块

### 对象说明

对象数据包含账户当前的资金，标的信息，即所有标的操作仓位的信息汇总

### 内容

#### 股票账户返回

```python
cash -- 当前可用资金（不包含冻结资金）
positions -- 当前持有的标的(包含不可卖出的标的)，dict类型，key是标的代码，value是Position对象
portfolio_value -- 当前持有的标的和现金的总价值
positions_value -- 持仓价值
capital_used -- 已使用的现金
returns -- 当前的收益比例, 相对于初始资金
pnl -- 当前账户总资产-初始账户总资产
start_date -- 开始时间
```

#### 期货账户返回

```python
cash -- 当前可用资金（不包含冻结资金）
positions -- 当前持有的标的(包含不可卖出的标的)，dict类型，key是标的代码，value是Position对象
portfolio_value -- 当前持有的标的和现金的总价值
positions_value -- 持仓价值
capital_used -- 已使用的现金
returns -- 当前的收益比例, 相对于初始资金
pnl -- 当前账户总资产-初始账户总资产
start_date -- 开始时间
```

#### 期权账户返回

```python
cash -- 当前可用资金（不包含冻结资金）
positions -- 当前持有的标的(包含不可卖出的标的)，dict类型，key是标的代码，value是Position对象
portfolio_value -- 当前持有的标的和现金的总价值
positions_value -- 持仓价值
returns -- 当前的收益比例, 相对于初始资金
pnl -- 当前账户总资产-初始账户总资产
margin -- 保证金
risk_degree -- 风险度
start_date -- 开始时间
```

### 示例

```python
def initialize(context):
    g.security = "600570.SS"
    set_universe([g.security])

def handle_data(context, data):
    portfolio = context.portfolio
    
    log.info('总资产: %.2f' % portfolio.portfolio_value)
    log.info('可用资金: %.2f' % portfolio.cash)
    log.info('持仓价值: %.2f' % portfolio.positions_value)
    log.info('收益率: %.2f%%' % (portfolio.returns * 100))
    log.info('盈亏: %.2f' % portfolio.pnl)
    
    # 检查是否有持仓
    if g.security in portfolio.positions:
        position = portfolio.positions[g.security]
        log.info('持仓数量: %d' % position.amount)
```

## Position - 持仓对象

### 使用场景

该对象仅支持回测、交易模块

### 对象说明

持有的某个标的的信息

### 注意事项

- 期货业务持仓把单个合约的持仓分为了多头仓(long)、空头仓(short)
- 期权业务持仓把单个合约的持仓分为了权利仓(long)、义务仓(short)、备兑仓(covered)

### 内容

#### 股票账户返回

```python
sid -- 标的代码
enable_amount -- 可用数量
amount -- 总持仓数量
last_sale_price -- 最新价格
cost_basis -- 持仓成本价格
today_amount -- 今日开仓数量(且仅回测有效)
business_type -- 持仓类型
```

#### 期货账户返回

```python
sid -- 标的代码
short_enable_amount -- 空头仓可用数量
long_enable_amount -- 多头仓可用数量
today_short_amount -- 空头仓今仓数量
today_long_amount -- 多头仓今仓数量
long_cost_basis -- 多头仓持仓成本
short_cost_basis -- 空头仓持仓成本
long_amount -- 多头仓总持仓量
short_amount -- 空头仓总持仓量
long_pnl -- 多头仓浮动盈亏
short_pnl -- 空头仓浮动盈亏
amount -- 总持仓数量
enable_amount -- 可用数量
last_sale_price -- 最新价格
business_type -- 持仓类型
delivery_date -- 交割日，期货使用
margin_rate -- 保证金比例
contract_multiplier -- 合约乘数
```

#### 期权账户返回

```python
sid -- 标的代码
short_enable_amount -- 义务仓可用数量
long_enable_amount -- 权利仓可用数量
covered_enable_amount -- 备兑仓可用数量
short_cost_basis -- 义务仓持仓成本
long_cost_basis -- 权利仓持仓成本
covered_cost_basis -- 备兑仓持仓成本
short_amount -- 义务仓总持仓量
long_amount -- 权利仓总持仓量
covered_amount -- 备兑仓总持仓量
short_pnl -- 义务仓浮动盈亏
long_pnl -- 权利仓浮动盈亏
covered_pnl -- 备兑仓浮动盈亏
last_sale_price -- 最新价格
margin -- 保证金
exercise_date -- 行权日，期权使用
business_type -- 持仓类型
```

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    order(g.security, 1000)
    position = get_position(g.security)
    
    if position.amount > 0:
        log.info('股票代码: %s' % position.sid)
        log.info('持仓数量: %d' % position.amount)
        log.info('可用数量: %d' % position.enable_amount)
        log.info('成本价: %.2f' % position.cost_basis)
        log.info('最新价: %.2f' % position.last_sale_price)
        
        # 计算盈亏
        profit = (position.last_sale_price - position.cost_basis) * position.amount
        log.info('浮动盈亏: %.2f' % profit)
```

## Order - 订单对象

### 使用场景

该对象仅支持回测、交易模块

### 对象说明

买卖订单信息

### 内容

```python
id -- 订单号
dt -- 订单产生时间，datetime.datetime类型
limit -- 指定价格
symbol -- 标的代码(备注：标的代码尾缀为四位，上证为XSHG，深圳为XSHE)
amount -- 下单数量，买入是正数，卖出是负数
created -- 订单生成时间，datetime.datetime类型
filled -- 成交数量，买入时为正数，卖出时为负数
entrust_no -- 委托编号
priceGear -- 盘口档位
status -- 订单状态(str)，该字段取值范围：
    '0' -- "未报"
    '1' -- "待报"
    '2' -- "已报"
    '3' -- "已报待撤"
    '4' -- "部成待撤"
    '5' -- "部撤"
    '6' -- "已撤"
    '7' -- "部成"
    '8' -- "已成"
    '9' -- "废单"
    '+' -- "已受理"
    '-' -- "已确认"
    'V' -- "已确认"
```

### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 下单
    order_id = order(g.security, 100)
    
    # 获取订单信息
    if order_id:
        order_obj = get_order(order_id)
        log.info('订单ID: %s' % order_obj.id)
        log.info('股票代码: %s' % order_obj.symbol)
        log.info('下单数量: %d' % order_obj.amount)
        log.info('订单状态: %s' % order_obj.status)
        log.info('成交数量: %d' % order_obj.filled)
        
        # 检查订单状态
        if order_obj.status == '8':  # 已成交
            log.info('订单已完全成交')
        elif order_obj.status == '7':  # 部分成交
            log.info('订单部分成交')
```

## 相关文档

- [策略引擎框架](framework.md) - 了解如何在策略中使用这些对象
- [股票交易API](stock-trading.md) - 查看交易相关的函数
- [工具函数API](utilities.md) - 其他实用工具函数
