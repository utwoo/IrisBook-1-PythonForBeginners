# seaborn.lmplot() 函数默认情况下会绘制散点图和拟合的线性回归线。散点图展示了两个变量
# 之间的关系，而线性回归线表示了拟合的线性关系。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

# 可视化线性回归关系，考虑鸢尾花分类
sns.lmplot(
    data=iris_sns, 
    x = 'sepal_length', 
    y='sepal_width', 
    hue = 'species')

plt.show()