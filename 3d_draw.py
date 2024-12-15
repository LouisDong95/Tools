import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# file
dataset = 'Reuters'
file = '../results/Reuters/param2.csv'
metrics = 'ACC'
para1 = [0.1, 0.5, 1.0, 5.0, 10.0] # x-axis
para2 = [0.1, 0.3, 0.5, 0.7, 0.9] # y-axis

x = list(range(len(para1)))
y = list(range(len(para2)))
x_tickets = [str(_x) for _x in para1]
y_tickets = [str(_y) for _y in para2]
data = pd.read_csv(file)
acc = data[metrics].to_numpy().reshape(len(x), len(y))
xx, yy = np.meshgrid(x, y)

color_list = []
COLOR = ["blue", "cornflowerblue", "mediumturquoise", "goldenrod", "yellow"]
for i in range(len(y)):
    c = COLOR[i]
    color_list.append([c] * len(x))
color_list = np.asarray(color_list)

xx_flat, yy_flat, acc_flat, color_flat = xx.ravel(), yy.ravel(), acc.ravel(), color_list.ravel()

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.bar3d(xx_flat - 0.35, yy_flat - 0.35, 0, 0.7, 0.7, acc_flat,
         color=color_flat,  # 颜色
         edgecolor="black",  # 黑色描边
         shade=True)  # 加阴影

# 座标轴名
ax.set_ylabel(r"$\lambda$")
ax.set_xlabel(r"$\tau$")
ax.set_zlabel(metrics)

# 座标轴范围
ax.set_zlim((0, 1))
ax.set_xticks(y)
ax.set_xticklabels(y_tickets)
ax.set_yticks(x)
ax.set_yticklabels(x_tickets)

# 保存
fig.savefig("../results/%s/%s.svg" %(dataset, metrics), bbox_inches='tight', pad_inches=0.3)
plt.close(fig)