# spsspro.algorithm.supervised_learning模块
# 包含监督学习算法

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# 过滤警告信息
warnings.filterwarnings('ignore')

# 设置matplotlib中文字体支持
try:
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
except:
    pass  # 如果字体不存在，忽略错误

def decision_tree_classifier(data_x, data_y, test_size=0.3, random_state=42, max_depth=None, criterion='gini'):
    """
    决策树分类算法
    
    参数:
    data_x: pandas.DataFrame, 特征数据
    data_y: pandas.Series, 目标变量
    test_size: float, 测试集比例，默认0.3
    random_state: int, 随机种子，默认42
    max_depth: int, 决策树最大深度，默认None
    criterion: str, 分类标准，'gini'或'entropy'，默认'gini'
    
    返回:
    dict: 包含模型、预测结果和评估指标的字典
    """
    # 数据检查
    if not isinstance(data_x, pd.DataFrame):
        raise TypeError("data_x必须是pandas.DataFrame类型")
    if not isinstance(data_y, pd.Series):
        raise TypeError("data_y必须是pandas.Series类型")
    
    # 数据分割
    X_train, X_test, y_train, y_test = train_test_split(
        data_x, data_y, test_size=test_size, random_state=random_state
    )
    
    # 创建并训练模型
    model = DecisionTreeClassifier(max_depth=max_depth, criterion=criterion, random_state=random_state)
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    
    # 特征重要性
    feature_importance = pd.DataFrame({
        'feature': data_x.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    # 评估指标
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    # 可视化混淆矩阵（返回图形数据）
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                xticklabels=np.unique(data_y),
                yticklabels=np.unique(data_y))
    plt.xlabel('预测标签', fontsize=12)
    plt.ylabel('真实标签', fontsize=12)
    plt.title('混淆矩阵', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # 可视化特征重要性（返回图形数据）
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='importance', y='feature', data=feature_importance, palette='viridis')
    plt.title('特征重要性', fontsize=14, fontweight='bold')
    plt.xlabel('重要性', fontsize=12)
    plt.ylabel('特征', fontsize=12)
    # 添加数值标签
    for i, v in enumerate(feature_importance['importance']):
        ax.text(v + 0.01, i, f'{v:.4f}', va='center')
    plt.tight_layout()
    
    # 返回结果
    result = {
        'model': model,
        'accuracy': accuracy,
        'classification_report': report,
        'confusion_matrix': conf_matrix,
        'feature_importance': feature_importance,
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test,
        'y_pred': y_pred
    }
    
    return result