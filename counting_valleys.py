#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_lvl = 0
    count = 0

    for step in s:
        #print(step)
        #print(type(step))
        if step == 'U':
            sea_lvl = sea_lvl + 1
            #print(sea_lvl)
        elif step == 'D':
            sea_lvl = sea_lvl - 1
            #print(sea_lvl)

        if sea_lvl > 0:
            climb_type = 'M'
            #print(climb_type)
        elif sea_lvl < 0:
            climb_type = 'V'
            #print(climb_type)
        elif sea_lvl == 0:
            if climb_type == 'V':
                count = count + 1
                #print(count)
            else:
                continue
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    #fptr.write(str(result) + '\n')

    #fptr.close()

    print(result)
