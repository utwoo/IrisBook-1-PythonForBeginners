# 分散点图 (strip plot) 一般用来可视化一组分类变量与连续变量的关系。在分散图中，每个
# 数据点通过垂直于分类变量的轴上的一个点表示，连续变量的取值则沿着水平轴展示。
# 这种图形通常用于可视化分类变量和数值变量之间的关系，以观察数据的分布、聚集和离散程度，
# 同时也可以用于比较不同分类变量水平下的数值变量。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
sns.stripplot(ax=ax, 
              data=iris_sns, 
              x='sepal_length', 
              y='species', 
              hue='petal_length', 
              palette='RdYlBu_r')

plt.show()