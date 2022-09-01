# -*- coding: utf-8 -*-
def Sumas(a):
    suma = 0
    while(a>=1):
        suma+=a
        a=a-1
    return suma

b=Sumas(4)

print(b)