#Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):\n",
#zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],\n",
#ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].\n",
#Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy##Полученные значения должны быть равны.
#Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
#а затем с использованием функций из библиотек numpy и pandas."


import numpy as np
import matplotlib.pyplot as plt


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
print(zp)
ks = np.array( [401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
print(ks)

plt.scatter(zp, ks)
plt.show()


