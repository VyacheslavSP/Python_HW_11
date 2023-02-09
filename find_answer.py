import math
import numpy
import matplotlib.pyplot as plt


def find_above_below_zero(input_range):
    func_above_zero_y = []
    func_above_zero_x = []
    func_below_zero_y = []
    func_below_zero_x = []
    func_above = []
    func_below = []
    data = build(input_range)
    for element in data:

        if (element > 0):
            func_above_zero_x.append(input_range[data.index(element)])
            func_above_zero_y.append(element)
        else:
            func_below_zero_x.append(input_range[data.index(element)])
            func_below_zero_y.append(element)

    func_above.append(func_above_zero_x)
    func_above.append(func_above_zero_y)
    func_below.append(func_below_zero_x)
    func_below.append(func_below_zero_y)

    return func_above, func_below,


def build(input_range):
    global data
    data = []
    for element in input_range:
        data.append((-12*element ** 4*math.sin(math.cos(element)) -
                     18*element ** 3+5*element**2+10*element-30))
    return data


def find_extrem(input_range, data):
    extr_y = []
    extr_x = []
    tmp = None
    i = 1
    while i in range(len(input_range)-1):
        if (data[i+1] < data[i] > data[i-1]):
            tmp = data[i]
            extr_y.append(tmp)
            extr_x.append(input_range[i])
            i += 1
        elif (data[i+1] > data[i] < data[i-1]):
            tmp = data[i]
            extr_y.append(tmp)
            extr_x.append(input_range[i])
            i += 1
        else:
            i += 1
    return extr_y, extr_x


def radix(input_range, data):
    radix_x = []
    i = 1
    while i in range(len(input_range)-1):
        # пи=3. Фу,как грубо.Более корректного решения в графической форме не нашел. Алтернатива-матеметическое вычисление коней
        if (data[i-1] < 0 < data[i] or data[i-1] > 0 > data[i]):
            radix_x.append(input_range[i])
            i += 1
        else:
            i += 1
    return radix_x


# графический способ решения- разбей на участки межу экстемумами
def find_growth(input_range, data, extr_y):
    tmp_line_grown_y = []
    tmp_line_grown_x = []
    tmp_line_fall_y = []
    tmp_line_fall_x = []
    line_grown_y = [[]]
    line_grown_x = [[]]
    line_fall_y = [[]]
    line_fall_x = [[]]
    i = 0
    j = 0
    k = 1
    l = 0
    m = 1
    n = 0
    while i in range(len(input_range)-1):
        if (data[i] < extr_y[j]):
            tmp_line_grown_y.append(data[i])
            tmp_line_grown_x.append(input_range[i])
            i += 1
        elif (data[i] > extr_y[j]):
            tmp_line_fall_y.append(data[i])
            tmp_line_fall_x.append(input_range[i])
            i += 1
        if (data[i] == extr_y[j]):
            if (j+1 < len(extr_y)):
                j += 1
            i += 1
    while k in range(len(tmp_line_grown_y)-1):
        # если разрыв меньше 2х точек
        if (tmp_line_grown_x[k]-tmp_line_grown_x[k-1] < (input_range[1]-input_range[0])*2):

            line_grown_y[l].append(tmp_line_grown_y[k])
            line_grown_x[l].append(tmp_line_grown_x[k])
            k += 1
        else:
            line_grown_y.append(list(''))
            line_grown_x.append(list(''))
            l += 1
            k += 1
    while m in range(len(tmp_line_fall_y)-1):
        # если разрыв меньше 2х точек
        if (tmp_line_fall_x[m]-tmp_line_fall_x[m-1] < (input_range[1]-input_range[0])*2):

            line_fall_y[n].append(tmp_line_fall_y[m])
            line_fall_x[n].append(tmp_line_fall_x[m])
            m += 1
        else:
            line_fall_y.append(list(''))
            line_fall_x.append(list(''))
            n += 1
            m += 1
    return (line_grown_y, line_grown_x, line_fall_y, line_fall_x)
