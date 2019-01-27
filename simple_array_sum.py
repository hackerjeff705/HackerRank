#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    sum = 0
    for num in ar:
        sum += num
    return(sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    #print(ar)

    result = simpleArraySum(ar)

    #print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
