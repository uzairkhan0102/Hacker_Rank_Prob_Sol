
'''

Integers in Python can be as big as the bytes in your machine's memory.
There is no limit in size as there is: 2^31 -1 (c++ int) or 2^63 -1
(C++ long long int).

As we know, the result of a^b grows really fast with increasing b.

Let's do some calculations on very large integers.

Task
Read four numbers, a, b, c, and d, and print the result of a^b+c^d.

Input Format
Integers a, b, c, and d are given on four separate lines, respectively.

Constraints




Output Format
Print the result of a^b + c^d on one line.

Sample Input

9
29
7
27
Sample Output

4710194409608608369201743232

Note: This result is bigger than 2^63 -1.
Hence, it won't fit in the long long int of C++ or a 64-bit integer.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

line = sys.stdin.readlines()

#a = pow(int(line[0]),int(line[1]))
#a= pow(999,999)
#b= pow(999,999)
a = pow(int(line[0]),int(line[1]))
b = pow(int(line[2]),int(line[3]))
print(a+b)
#print(line[0])
#print(line[2:4])
#print(line[5:6])
#print(line[7:])
