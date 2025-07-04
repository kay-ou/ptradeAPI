# 快速入门

本文档将带您快速上手 Ptrade API，从最简单的策略开始，逐步学习如何编写有效的量化交易策略。

## 简单但是完整的策略

先来看一个简单但是完整的策略:

```python
def initialize(context):
    set_universe('600570.SS')

def handle_data(context, data):
    pass
```

一个完整策略只需要两步:

1. `set_universe`: 设置我们要操作的股票池，上面的例子中，只操作一支股票: '600570.SS'，恒生电子。所有的操作只能对股票池的标的进行。
2. 实现一个函数: `handle_data`。

这是一个完整的策略，但是我们没有任何交易，下面我们来添加一些交易。

## 添加一些交易

```python
def initialize(context):
    g.security = '600570.SS'
    # 是否创建订单标识
    g.flag = False
    set_universe(g.security)

def handle_data(context, data):
    if not g.flag:
        order(g.security, 1000)
        g.flag = True
```

这个策略里，当我们没有创建订单时就买入1000股'600570.SS'，具体的下单API请看[order](../api-reference/stock-trading.md#order)函数。这里我们有了交易，但是只是无意义的交易，没有依据当前的数据做出合理的分析。

## 实用的策略

下面我们来看一个真正实用的策略

在这个策略里，我们会根据历史价格做出判断:

- 如果上一时间点价格高出五天平均价1%，则全仓买入
- 如果上一时间点价格低于五天平均价，则空仓卖出

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    
def handle_data(context, data):
    security = g.security
    sid = g.security
    
    # 取得过去五天的历史价格
    df = get_history(5, '1d', 'close', security, fq=None, include=False)
    
    # 取得过去五天的平均价格
    average_price = round(df['close'][-5:].mean(), 3)

    # 取得上一时间点价格
    current_price = data[sid]['close']
    
    # 取得当前的现金
    cash = context.portfolio.cash
    
    # 如果上一时间点价格高出五天平均价1%, 则全仓买入
    if current_price > 1.01*average_price:
        # 用所有 cash 买入股票
        order_value(g.security, cash)
        log.info('buy %s' % g.security)
    # 如果上一时间点价格低于五天平均价, 则空仓卖出
    elif current_price < average_price and get_position(security).amount > 0:
        # 卖出所有股票,使这只股票的最终持有量为0
        order_target(g.security, 0)
        log.info('sell %s' % g.security)
```

## 模拟盘和实盘注意事项

### 关于持久化

#### 为什么要做持久化处理

服务器异常、策略优化等诸多场景，都会使得正在进行的模拟盘和实盘策略存在中断后再重启的需求，但是一旦交易中止后，策略中存储在内存中的全局变量就清空了，因此通过持久化处理为量化交易保驾护航必不可少。

#### 量化框架持久化处理

使用pickle模块保存股票池、账户信息、订单信息、全局变量g定义的变量等内容。

注意事项：

1. 框架会在[before_trading_start（隔日开始）](../api-reference/framework.md#before_trading_start)、[handle_data](../api-reference/framework.md#handle_data)、[after_trading_end](../api-reference/framework.md#after_trading_end)事件后触发持久化信息更新及保存操作；
2. 券商升级/环境重启后恢复交易时，框架会先执行策略[initialize](../api-reference/framework.md#initialize)函数再执行持久化信息恢复操作。如果持久化信息保存有策略定义的全局对象g中的变量，将会以持久化信息中的变量覆盖掉[initialize](../api-reference/framework.md#initialize)函数中初始化的该变量。
3. 全局变量g中不能被序列化的变量将不会被保存。您可在[initialize](../api-reference/framework.md#initialize)中初始化该变量时名字以'__'开头；
4. 涉及到IO(打开的文件，实例化的类对象等)的对象是不能被序列化的；
5. 全局变量g中以'__'开头的变量为私有变量，持久化时将不会被保存；

#### 示例

```python
class Test(object):
    count = 5

    def print_info(self):
        self.count += 1
        log.info("a" * self.count)


def initialize(context):
    g.security = "600570.SS"
    set_universe(g.security)
    # 初始化无法被序列化类对象，并赋值为私有变量，落地持久化信息时跳过保存该变量
    g.__test_class = Test()

def handle_data(context, data):
    # 调用私有变量中定义的方法
    g.__test_class.print_info()
```

#### 策略中持久化处理方法

使用pickle模块保存 g 对象(全局变量)。

#### 示例

```python
import pickle
from collections import defaultdict
NOTEBOOK_PATH = '/home/fly/notebook/'
'''
持仓N日后卖出，仓龄变量每日pickle进行保存，重启策略后可以保证逻辑连贯
'''
def initialize(context):
    #尝试启动pickle文件
    try:
        with open(NOTEBOOK_PATH+'hold_days.pkl','rb') as f:
            g.hold_days = pickle.load(f)
    #定义空的全局字典变量
    except:
        g.hold_days = defaultdict(list)
    g.security = '600570.SS'
    set_universe(g.security)

# 仓龄增加一天
def before_trading_start(context, data):
    if g.hold_days:
        g.hold_days[g.security] += 1
        
# 每天将存储仓龄的字典对象进行pickle保存
def handle_data(context, data):
    if g.security not in list(context.portfolio.positions.keys()) and g.security not in g.hold_days:
        order(g.security, 100)
        g.hold_days[g.security] = 1
    if g.hold_days:
        if g.hold_days[g.security] > 5:
            order(g.security, -100)
            del g.hold_days[g.security]
    with open(NOTEBOOK_PATH+'hold_days.pkl','wb') as f:
        pickle.dump(g.hold_days,f,-1)
```

## 下一步

- [策略示例](examples.md) - 查看更多完整的策略示例
- [API参考](../api-reference/) - 查看详细的API文档
- [常见问题](../advanced/faq.md) - 解决常见问题
