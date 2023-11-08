import matplotlib.pyplot as plt
import numpy as np

# 创建二维数据
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)  # 构造网格坐标点
Z = X**2 + Y**2

"""
X:二维数组，表示数据点的横坐标。
Y:二维数组，表示数据点的纵坐标。
Z:二维数组，表示数据点对应的函数值或高度。
levels:用于指定绘制的等高线层级或数值列表。
colors:用于指定等高线的颜色，可以是单个颜色字符串、颜色序列或 colormap 对象。
cmap:颜色映射，用于将数值映射为颜色。可以是预定义的 colormap 名称或 colormap 对象。
linestyles:用于指定等高线的线型，可以是单个线型字符串或线型序列。
linewidths:用于指定等高线的线宽，可以是单个线宽值或线宽序列。
alpha:用于指定等高线的透明度。
"""
# 绘制等高线图
plt.contour(X, Y, Z, levels=np.linspace(0, 8, 16+1), cmap='RdYlBu_r')
# 添加颜色图例
plt.colorbar()
# 显示图形
plt.show()
