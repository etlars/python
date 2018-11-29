# -*- coding:utf-8 -*-

from functools import reduce

def Result(x , y) :
    return x if x<y else y
    
    
l = [ 8 , 9 , 9 , 4 , 5 , 9, 3  , 2 , 1 ]
ret =reduce(Result,l)
print (ret)
