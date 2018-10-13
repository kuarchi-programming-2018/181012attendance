# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n - 1):
            c = a + b
            a = b
            b = c
        return c


#この n に2以上の整数を代入してください
n = 2018
print("F(" + str(n) + ")=" + str(fib(n)))

#F(2018) の具体的な値は入りきらないので省略します