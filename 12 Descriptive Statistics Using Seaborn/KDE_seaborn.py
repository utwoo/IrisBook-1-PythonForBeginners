# 核密度估计 (Kernel Density Estimation, KDE) 是一种非参数方法，用于估计连续变量
# 的概率密度函数 (Probability Density Function, PDF)。它通过将每个数据点视为一个核函
# 数 (通常是高斯核函数)，在整个变量范围内生成一系列核函数，然后将这些核函数进行平滑和叠加，
# 从而得到连续的概率密度估计曲线。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

fig = plt.figure()

# 绘制花萼长度样本数据，高斯核密度估计
ax = fig.add_subplot(2, 2, 1)
sns.kdeplot(
    data=iris_sns,
    x='sepal_length',
    bw_adjust=0.3,
    fill=True
)

sns.rugplot(
    data=iris_sns,
    x='sepal_length'
)

# 绘制花萼长度样本数据，高斯核密度估计，考虑鸢尾花类别
ax = fig.add_subplot(2, 2, 2)
sns.kdeplot(
    data=iris_sns, 
    x='sepal_length', 
    hue='species',
    bw_adjust=0.5, 
    fill=True
)

sns.rugplot(
    data=iris_sns, 
    x='sepal_length', 
    hue='species'
)

# 绘制花萼长度样本数据，高斯核密度估计，考虑鸢尾花类别，堆叠
ax = fig.add_subplot(2, 2, 3)
sns.kdeplot(
    data=iris_sns, 
    x='sepal_length', 
    hue= 'species',
    multiple='stack', 
    bw_adjust=0.5
)

# 绘制后验概率 (成员值)
ax = fig.add_subplot(2, 2, 4)
sns.kdeplot(
    data=iris_sns, 
    x='sepal_length',
    hue='species', 
    bw_adjust=0.5, 
    multiple = 'fill'
)

plt.show()
