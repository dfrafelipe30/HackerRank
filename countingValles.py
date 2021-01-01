#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    nivel = 0
    valles = 0
    for i in path:
        if i == "U":
            nivel += 1
        else:
            nivel -= 1
        if i == "U" and nivel == 0:
            valles += 1
    return valles

if __name__ == '__main__':
    
    s = "UDDDUDUU"
    n = 8
    result = countingValleys(n,s)
    print(result) 
