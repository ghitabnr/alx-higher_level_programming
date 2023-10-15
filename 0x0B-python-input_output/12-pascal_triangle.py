#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n):
    """pascal_triangle"""
    ma_list = []
    for i in range(n):
        ma_list.append([])
        for j in range(i+1):
            try:
                if j - 1 == -1:
                    ma_list[i].append(1)
                else:
                    ma_list[i].append(ma_list[i-1][j-1] + ma_list[i-1][j])
            except IndexError:
                ma_list[i].append(1)
    return (ma_list)
