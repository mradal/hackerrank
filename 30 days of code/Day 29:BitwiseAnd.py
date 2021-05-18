#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'bitwiseAnd' function below.
def bitwiseAnd(N,K):
    mx=0
    for i in range(1,N+1):
        for j in range(1,i):
            b=i&j
            if mx<b<K:
                mx=b
                if mx==K-1:
                    return mx
    return mx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
