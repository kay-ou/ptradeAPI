# 工具函数API

本文档介绍各种实用的工具函数，包括日志记录、邮件发送、权限校验等功能。

## 日志和调试

### log - 日志记录

```python
log(content)
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于打印日志。支持如下场景的日志记录：

```python
log.debug("debug")
log.info("info")
log.warning("warning")
log.error("error")
log.critical("critical")
```

与python的logging模块用法一致

#### 参数

参数可以是字符串、对象等

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 打印出一个格式化后的字符串
    log.info("Selling %s, amount=%s" % (g.security, 10000))
    
    # 不同级别的日志
    log.debug("调试信息")
    log.info("一般信息")
    log.warning("警告信息")
    log.error("错误信息")
    log.critical("严重错误")
```

### is_trade - 业务代码场景判断

```python
is_trade()
```

#### 使用场景

该函数仅在回测、交易模块可用

#### 接口说明

该接口用于提供业务代码执行场景判断依据，明确标识当前业务代码运行场景为回测还是交易。因部分函数仅限回测或交易场景使用，该函数可以协助区分对应场景，以便限制函数可以在一套策略代码同时兼容回测与交易场景。

#### 参数

无

#### 返回

布尔类型，当前代码在交易中运行返回True，当前代码在回测中运行返回False(bool)

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    _id = order(g.security, 100)
    
    if is_trade():
        log.info("当前运行场景：交易")
        # 交易环境特有的逻辑
        snapshot = get_snapshot(g.security)
    else:
        log.info("当前运行场景：回测")
        # 回测环境特有的逻辑
        set_slippage(slippage=0.002)
```

## 股票状态检查

### check_limit - 代码涨跌停状态判断

```python
check_limit(security, query_date=None)
```

#### 使用场景

该函数在研究、回测、交易模块可用

#### 接口说明

该接口用于标识股票的涨跌停情况。

注意事项：

1. 入参的security非str非list类型，返回空字典
2. 入参的query_date仅支持YYYYmmdd格式的传参，当query_date入参为None或传入当日日期时，返回的结果是以实时最新价判断涨跌停状态;当query_date入参为历史交易日期，则均以交易日收盘价判断涨跌停状态。

#### 参数

security：单只股票代码或者多只股票代码组成的列表，必填字段(list[str]/str)；

query_date：查询日期，查询指定日期股票代码的涨跌停状态，回测不传默认是回测当日时间，交易和研究不传默认是执行当日时间，非必填字段(str)；

#### 返回

正常返回一个dict类型数据，包含每只股票代码的涨停状态。多只股票代码查询时其中部分股票代码查询异常则该代码返回既不涨停也不跌停状态0。(dict[str:int])

涨跌停状态说明：

- 2：触板涨停（已经是涨停价格，但还有卖盘）(仅支持交易研究查询当日)；
- 1：涨停；
- 0：既不涨停也不跌停；
- -1：跌停；
- -2：触板跌停（已经是跌停价格，但还有买盘）(仅支持交易研究查询当日)；

#### 示例

```python
def initialize(context):
    g.security = ['600570.SS', '000001.SZ']
    set_universe(g.security)

def handle_data(context, data):
    # 检查股票涨跌停状态
    for stock in g.security:
        stock_flag = check_limit(stock)[stock]
        if stock_flag == 1:
            log.info('%s 涨停' % stock)
        elif stock_flag == -1:
            log.info('%s 跌停' % stock)
        elif stock_flag == 0:
            # 正常交易，可以下单
            order(stock, 100)
```

## 通信功能

### send_email - 发送邮箱信息

```python
send_email(send_email_info, get_email_info, smtp_code, info='', path='', subject='')
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

该接口用于通过QQ邮箱发送邮件内容。

注意事项：

1. 该接口需要服务端连通外网，是否开通由所在券商决定
2. 是否允许发送附件（即path参数），由所在券商的配置管理决定
3. 邮件中接受到的附件为文件名而非附件路径

#### 参数

send_email_info：发送方的邮箱地址，必填字段，如:example@qq.com(str)；

get_email_info：接收方的邮箱地址，必填字段，如:[example1@qq.com, example2@qq.com](list[str]/str)；

smtp_code：邮箱的smtp授权码，注意，不是邮箱密码，必填字段(str)；

info：发送内容，选填字段，默认空字符串(str)；

path：附件路径，选填字段，如:'/home/fly/notebook/stock.csv'，默认空字符串(str)；

subject：邮件主题，默认空字符串(str)；

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 发送交易提醒邮件
    if get_position(g.security).amount > 0:
        send_email(
            'sender@qq.com', 
            ['receiver@qq.com'], 
            'smtp_authorization_code', 
            info='策略已买入股票：%s' % g.security,
            subject='交易提醒'
        )
