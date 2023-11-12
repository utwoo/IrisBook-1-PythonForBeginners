import matplotlib.pyplot as plt
import numpy as np

# 生成曲面数据
x = np.linspace(-3, 3, 121)
y = np.linspace(-3, 3, 121)

X, Y = np.meshgrid(x, y)
Z = X * np.exp(-X**2 - Y**2)

fig = plt.figure()

# 生成曲面数据
ax = fig.add_subplot(projection='3d')
ax.contour(X, Y, Z, cmap='RdYlBu_r', levels=20)

# 设置坐标轴标签
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1,x2)')
# 设置坐标轴取值范围
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-0.5, 0.5)
# 设置正交投影
ax.set_proj_type('ortho')
# 设置相机视角
ax.view_init(elev=30, azim=150)

plt.show()
