import random
import matplotlib
from matplotlib import pyplot as plt

# 显示中文
# Windows/Linus
font = {'family' : 'MicroSoft Yahei', 'weight': 'bold', 'size': '9'}
matplotlib.rc("font", **font)

# 设置图片 大小 20x8
fig = plt.figure(figsize=(20, 8), dpi=80)

y = [random.randint(0, 4) for i in range(20)]
x = range(11, 31)

plt.plot(x, y)

# 调整 x 轴刻度
_xticks_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xticks_labels)
plt.yticks(range(0, 6))

# 添加描述信息
plt.xlabel("年龄")
plt.ylabel("个数")
plt.title("朋友数")

# 画网格, alpha 透明度
plt.grid(alpha=0.4)

# 展示
plt.show()