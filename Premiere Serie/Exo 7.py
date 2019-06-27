# -*- coding: utf8 -*-


def fibo_recursive(n):
        if (n <= 1):
                return n
        else:
                return fibo_recursive(n-1) + fibo_recursive(n-2)
         

for i in range (2, 11):
        print(fibo_recursive(i))
 