import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# From file
# results = pd.read_csv('')
# acc = results['ACC']
# nmi = results['NMI']

# demo
Ours_acc = [0.527, 0.505, 0.490, 0.46, 0.436]
Ours_nmi = [0.477, 0.471, 0.473, 0.434, 0.411]


x = np.arange(0.1, 1.0, 0.2)

# 绘图
plt.plot(x, Ours_acc, color='red', label='Ours')
plt.plot(x, Ours_nmi, color='blue', label='DIVDIE')

# 设置主要刻度
major_ticks = x  # 仅显示这些主要刻度
plt.gca().xaxis.set_major_locator(ticker.FixedLocator(major_ticks))
# 关闭次要刻度和次要网格线
plt.gca().xaxis.set_minor_locator(ticker.NullLocator())  # 不显示次要刻度
plt.grid(True, which='major', linestyle='--', linewidth=0.5)  # 仅显示主要网格线
# 添加图例
plt.legend()

# 添加标题和标签
plt.ylim(0.3, 0.6)
plt.xlabel('Missing rate')
plt.ylabel('NMI')
x_major_locator = plt.MultipleLocator(0.2)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.xticks(x)

plt.savefig("", bbox_inches='tight', pad_inches=0)
