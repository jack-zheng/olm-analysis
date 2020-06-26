import matplotlib
from matplotlib import pyplot as plt


# 显示中文
# Windows/Linus
font = {'family' : 'MicroSoft Yahei', 'weight': 'bold', 'size': '9'}
matplotlib.rc("font", **font)

# 设置图片 大小 20x8
fig = plt.figure(figsize=(20, 8), dpi=80)

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游降魔篇", "变形金刚5", "最后的骑士", "摔跤吧 爸爸", "加勒比海盗5",
"死无对证", "金刚", "骷髅岛", "极限特工-最终回归", "生化危机6", "乘风破浪", "神偷奶爸", "智取威虎山", "大闹天竺", "金刚狼3",
"殊死一战", "蜘蛛侠"]

b = [56.01, 26.93, 17.53, 16.49, 15.45, 12.98, 11.8, 11.61, 11.26, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]

plt.barh(a, b, height=0.3)

# 添加描述信息
plt.xlabel("电影名")
plt.ylabel("票房")
plt.title("票房榜")

plt.grid(alpha=0.3)

plt.show()