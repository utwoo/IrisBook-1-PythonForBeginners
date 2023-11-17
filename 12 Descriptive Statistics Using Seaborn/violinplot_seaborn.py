# 小提琴图 (violin plot) 是一种用于可视化数值变量分布的图表类型。它结合了核密度估计曲线和箱型图的特点。

# 小提琴图的主要组成部分包括：
# ► 背景形状：由核密度估计曲线组成，表示数据在不同值上的概率密度。
# ► 中位数线：位于核密度估计曲线的中间位置，表示数据的中位数。
# ► 四分位线：分别位于核密度估计曲线的 25% 和 75% 位置，表示数据的四分位范围。
# ► 离群值点：位于核密度估计曲线之外的离群值数据点。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

fig = plt.figure()

# 绘制花萼长度样本数据，小提琴图，考虑分类
sns.violinplot(
    data=iris_sns,
    x='sepal_length',
    y='species')

# 蜂群图 + 小提琴图，考虑鸢尾花分类
sns.catplot(
    data=iris_sns,
    x='sepal_length',
    y='species',
    kind='violin',
    color='.9',
    inner=None)

sns.swarmplot(
    data=iris_sns,
    x='sepal_length',
    y='species',
    size=3)

plt.show()
