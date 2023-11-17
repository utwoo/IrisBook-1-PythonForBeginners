# 边缘分布是指在多变量数据集中，针对单个变量的分布情况。它表示了某个特定变量在与其他变量无关时的概率分布。边缘分布
# 可以通过将多变量数据集投影到某个特定变量的轴上来获得。通过分析边缘分布，我们可以了解每个变量单独的分布特征，包括
# 均值、方差、偏度、峰度等统计量，以及分布的形状和模式。边缘分布对于探索数据集的特征、进行单变量分析和了解数据的单
# 个方面非常有用。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

# 联合分布、边缘分布
sns.jointplot(
    data=iris_sns, 
    x='sepal_length', 
    y='sepal_width',
    kind = 'kde', 
    fill = True)

# 联合分布、边缘分布，考虑鸢尾花分类
sns.jointplot(
    data=iris_sns, 
    x='sepal_length', 
    y='sepal_width',
    hue = 'species', 
    kind='kde')

plt.show()