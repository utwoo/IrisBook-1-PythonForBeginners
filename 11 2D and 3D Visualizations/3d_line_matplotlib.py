import matplotlib.pyplot as plt
import numpy as np

# 生成随机游走数据
num_steps = 300
t = np.arange(num_steps)
x = np.cumsum(np.random.standard_normal(num_steps))
y = np.cumsum(np.random.standard_normal(num_steps))
z = np.cumsum(np.random.standard_normal(num_steps))

# 创建3D图像对象
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 绘制线图
ax.plot(x,y,z, color='darkblue')
# 绘制散点图
ax.scatter(x,y,z, c=t, cmap='viridis')
# 设置坐标轴标签
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
# 设置相机视角
ax.view_init(elev = 30, azim = 120)
# 设置正交投影
ax.set_proj_type('ortho')

plt.show()