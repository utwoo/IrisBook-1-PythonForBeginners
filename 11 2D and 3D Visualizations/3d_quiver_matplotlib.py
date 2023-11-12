import matplotlib.pyplot as plt

# 定义二维列表
A = [[0, 5],
     [3, 4],
     [5, 0]]

# 自定义可视化函数
def draw_vector_3D(vector, RGB):
    plt.quiver(0, 0, 0,             # 箭头的起点坐标
               vector[0],           # 箭头在 x 轴上的分量
               vector[1],           # 箭头在 y 轴上的分量
               vector[2],           # 箭头在 z 轴上的分量
               # 箭头的长度应该乘以的比例因子(0表示箭头的长度将被设置为一个合适的长度，不乘以比例因子)
               arrow_length_ratio=0,
               color=RGB,           # 箭头的颜色
               zorder=1e5)          # 图层序号


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(projection='3d', proj_type='ortho')

# 第一列向量
v1 = [row[0] for row in A] # [0, 3, 5]
draw_vector_3D(v1, '#FF6600')
# 第二列向量
v_2 = [row[1] for row in A] # [5, 4, 0]
draw_vector_3D(v_2,'#FFBBFF')

# 设置轴范围
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(0,5)
# 设置坐标轴的标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# 设置观察者的仰角为30度，方位角为30度，即改变三维图形的视角
ax.view_init(elev = 30, azim = 30)
# 设置三个坐标轴的比例一致，使得图形在三个方向上等比例显示
ax.set_box_aspect([1,1,1])

plt.show()
