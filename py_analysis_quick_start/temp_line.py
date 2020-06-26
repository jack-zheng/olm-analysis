import random
import matplotlib
from matplotlib import pyplot as plt

# 显示中文
# Windows/Linus
font = {'family' : 'MicroSoft Yahei', 'weight': 'bold', 'size': '9'}
matplotlib.rc("font", **font)

# 设置图片 大小 20x8
fig = plt.figure(figsize=(20, 8), dpi=80)

y = [random.randint(20, 35) for i in range(120)]
x = range(120)

plt.plot(x, y)

# 调整 x 轴刻度
_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]
# 将 x 和 labels 一一绑定； rotation 旋转 label
plt.xticks(list(x)[::3], _xticks_labels[::3], rotation=45)

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 'C")
plt.title("10点到12点温度变化")

# 展示
plt.show()