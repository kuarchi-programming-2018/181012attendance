# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return b

fib(10)

print("n=2018のとき" + "f(n)=" + str(fib(2018)) + "である。")


