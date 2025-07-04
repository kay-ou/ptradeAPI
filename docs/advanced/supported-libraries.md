# 支持的三方库

Ptrade API 支持以下 Python 第三方库，您可以在策略中直接导入使用。

## 数据分析和科学计算

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| numpy | 1.11.2 | 数值计算基础库 |
| pandas | 0.23.4 | 数据分析和处理 |
| scipy | 0.18.0 | 科学计算库 |
| numexpr | 2.6.1 | 快速数值表达式计算 |
| Bottleneck | 1.0.0 | 快速NumPy数组函数 |

## 机器学习

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| scikit-learn | 0.18 | 机器学习库 |
| sklearn | 0.0 | scikit-learn别名 |
| tensorflow | 1.3.0rc1 | 深度学习框架 |
| Keras | 2.2.4 | 高级神经网络API |
| Keras-Applications | 1.0.8 | Keras预训练模型 |
| Keras-Preprocessing | 1.1.0 | Keras数据预处理 |
| Theano | 0.8.2 | 深度学习库 |
| xgboost | 0.6a2 | 梯度提升框架 |
| PyBrain | 0.3 | 神经网络库 |
| hmmlearn | 0.2.0 | 隐马尔可夫模型 |

## 数据可视化

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| matplotlib | 1.5.3 | 绘图库 |
| seaborn | 0.7.1 | 统计数据可视化 |
| cycler | 0.10.0 | matplotlib样式循环 |

## 技术分析

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| TA-Lib | 0.4.10 | 技术分析库 |

## 数据获取

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| tushare | 1.2.48 | 金融数据接口 |
| xcsc-tushare | 1.0.0 | 定制版tushare |
| requests | 2.7.0 | HTTP请求库 |
| beautifulsoup4 | 4.6.0 | HTML/XML解析 |
| lxml | 4.5.0 | XML和HTML处理 |

## 数据存储

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| h5py | 2.6.0 | HDF5文件接口 |
| tables | 3.3.0 | HDF5数据表 |
| SQLAlchemy | 1.0.8 | SQL工具包 |
| PyMySQL | 0.9.3 | MySQL数据库连接 |
| cx-Oracle | 8.0.1 | Oracle数据库连接 |
| bcolz | 1.2.1 | 列式存储 |

## 统计分析

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| statsmodels | 0.10.2 | 统计建模 |
| arch | 3.2 | 金融计量经济学 |
| patsy | 0.4.0 | 统计模型描述 |

## 文本处理

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| jieba | 0.38 | 中文分词 |
| gensim | 0.13.3 | 主题建模 |

## 任务调度

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| APScheduler | 3.3.1 | 任务调度器 |

## 优化计算

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| cvxopt | 1.1.8 | 凸优化 |
| Cython | 0.22.1 | Python C扩展 |

## 工具库

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| python-dateutil | 2.7.5 | 日期时间处理 |
| pytz | 2015.4 | 时区处理 |
| six | 1.10.0 | Python 2/3兼容 |
| click | 4.0 | 命令行接口 |
| retrying | 1.3.3 | 重试装饰器 |
| cachetools | 3.1.0 | 缓存工具 |
| toolz | 0.7.4 | 函数式编程工具 |

## 加密和安全

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| crypto | 1.4.1 | 加密库 |
| pycrypto | 2.6.1 | 密码学工具包 |

## 文件处理

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| xlrd | 1.1.0 | Excel文件读取 |
| PyYAML | 3.13 | YAML文件处理 |
| bz2file | 0.98 | bz2压缩文件处理 |

## 网络和通信

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| tornado | 4.4.2 | Web框架 |
| pyzmq | 16.1.0.dev0 | ZeroMQ消息传递 |
| boto | 2.43.0 | AWS SDK |

## 其他工具

| 库名称 | 版本号 | 说明 |
|--------|--------|------|
| networkx | 1.9.1 | 图论和网络分析 |
| PyWavelets | 0.4.0 | 小波变换 |
| tabulate | 0.7.5 | 表格格式化 |
| smart-open | 1.3.5 | 智能文件打开 |

## 使用示例

### 数据分析示例

```python
import pandas as pd
import numpy as np

def handle_data(context, data):
    # 获取历史数据
    hist = get_history(20, '1d', 'close', '600570.SS')
    
    # 使用pandas计算移动平均
    ma5 = hist['close'].rolling(5).mean()
    ma20 = hist['close'].rolling(20).mean()
    
    # 使用numpy进行数值计算
    returns = np.diff(hist['close']) / hist['close'][:-1]
    volatility = np.std(returns)
```

### 技术分析示例

```python
import talib

def handle_data(context, data):
    # 获取历史数据
    hist = get_history(50, '1d', ['open', 'high', 'low', 'close'], '600570.SS')
    
    # 使用TA-Lib计算技术指标
    rsi = talib.RSI(hist['close'].values)
    macd, signal, histogram = talib.MACD(hist['close'].values)
    
    # 基于技术指标进行交易决策
    if rsi[-1] < 30:  # 超卖
        order_value('600570.SS', 10000)
```

### 机器学习示例

```python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def initialize(context):
    g.model = None
    g.security = '600570.SS'
    set_universe(g.security)

def handle_data(context, data):
    # 获取特征数据
    hist = get_history(100, '1d', 'close', g.security)
    
    # 构建特征
    features = pd.DataFrame()
    features['ma5'] = hist['close'].rolling(5).mean()
    features['ma20'] = hist['close'].rolling(20).mean()
    features['rsi'] = talib.RSI(hist['close'].values)
    
    # 如果有足够数据，进行预测
    if len(features.dropna()) > 50:
        # 训练模型（简化示例）
        if g.model is None:
            # 这里应该有标签数据
            g.model = RandomForestClassifier()
            # g.model.fit(X_train, y_train)
        
        # 进行预测
        # prediction = g.model.predict(features.iloc[-1:])
```

## 注意事项

1. **版本兼容性**: 请确保您的代码与列出的库版本兼容
2. **性能考虑**: 某些库（如深度学习框架）可能会影响策略运行速度
3. **内存使用**: 大型数据处理时注意内存使用情况
4. **导入时间**: 避免在频繁调用的函数中重复导入库

## 更新说明

库版本会定期更新，请关注版本变动通知。如需使用特定版本的库，请联系技术支持。
