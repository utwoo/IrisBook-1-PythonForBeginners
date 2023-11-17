# 高斯核函数 KDE 也可以用在估算二元联合分布

# 联合分布是统计学中用于描述两个或多个随机变量同时取值的概率分布。它提供了关于多个变量之间关系的信息，包括它们的联
# 合概率、相互依赖程度以及共同变化的模式。联合分布可以以多种形式呈现，如概率质量函数（离散变量）或概率密度函数（连
# 续变量）。通过分析联合分布，我们可以洞察变量之间的相关性、条件概率以及预测和推断未来事件的可能性。联合分布在概率
# 论、统计建模、数据分析和机器学习等领域具有广泛应用。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

# 联合分布概率密度等高线，考虑分布
sns.displot(
    data=iris_sns,
    x='sepal_length',
    y='sepal_width',
    kind='kde',
    hue='species')

sns.scatterplot(
    data=iris_sns,
    x='sepal_length',
    y='sepal_width',
    hue='species'
)

plt.show()
