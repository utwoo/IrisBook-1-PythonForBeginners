# 散点图是一种数据可视化图表，用于展示两个变量之间的关系。它通过在坐标系中以点的形式表示
# 每个数据点，横轴代表一个变量，纵轴代表另一个变量。
# 散点图可以帮助我们观察和分析数据点之间的趋势、分布和相关性。通过观察点的聚集程度和分布
# 形状，我们可以推断两个变量之间的关系类型，如线性正相关、线性负相关、线性无关，甚至是非线性关系。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

# 鸢尾花散点图 + 毛毯图，考虑鸢尾花分类
fig, ax = plt.subplots(figsize=(8, 4))

sns.scatterplot(
    data=iris_sns,
    x='sepal_length',
    y='sepal_width',
    hue='species'
)

sns.rugplot(
    data=iris_sns,
    x='sepal_length',
    y='sepal_width',
    hue='species'
)

plt.show()
