import matplotlib.pyplot as plt
import numpy as np

# 创建二维数据
x = np.linspace(-3, 3, 121)
y = np.linspace(-3, 3, 121)
X, Y = np.meshgrid(x, y)
Z = X * np.exp(- X**2 - Y**2)

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

# 等高线
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, levels=20, cmap='RdYlBu_r', linewidths=1)
fig.colorbar(CS)
ax.set_xlabel('$\it{x_1}$')
ax.set_ylabel('$\it{x_2}$')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(X.min(), X.max())
ax.set_ylim(Y.min(), Y.max())
ax.grid(False)
ax.set_aspect('equal', adjustable='box')

# 填充等高线
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, levels=20, cmap='RdYlBu_r')
fig.colorbar(CS)
ax.set_xlabel('$\it{x_1}$')
ax.set_ylabel('$\it{x_2}$')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(X.min(), X.max())
ax.set_ylim(Y.min(), Y.max())
ax.grid(False)
ax.set_aspect('equal', adjustable='box')

# 显示图形
plt.show()
