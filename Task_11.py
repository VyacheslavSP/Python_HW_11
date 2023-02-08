

import matplotlib.pyplot as plt
import find_answer
import math
import numpy
# f(x)=-12*x^4*sin(cos(x))-18*x^2+10*x-30
# x = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = numpy.linspace(-15.00000, 15.000000, num=10000)
full_graph = []
func_increases = []
func_decreasing = []
extrem = []
func_above_zero = []
func_below_zero = []
func_above = find_answer.find_above_below_zero(x)[0]
func_below = find_answer.find_above_below_zero(x)[1]
data = find_answer.build(x)
for element in x:
    full_graph.append((-12*element ** 4*math.sin(math.cos(element)) -
                       18*element ** 3+5*element**2+10*element-30))
fig = plt.figure()
# plt.plot(x, full_graph)
extrem = find_answer.find_extrem(x, data)
radix = find_answer.radix(x, data)
tmp_arr_y = [0] * len(radix)
plt.scatter(func_above[0], func_above[1])
plt.scatter(func_below[0], func_below[1])
plt.scatter(extrem[1], extrem[0])
plt.scatter(radix, tmp_arr_y)
plt.grid(True)

plt.show()
