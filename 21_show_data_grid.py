# https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484538&idx=1&sn=d9b614201c96ad283bbad8a867d42082&scene=19#wechat_redirectimport numpy as np
import numpy as np
from matplotlib import pyplot

x = np.linspace(-np.pi, np.pi, 256)

cos = np.cos(x)
sin = np.sin(x)

pyplot.plot(x, cos, '--', linewidth=2)
pyplot.plot(x, sin)

pyplot.show()


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = pyplot.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

pyplot.show()