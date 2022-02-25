#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    
    last_value = arr[-1]
    
    index = len(arr) -2
    
    while arr[index] > last_value and index >= 0:
        
        arr[index+1] = arr[index]
        
        print(' '.join(map(str, arr)))

        index -=1
    
    arr[index+1] = last_value
    print(' '.join(map(str, arr)))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    insertionSort1(n, arr)
