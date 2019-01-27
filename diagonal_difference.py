#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    print(a, b)
    tot_a = 0
    tot_b = 0
    for a_n, b_n in zip(a,b):
        print(a_n, b_n)
        if a_n > b_n:
            tot_a = tot_a + 1
        elif b_n > a_n:
            tot_b = tot_b + 1
        else:
            tot_a = tot_a + 0
            tot_b = tot_b + 0
        #print(tot_a, tot_b)
        return(tot_a, tot_b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
