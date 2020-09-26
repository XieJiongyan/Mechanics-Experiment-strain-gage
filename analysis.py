import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from matplotlib.pyplot import MultipleLocator

plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
df = pd.read_csv("Experiment1 strain gage/input/test1.csv")
# print(type(df))
# print(df)
# df.head()
# df.info()
print(df['sg1'])

#[1, 2, 3, 4]
rows = [i + 1 for i in np.arange(0, 4)]
cols = ['sg' + str(i) for i in np.arange(1, 7)]
print(cols)
print(rows)
for col in cols:
    plt.plot(rows, df[col])


# show
plt.legend(['应变片1','应变片2','应变片3','应变片4','应变片5','应变片6'])

x_major_locator = MultipleLocator(1)
ax=plt.gca()

ax.xaxis.set_major_locator(x_major_locator)

plt.xlabel('放置重物数量')
plt.ylabel('应变大小')
plt.title('第一次实验情况')

plt.show()

df2 = pd.read_csv("Experiment1 strain gage/input/test2.csv")

print(df['sg1'])

#[1, 2, 3, 4]
rows = [i + 1 for i in np.arange(0, 4)]
cols = ['sg' + str(i) for i in np.arange(1, 7)]
print(cols)
print(rows)
for col in cols:
    plt.plot(rows, df[col])


# show
plt.legend(['应变片1','应变片2','应变片3','应变片4','应变片5','应变片6'])

x_major_locator = MultipleLocator(1)
ax=plt.gca()

ax.xaxis.set_major_locator(x_major_locator)

plt.xlabel('放置重物数量')
plt.ylabel('应变大小')
plt.title('第二次实验情况')
plt.show()
