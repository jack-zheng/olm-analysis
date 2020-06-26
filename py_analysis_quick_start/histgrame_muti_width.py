import matplotlib
from matplotlib import pyplot as plt

# 数据分组： 总数<100, 分成 5-12 组

# 显示中文
# Windows/Linus
font = {'family' : 'MicroSoft Yahei', 'weight': 'bold'}
matplotlib.rc("font", **font)

# 没有处理过的原始连续数据才能被画成直方图，这种处理过的不行, 直接用 bar 来画
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

plt.figure(figsize=(20, 8), dpi=80)
plt.bar(range(12), quantity, width=1)

# 设置 x 刻度
_x = [i-0.5 for i in range(13)]
_xtick_labels = interval + [150]
plt.xticks(_x, _xtick_labels)

plt.grid(alpha=0.4)
plt.show()