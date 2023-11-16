# 蜂群图 (swarm plot) 是一种用于可视化分类变量和数值变量关系的图表类型。它通过在分类
# 轴上对数据进行分散排列，避免数据点的重叠，以展示数值变量在不同类别下的分布情况。每个数据点
# 在分类轴上的位置表示其对应的数值大小，从而呈现出数据的密度和分布趋势。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
sns.swarmplot(ax=ax, 
              data=iris_sns, 
              x='sepal_length', 
              y='species', 
              hue='petal_length', 
              palette='RdYlBu_r')

plt.show()