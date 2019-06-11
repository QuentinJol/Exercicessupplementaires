# -*- coding: utf8 -*-

# Les 100 premiers entiers

entiers=range(1, 101)

i=1
j=0

while i < 101:
    print(entiers[j], "*", entiers[j], "=", entiers[j]*entiers[j])
    i += 1
    j += 1



print("Finish !")