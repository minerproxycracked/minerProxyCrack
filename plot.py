#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt


def author_fee(x):
    if x == 0:
        return 0
    if 0 < x <= 5:
        return 0.5
    if x <= 10:
        return 1
    if x <= 20:
        return 2
    return x


def main():
    x = np.linspace(0, 50, 10000)
    y = np.array(list(author_fee(d) for d in x))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(u'303阶梯抽水示意图')
    plt.xlabel(u'抽水')
    plt.ylabel(u'作者抽水')
    plt.xticks(range(0, 51, 5))
    plt.yticks(range(0, 51, 5))
    plt.plot(x, y, 'b')
    plt.show()


if __name__ == '__main__':
    main()
