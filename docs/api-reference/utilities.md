# 工具函数API

本文档详细介绍了 Ptrade 平台提供的各类辅助工具函数，包括日志记录、系统交互、通信及权限管理等。

---

## 日志与调试

### `log()` - 日志记录

-   **接口说明**: 在策略运行过程中打印日志，方便调试和监控。支持不同级别的日志记录。
-   **使用方法**:
    ```python
    log.debug("这是一条调试信息")
    log.info("这是一条普通信息")
    log.warning("这是一条警告信息")
    log.error("这是一条错误信息")
    log.critical("这是一条严重错误信息")
    ```-   **参数**:
    -   `content`: 可以是字符串、对象等任何需要打印的内容。
-   **返回**: `None`。

### `is_trade()` - 场景判断

-   **接口说明**: 判断当前策略是运行在**交易**环境还是**回测**环境。
-   **返回**: `bool`。在交易环境中返回 `True`，在回测环境中返回 `False`。

### `check_limit()` - 涨跌停状态判断

-   **接口说明**: 检查指定证券在指定日期的涨跌停状态。
-   **参数**:
    -   `security` (str or list[str]): 单个或多个证券代码。
    -   `query_date` (str, optional): 查询日期，格式 `YYYYMMDD`。默认为当前日期。
-   **返回**: `dict`。key为证券代码，value为状态码：
    -   `1`: 涨停
    -   `-1`: 跌停
    -   `2`: 触及涨停
    -   `-2`: 触及跌停
    -   `0`: 未涨跌停

---

## 文件与路径

### `create_dir()` - 创建目录

-   **接口说明**: 在研究环境的根目录下创建新的子目录。
-   **注意事项**: Ptrade 禁用了 `os` 模块，请使用此函数创建目录。根目录为 `/home/fly/notebook/`。
-   **参数**:
    -   `user_path` (str): 要创建的子目录路径，如 `'my_data'` 或 `'my_data/daily'`。
-   **返回**: `None`。

### `get_research_path()` - 获取研究路径

-   **接口说明**: 获取研究环境的根目录路径。
-   **返回**: 字符串，研究环境的根路径 (`/home/fly/notebook/`)。

### `convert_position_from_csv()` - 从CSV加载底仓

-   **使用场景**: 仅回测模块可用。
-   **接口说明**: 从 CSV 文件中读取持仓信息，用于 `set_yesterday_position()` 设置回测底仓。
-   **参数**:
    -   `path` (str): CSV文件的路径。文件需包含 `sid`, `amount`, `enable_amount`, `cost_basis` 等列。
-   **返回**: `list[dict]`，可直接传递给 `set_yesterday_position()`。

---

## 通信功能

### `send_email()` - 发送邮件

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 通过QQ邮箱发送邮件。
-   **注意事项**: 需要券商开启外网访问权限。
-   **参数**:
    -   `send_email_info` (str): 发件人QQ邮箱。
    -   `get_email_info` (str or list[str]): 收件人邮箱。
    -   `smtp_code` (str): 发件人邮箱的SMTP授权码。
    -   `info` (str, optional): 邮件正文。
    -   `path` (str, optional): 附件路径。
    -   `subject` (str, optional): 邮件主题。
-   **返回**: `None`。

### `send_qywx()` - 发送企业微信

-   **使用场景**: 仅交易模块可用。
-   **接口说明**: 通过企业微信应用发送消息。
-   **注意事项**: 需要券商开启外网访问权限。
-   **参数**:
    -   `corp_id` (str): 企业ID。
    -   `secret` (str): 应用的Secret。
    -   `agent_id` (str): 应用的AgentId。
    -   `info` (str, optional): 消息内容。
    -   `toparty`/`touser`/`totag` (str, optional): 指定接收的部门、成员或标签。
-   **返回**: `None`。

---

## 账户与权限

### `get_user_name()` - 获取用户名

-   **接口说明**: 获取当前登录终端的资金账号。
-   **返回**: 资金账号 (str)。

### `get_trade_name()` - 获取交易名称

-   **接口说明**: 获取当前运行的交易实例的名称。
-   **返回**: 交易名称 (str)。

### `permission_test()` - 权限校验

-   **使用场景**: 仅交易模块可用，且建议在 `initialize` 或 `after_trading_end` 中调用。
-   **接口说明**: 用于策略的授权验证，可校验使用者账号和策略有效期。
-   **参数**:
    -   `account` (str, optional): 授权的资金账号。
    -   `end_date` (str, optional): 授权截止日期，格式 `YYYYMMDD`。
-   **返回**: `bool`。校验成功返回 `True`，失败返回 `False`。
