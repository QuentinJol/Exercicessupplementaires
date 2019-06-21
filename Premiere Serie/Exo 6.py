# -*- coding: utf8 -*-

A=0
B=1
C=0
i=0

while i != 10:
    C=A+B
    print(A, " + ", B, " = ", C)
    A=B
    B=C
    i += 1

