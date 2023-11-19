# 数列是指一列按照一定规律排列的数，它通常用一个公式来表示，也可以用递推关系式来定义。数列中的每个数称为数列的项，
# 用 an来表示第 n 项。数列在数学中具有广泛的应用，它是许多数学分支的基础，如数学分析、概率论、统计学、离散数学和计算
# 机科学等。在数学中，数列是一种有序的集合，通常用于研究数学对象的性质和行为，例如函数、级数、微积分和代数等。数列
# 可以分为等差数列、等比数列和通项公式不规则数列等几种类型。等差数列的项之间的差是固定的，比如 1、2、3、4 … 100。
# 等比数列的相邻项之间的比是固定的，比如 2、4、8、16 … 2048。

import numpy as np

print('---- np.array ----')
print(np.arange(5))
print(np.arange(5, dtype=float))
print(np.arange(10, 20))
print(np.arange(10, 20, 2))
print(np.arange(10, 20, 2, dtype=float))
print('---- np.linspace ----')
# 等差数列
print(np.linspace(0, 5, 11))
print('---- np.logspace ----')
# 等比数列
print(np.logspace(0, 4, 5, base=10))
print(np.logspace(0, 4, 5, base=2))
