
'''


Staircase detail

This is a staircase of size n =4:

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces.
The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.

Function Description

Complete the staircase function in the editor below.

staircase has the following parameter(s):

int n: an integer
Print

Print a staircase as described above.

Input Format

A single integer,n , denoting the size of the staircase.

Constraints

 .

Output Format

Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces in it.

Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######

Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .
'''



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):

    k = n-1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
        for j in range(0, i+1): 
          
            # printing stars 
            print("#", end="") 
      
        # ending line after each row 
        print("\r") 

if __name__ == '__main__':
    n = int(input())

    staircase(n)