```

### send_qywx - 发送企业微信信息

```python
send_qywx(corp_id, secret, agent_id, info='', path='', toparty='', touser='', totag='')
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

该接口用于通过企业微信发送内容。

注意事项：

1. 该接口需要服务端连通外网，是否开通由所在券商决定
2. 是否允许发送文件（即path参数），由所在券商的配置管理决定
3. 企业微信不能同时发送文字和文件，当同时入参info和path的时候，默认发送文件
4. 企业微信接受到的文件为文件名而非文件路径

#### 参数

corp_id：企业ID，必填字段(str)；

secret：企业微信应用的密码，必填字段(str)；

agent_id：企业微信应用的ID，必填字段(str)；

info：发送内容，选填字段，默认空字符串(str)；

path：发送文件，选填字段，如:'/home/fly/notebook/stock.csv'，默认空字符串(str)；

toparty：发送对象为部门，选填字段，默认空字符串(str)，多个对象之间用 '|' 符号分割；

touser：发送内容为个人，选填字段，默认空字符串(str)，多个对象之间用 '|' 符号分割；

totag：发送内容为分组，选填字段，默认空字符串(str)，多个对象之间用 '|' 符号分割；

注意：toparty、touser、totag如果都不传入，接口默认发送至应用中设定的第一个toparty

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 发送企业微信消息
    if data[g.security]['close'] > 50:
        send_qywx(
            'corp_id_here', 
            'secret_here', 
            'agent_id_here', 
            info='股价突破50元，已触发委托买入', 
            toparty='1|2'
        )
```

## 权限和文件管理

### permission_test - 权限校验

```python
permission_test(account=None, end_date=None)
```

#### 使用场景

该函数仅在交易模块可用

#### 接口说明

该接口用于账号和有效期的权限校验，用户可以在接口中入参指定账号和指定有效期截止日，策略运行时会校验运行策略的账户与指定账户是否相符，以及运行当日日期是否超过指定的有效期截止日，任一条件校验失败，接口都会返回False，两者同时校验成功则返回True。校验失败会在策略日志中提示原因。

注意事项：

该函数仅在initialize、before_trading_start、after_trading_end模块中支持调用

#### 参数

account：授权账号，选填字段，如果不填就代表不需要验证账号(str)；

end_date：授权有效期截止日，选题字段，如果不填就代表不需要验证有效期(str)，日期格式必须为'YYYYmmdd'的8位日期格式，如'20200101'；

#### 返回

布尔类型，校验成功返回True，校验失败返回False(bool)

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    
    # 权限校验
    flag = permission_test(account='10110922', end_date='20250101')
    if not flag:
        raise RuntimeError('授权不通过，终止程序')

def handle_data(context, data):
    pass
```

### create_dir - 创建文件目录路径

```python
create_dir(user_path=None)
```

#### 使用场景

该函数在研究、回测、交易模块可用

#### 接口说明

由于ptrade引擎禁用了os模块，因此用户无法在策略中通过编写代码实现子目录创建。用户可以通过此接口来创建文件的子目录路径。

注意事项：

文件根目录路径为'/home/fly/notebook'

#### 参数

user_path：子目录路径，选填字段，(str)

比如user_path='download'，会在研究中生成/home/fly/notebook/download的目录；

比如user_path='download/2022'，会在研究中生成/home/fly/notebook/download/2022的目录；

#### 返回

None

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    # 创建以股票代码命名的目录
    create_dir(user_path=g.security)

def handle_data(context, data):
    pass
```

### get_user_name - 获取用户名

```python
get_user_name()
```

#### 使用场景

该函数在回测、交易模块可用

#### 接口说明

该接口用于获取登录终端的资金账号。

#### 参数

无

#### 返回

字符串类型，返回当前登录的资金账号(str)

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    
    # 获取当前用户名
    user_name = get_user_name()
    log.info('当前用户: %s' % user_name)

def handle_data(context, data):
    pass
```

### get_research_path - 获取研究路径

```python
get_research_path()
```

#### 使用场景

该函数在回测、交易模块可用

#### 接口说明

该接口用于获取研究环境的文件路径。

#### 参数

无

#### 返回

字符串类型，返回研究环境的根路径(str)

#### 示例

```python
def initialize(context):
    g.security = '600570.SS'
    set_universe(g.security)
    
    # 获取研究路径
    research_path = get_research_path()
    log.info('研究路径: %s' % research_path)

def handle_data(context, data):
    pass
```

## 相关文档

- [基础信息API](basic-info.md) - 获取交易日期、市场信息
- [股票交易API](stock-trading.md) - 股票交易相关功能
- [对象说明](objects.md) - Context、Portfolio等对象详解
