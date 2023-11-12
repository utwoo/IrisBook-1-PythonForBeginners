import matplotlib.pyplot as plt
import numpy as np

# 生成曲面数据
x = np.linspace(-3, 3, 121)
y = np.linspace(-3, 3, 121)

X, Y = np.meshgrid(x, y)
Z = X * np.exp(-X**2 - Y**2)

fig = plt.figure()

# =============
# First subplot
# =============
# 用 Matplotlib 可视化三维曲面
ax = fig.add_subplot(121, projection='3d')

ax.plot_surface(X, Y, Z, cmap='RdYlBu_r')

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

# ==============
# Second subplot
# ==============
# 用 Matplotlib 可视化三维线框
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.view_init(elev=30, azim=150)

plt.show()
