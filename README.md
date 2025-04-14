# SPSS Pro

一个用于统计分析和机器学习的Python库，提供简单易用的接口。

## 安装

```bash
pip install -e .
```

## 功能特点

- 监督学习算法
  - 决策树分类
  - 更多算法将陆续添加...

## 使用示例

### 决策树分类

```python
import numpy
import pandas
from spsspro.algorithm import supervised_learning

# 生成案例数据
data_x = pandas.DataFrame({
    "A": numpy.random.random(size=100),
    "B": numpy.random.random(size=100)
})
data_y = pandas.Series(data=numpy.random.choice([1, 2], size=100), name="C")

# 决策树分类
result = supervised_learning.decision_tree_classifier(data_x=data_x, data_y=data_y)

# 查看结果
print(f"模型准确率: {result['accuracy']}")
print("\n特征重要性:")
print(result['feature_importance'])
```

## 依赖项

- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn