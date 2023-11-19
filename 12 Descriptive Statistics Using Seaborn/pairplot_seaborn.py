# 对特征散点图矩阵，可视化多个变量之间的关系和分布。它会将数据集中的每对特征绘制为散点图，并展示变量之间的散点关系和单变量的分布。

# seaborn.pairplot() 函数会根据数据集中的每对特征生成散点图，并以网格矩阵
# 的形式展示。对角线上的图形通常是单变量的直方图或核密度估计图，表示每个变量的分布情况。非对
# 角线上的图形是两个变量之间的散点图，展示它们之间的关系。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

sns.pairplot(data=iris_sns, hue='species')

plt.show()