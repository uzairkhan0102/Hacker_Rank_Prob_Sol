

'''
Given an array of integers, calculate the ratios of its elements that
are positive, negative, and zero. Print the decimal value of
each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to
six decimal places,though answers with absolute error of up to  are acceptable.

Example
arr = [1,1,0,1,1]
There are n=5  elements, two positive, two negative and one zero.
Their ratios are 2/5=0.400, 2/5=0.400, 1/5=0.200  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n] .

Constraints



Output Format

Print the following 3 lines, each to 6 decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: 3/6 = 0.5000 ,
negative: 2/6 = 0.3333  and zeros: 1/6 = 0.1666.

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    total = len(arr)
    posi = 0
    nega = 0
    zero = 0

    for i in range(0 , total):
        if arr[i] > 0:
            posi = posi + 1
        elif arr[i] < 0:
            nega = nega + 1
        elif arr[i] == 0:
            zero = zero + 1

    positive = posi/total
    negative = nega/total
    zeros = zero/total

    print (positive)
    print (negative)
    print (zeros)
    #return positive,negative,zeros

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
