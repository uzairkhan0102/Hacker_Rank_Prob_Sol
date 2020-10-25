'''

This tool returns the R length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order.
So, if the input iterable is sorted, the combination tuples will
be produced in sorted order.

Sample Code

>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

Task

You are given a string S.
Your task is to print all possible combinations, up to size k,
of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value K separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
import sys

#s , n  = sys.stdin.readlines().split()

word = sys.stdin.readlines()
word = str(word)
res = word.split(' ')
#res = [i for j in word.split() for i in (j, ' ')][:-1] 
word = res[0]
no = res[1]

word1 = list(word[2:])
num = int (no[:-2])

for i in range(1, int(num)+1):
    for j in combinations(sorted(word1), i):
        print (''.join(j))
'''        
word = sys.stdin.readlines()
word = str(word)
res = word.split(' ')
#res = [i for j in word.split() for i in (j, ' ')][:-1] 
word = res[0]
no = res[1]

word1 = list(word[2:])
num = int (no[:-2])
#print(word1,num)
#wordlist = [ch for ch in s] 
my = list(combinations(word1,num))
my.sort()
#print (my)
print('\n'.join(map(str, my)))
#for x in range(len(my)): 
#    print (my[x]) 
'''
