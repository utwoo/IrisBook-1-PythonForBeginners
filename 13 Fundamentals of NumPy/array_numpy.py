# 在 NumPy 中，array 是一种多维数组对象，它可以用于表示和操作向量、矩阵和张量等数据结构。array 是 NumPy 中最重要
# 的数据结构之一，它支持高效的数值计算和广播操作，可以用于处理大规模数据集和科学计算。与 Python 中的列表不同，
# array 是一个固定类型、固定大小的数据结构，它可以支持多维数组操作和高性能数值计算。array 的每个元素都是相同类型
# 的，通常是浮点数、整数或布尔值等基本数据类型。在创建 array 时，用户需要指定数组的维度和类型。例如，可以使用
# numpy.array() 函数创建一个一维数组或二维数组，也可以使用 numpy.zeros() 函数或 numpy.ones() 函数创建指定大
# 小的全 0 或全 1 数组，还可以使用 numpy.random 模块生成随机数组等。除了基本操作之外，NumPy 还提供了许多高级的数组
# 操作，例如数组切片、数组索引、数组重塑、数组转置、数组拼接和分裂等。

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from matplotlib import cm

import os

# 如果文件夹不存在，创建文件夹
if not os.path.isdir("Figures"):
    os.makedirs("Figures")

# 定义二维数组可视化函数
def visualize_2D(array, title, vmax, vmin):

    fig_width = math.ceil(array.shape[1] * 0.5)
    fig_length = math.ceil(array.shape[0] * 0.5)

    fig, ax = plt.subplots(figsize=(fig_width, fig_length))
    # 注意，seaborn.heatmap() 目前只能接受2D数组
    # 本书中，一维数组可视化时用圆圈
    # 可视化时，只有二维、三维数组用方块

    sns.heatmap(array,
                vmax=vmax,
                vmin=vmin,
                annot=True,      # 增加注释
                fmt=".0f",       # 注释数值的格式
                square=True,     # 热图方格为正方形
                cmap='RdYlBu_r',  # 指定色谱
                linewidths=.5,   # 方格线宽
                cbar=False,      # 不显示色谱条
                yticklabels=False,  # 不显示纵轴标签
                xticklabels=False,  # 不显示横轴标签
                ax=ax)           # 指定绘制热图的轴

    fig.savefig('Figures/' + title + '.svg', format='svg')

# 定义绘制一元数组可视化函数
def visualize_1D(array, title):
    fig, ax = plt.subplots()

    colors = cm.RdYlBu_r(np.linspace(0, 1, len(array)))

    for idx in range(len(array)):
        circle_idx = plt.Circle(
            (idx, 0),
            0.5,
            facecolor=colors[idx],
            edgecolor='w')

        ax.add_patch(circle_idx)
        ax.text(
            idx, 0, s=str(array[idx]),
            horizontalalignment='center',
            verticalalignment='center')

    ax.set_xlim(-0.6, 0.6 + len(array))
    ax.set_ylim(-0.6, 0.6)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    fig.savefig('Figures/' + title + '.svg', format='svg')


# 手动生成一维数组
print('------ 1D Array -----')
a_1D = np.array([-3, -2, -1, 0, 1, 2, 3])
print(a_1D)
print(a_1D.shape)
print(len(a_1D))
print(a_1D.ndim)
print(a_1D.size)
visualize_1D(a_1D, '1D Array')

# 手动生成二维数组
print('------ 2D Array -----')
a_2D = np.array([[-3, -2, -1],
                 [0, 1, 2]])
print(a_2D)
print(a_2D.shape)
print(a_2D.shape[0])  # 行数
print(a_2D.shape[1])  # 列数
print(a_2D.ndim)
print(a_2D.size)
print(len(a_2D))
# 可视化
visualize_2D(a_2D, '2D Array', 3, -3)

# 手动生成二维数组
print('------ 3D Array -----')
a_3D = np.array([[[-12, -11, -10, -9],
                  [-8, -7, -6, -5],
                  [-4, -3, -2, -1]],
                 [[0, 1, 2, 3],
                  [4, 5, 6, 7],
                  [8, 9, 10, 11]]])
print(a_3D.shape)
print(a_3D.ndim)
# 可视化
visualize_2D(a_3D[0], '3D Array Page 1', 12, -12)
print(a_3D[0].shape)
visualize_2D(a_3D[1], '3D Array Page 2', 12, -12)
