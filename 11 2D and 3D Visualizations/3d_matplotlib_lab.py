import matplotlib.pyplot as plt

# 创建一个新的图形窗口
fig = plt.figure()

# 在图形窗口中添加一个3D坐标轴子图
ax = fig.add_subplot(projection='3d')
# 设置坐标轴的标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# 设置投影类型为正交投影 ('ortho')
# 透视投影(persp)
ax.set_proj_type('persp')
# 设置观察者的仰角为30度，方位角为30度，即改变三维图形的视角
ax.view_init(elev=30, azim=30)
# 设置三个坐标轴的比例一致，使得图形在三个方向上等比例显示
ax.set_box_aspect([1,1,1])

plt.show()