# 策略引擎框架

## 业务流程框架

ptrade量化引擎以事件触发为基础，通过初始化事件（initialize）、盘前事件（before_trading_start）、盘中事件（handle_data）、盘后事件（after_trading_end）来完成每个交易日的策略任务。

initialize和handle_data是一个允许运行策略的最基础结构，也就是必选项，before_trading_start和after_trading_end是可以按需运行的。

handle_data仅满足日线和分钟级别的盘中处理，tick级别的盘中处理则需要通过tick_data或者run_interval来实现。

ptrade还支持委托主推事件（on_order_response）、交易主推事件（on_trade_response），可以通过委托和成交的信息来处理策略逻辑，是tick级的一个补充。

除了以上的一些事件以外，ptrade也支持通过定时任务来运行策略逻辑，可以通过run_daily接口实现。

![](https://converturltomd.com/static/images/help/BizFrame.png)
<!-- Image marked for download -->

## initialize（必选）

```python
initialize(context)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

该函数用于初始化一些全局变量，是策略运行的唯二必须定义函数之一。

注意事项：

该函数只会在回测和交易启动的时候运行一次

### 可调用接口

- [set_universe(回测/交易)](settings.md#set_universe)
- [set_benchmark(回测/交易)](settings.md#set_benchmark)
- [set_commission(回测)](settings.md#set_commission)
- [set_fixed_slippage(回测)](settings.md#set_fixed_slippage)
- [set_slippage(回测)](settings.md#set_slippage)
- [set_volume_ratio(回测)](settings.md#set_volume_ratio)
- [set_limit_mode(回测)](settings.md#set_limit_mode)
- [set_yesterday_position(回测)](settings.md#set_yesterday_position)
- [run_daily(回测/交易)](#run_daily)
- [run_interval(交易)](#run_interval)
- [get_trading_day(研究/回测/交易)](basic-info.md#get_trading_day)
- [get_all_trades_days(研究/回测/交易)](basic-info.md#get_all_trades_days)
- [get_trade_days(交易)](basic-info.md#get_trade_days)
- [convert_position_from_csv(回测)](utilities.md#convert_position_from_csv)
- [get_user_name(回测/交易)](utilities.md#get_user_name)
- [is_trade(回测/交易)](utilities.md#is_trade)
- [get_research_path(回测/交易)](utilities.md#get_research_path)
- [permission_test(交易)](utilities.md#permission_test)
- [set_future_commission(回测(期货))](futures.md#set_future_commission)
- [set_margin_rate(回测(期货))](futures.md#set_margin_rate)
- [get_margin_rate(回测(期货))](futures.md#get_margin_rate)
- [create_dir(回测/交易)](utilities.md#create_dir)
- [set_parameters(回测/交易)](settings.md#set_parameters)

### 参数

context: [Context对象](objects.md#Context)，存放有当前的账户及持仓信息；

### 返回

None

### 示例

```python
def initialize(context):
    #g为全局对象
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    order('600570.SS',100)
```

## before_trading_start（可选）

```python
before_trading_start(context, data)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

该函数在每天开始交易前被调用一次，用于添加每天都要初始化的信息，如无盘前初始化需求，该函数可以在策略中不做定义。

注意事项：

1. 在回测中，该函数在每个回测交易日8:30分执行。
2. 在交易中，该函数在开启交易时立即执行，从隔日开始每天9:10分(默认)执行。
3. 当在9:10前开启交易时，受行情未更新原因在该函数内调用实时行情接口会导致数据有误。可通过在该函数内sleep至9:10分或调用实时行情接口改为run_daily执行等方式进行避免。

### 可调用接口

- [set_universe(回测/交易)](settings.md#set_universe)
- [get_Ashares(研究/回测/交易)](stock-info.md#get_Ashares)
- [set_yesterday_position(回测)](settings.md#set_yesterday_position)
- [get_stock_info(研究/回测/交易)](stock-info.md#get_stock_info)
- [get_index_stocks(研究/回测/交易)](stock-info.md#get_index_stocks)
- [get_fundamentals(研究/回测/交易)](stock-info.md#get_fundamentals)

### 参数

context: [Context对象](objects.md#Context)，存放有当前的账户及持仓信息；

data：保留字段暂无数据；

### 返回

None

### 示例

```python
def initialize(context):
    #g为全局变量
    g.security = '600570.SS'
    set_universe(g.security)

def before_trading_start(context, data):
    log.info(g.security)

def handle_data(context, data):
    order('600570.SS',100)
```

## handle_data（必选）

```python
handle_data(context, data)
```

### 使用场景

该函数仅在回测、交易模块可用

### 接口说明

该函数在交易时间内按指定的周期频率运行，是用于处理策略交易的主要模块，根据策略保存时的周期参数分为每分钟运行和每天运行，是策略运行的唯二必须定义函数之一。

注意事项：

1. 该函数每个单位周期执行一次
2. 如果是日线级别策略，每天执行一次。股票回测场景下，在15:00执行；股票交易场景下，执行时间为券商实际配置时间。
3. 如果是分钟级别策略，每分钟执行一次，股票回测场景下，执行时间为9:31 -- 15:00，股票交易场景下，执行时间为9:30 -- 14:59。
4. 回测与交易中，handle_data函数不会在非交易日触发（如回测或交易起始日期为2015年12月21日，则策略在2016年1月1日-3日时，handle_data不会运行，4日继续运行）。

### 参数

context: [Context对象](objects.md#Context)，存放有当前的账户及持仓信息；

data：一个字典(dict)，key是标的代码，value是当时的SecurityUnitData对象，存放当前周期（日线策略，则是当天；分钟策略，则是这一分钟）的数据；

注意：为了加速，data中的数据只包含股票池中所订阅标的的信息，可使用data[security]的方式来获取当前周期对应的标的信息；

### 返回

None

### 示例

```python
def initialize(context):
    #g为全局变量
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    order('600570.SS',100)
```
