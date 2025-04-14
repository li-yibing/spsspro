import numpy
import pandas
import matplotlib.pyplot as plt
from spsspro.algorithm import supervised_learning

# 生成案例数据
data_x = pandas.DataFrame({
    "A": numpy.random.random(size=100),
    "B": numpy.random.random(size=100)
})
data_y = pandas.Series(data=numpy.random.choice([1, 2], size=100), name="C")

# 决策树分类
result = supervised_learning.decision_tree_classifier(data_x=data_x, data_y=data_y)

# 规范化输出结果
print("\n" + "="*50)
print("决策树分类结果报告")
print("="*50)
print(f"\n模型准确率: {result['accuracy']:.4f}")

print("\n特征重要性:")
print(result['feature_importance'])

print("\n分类报告:")
for label, metrics in result['classification_report'].items():
    if isinstance(metrics, dict):
        print(f"类别 {label}:")
        print(f"  精确率(Precision): {metrics['precision']:.4f}")
        print(f"  召回率(Recall): {metrics['recall']:.4f}")
        print(f"  F1分数: {metrics['f1-score']:.4f}")
        print(f"  样本数: {metrics['support']}")

print("\n混淆矩阵:")
print(result['confusion_matrix'])

# 添加可视化图表展示
plt.figure(figsize=(12, 10))

# 绘制特征重要性条形图
plt.subplot(2, 1, 1)
feature_importance = result['feature_importance']
sorted_idx = feature_importance['importance'].argsort()
features = feature_importance['feature'].iloc[sorted_idx]
importances = feature_importance['importance'].iloc[sorted_idx]
plt.barh(features, importances, color='skyblue')
plt.xlabel('重要性')
plt.ylabel('特征')
plt.title('特征重要性可视化')

# 绘制混淆矩阵热力图
plt.subplot(2, 1, 2)
conf_matrix = result['confusion_matrix']
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('混淆矩阵可视化')
plt.colorbar()

# 添加数值标签
thresh = conf_matrix.max() / 2
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        plt.text(j, i, format(conf_matrix[i, j], 'd'),
                 ha="center", va="center",
                 color="white" if conf_matrix[i, j] > thresh else "black")

# 设置坐标轴
classes = numpy.unique(data_y)
plt.xticks(range(len(classes)), classes)
plt.yticks(range(len(classes)), classes)
plt.xlabel('预测标签')
plt.ylabel('真实标签')

plt.tight_layout()
plt.show()