import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

# 加载鸢尾花数据集
iris = datasets.load_iris()

# 取出前三个特征作为横纵坐标和高度
X = iris.data[:, :3]
y = iris.target

# 创建3D图像对象
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 绘制散点图
ax.scatter(X[:,0], X[:,1], X[:,2], c=y)
# 设置坐标轴标签
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')
# 设置坐标轴取值范围
ax.set_xlim(4,8) 
ax.set_ylim(1,5)
ax.set_zlim(0,8)
# 设置正交投影
ax.set_proj_type('ortho')

plt.show()