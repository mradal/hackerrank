#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    b=0
    for i in range(n):
        numberOfSwaps=0
        for j in range(n-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
                numberOfSwaps+=1
        if numberOfSwaps==0:
            break
        else:
            b+=numberOfSwaps
    print("Array is sorted in %d swaps."%(b))
    print("First Element:", a[0])
    print("Last Element:", a[n-1])
