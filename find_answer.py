import math
import numpy


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
