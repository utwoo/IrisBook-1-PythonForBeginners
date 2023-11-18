# 联合分布、边缘分布

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

g = sns.JointGrid(data=iris_sns, x='sepal_length', y='sepal_width')
g.plot_joint(sns.scatterplot)
g.plot_marginals(sns.boxplot)

g = sns.JointGrid(data=iris_sns, x="sepal_length", y="sepal_width")
g.plot_joint(sns.scatterplot)
g.plot_marginals(sns.kdeplot)

plt.show()