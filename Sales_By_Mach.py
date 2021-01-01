#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    parejas = 0
    colores = set()
    for i in ar:
        if i not in colores:
            colores.add(i)
        else:
            parejas = parejas + 1
            colores.remove(i)
    return parejas

if __name__ == '__main__':
    n = 7;
    ar = [10,20,20,10,10,30,50,10,20]
    result = sockMerchant(n,ar)
    print(str(result))