# 箱型图 (box plot) 是一种常用的统计图表，用于展示数值变量的分布情况和异常值检测。
# 箱型图通过绘制数据的五个关键统计量，即最小值 (minimum)、第一四分位数 (first
# quartile) Q1、中位数 (median, second quartile) Q2、第三四分位数 (third quartile)
# Q3、最大值 (maximum) 以及可能存在的异常值来提供对数据的直观概览。

# 箱型图的主要元素包括：
# ► 箱体 (box)：由第一四分位数 Q1 和第三四分位数 Q3 之间的数据范围组成。箱体的高度表示数据
# 的四分位距 IQR = Q3 − Q1，箱体的中线表示数据的中位数。
# ► 须 (whisker)：延伸自箱体的线段，表示数据的整体分布范围。通常，须的长度为 1.5 倍的四
# 分位距。用 Seaborn 绘制的箱型图左须距离 Q1、右须距离 Q3
# 宽度并不相同。根据 Seaborn 的技术文档，左须、右须延伸至该范围 [Q1 − 1.5 × IQR, Q3
# + 1.5 × IQR] 内最远的样本点，具体如图 15 所示。更为极端的样本会被标记为异常值。
# ► 异常值 (outliers)：范围 [Q1 − 1.5 × IQR, Q3 + 1.5 × IQR] 之外的数据点，被认为是
# 异常值，可能表示数据中的极端值或异常观测。

import matplotlib.pyplot as plt
import seaborn as sns

# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
sns.boxplot(ax=ax, 
              data=iris_sns, 
              x='sepal_length', 
              y='species')

plt.show()