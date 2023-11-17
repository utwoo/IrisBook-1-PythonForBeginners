# 二元直方热图由一个矩形网格组成，其中每个单元格的颜色代表了对应的数据频数、概率、概率密
# 度。通常，行和列代表两个不同的随机变量，而单元格中的颜色强度表示频数、概率、概率密度。
# 二元直方热图可以帮助我们观察两个变量之间的关系以及它们的分布模式。通过观察颜色的变化和
# 集中区域，我们可以得出关于两个变量之间的相关性、联合分布和潜在模式的初步结论。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

# 鸢尾花二元频率直方热图
sns.displot(
    data=iris_sns,
    x='sepal_length',
    y='sepal_width',
    binwidth=(0.2, 0.2),
    cbar=True)

plt.show()
