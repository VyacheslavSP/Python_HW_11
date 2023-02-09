

import matplotlib.pyplot as plt
import find_answer
import math
import numpy
# f(x)=-12*x^4*sin(cos(x))-18*x^2+10*x-30
# x = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = numpy.linspace(-15.00000, 15.000000, num=10000)

func_increases = []
func_decreasing = []
extrem = []
func_above_zero = []
func_below_zero = []
func_above = find_answer.find_above_below_zero(x)[0]
func_below = find_answer.find_above_below_zero(x)[1]
data = find_answer.build(x)
fig = plt.figure()
# plt.plot(x, full_graph)
extrem = find_answer.find_extrem(x, data)
radix = find_answer.radix(x, data)
tmp_arr_y = [0] * len(radix)
plt.scatter(func_above[0], func_above[1], marker="D", s=1)
plt.scatter(func_below[0], func_below[1], marker="D", s=1)
plt.scatter(extrem[1], extrem[0])
plt.scatter(radix, tmp_arr_y)
growth_y = find_answer.find_growth(
    x, data, extrem[0])[0]

growth_x = find_answer.find_growth(x, data, extrem[0])[1]

fall_y = find_answer.find_growth(x, data, extrem[0])[2]

fall_x = find_answer.find_growth(x, data, extrem[0])[3]
i = 0
j = 0
while (i < len(growth_y)):
    plt.plot(growth_x[i], growth_y[i],  'y--')
    i += 1
while (j < len(fall_y)):
    plt.plot(fall_x[j], fall_y[j],  'm--')
    j += 1
plt.grid(True)

plt.show()
