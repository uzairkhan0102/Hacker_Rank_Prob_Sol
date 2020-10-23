
'''
There is an array of  integers. There are also 2 disjoint sets,
A and B, each containing M integers. You like all the integers in
set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i e A, you add 1 to your happiness.
If i re B, you add -1 to your happiness. Otherwise, your happiness
does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements.
However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers n and m separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
#import re

n, m = input().split()

sc_ar = input().split()

A = set(input().split())

B = set(input().split())

print(sum([(i in A) - (i in B) for i in sc_ar]))
'''
n,sc_ar,set(A),set(B)  = sys.stdin.readlines()

#print (sc_ar)
#print (A)
#print (B)
print (sum([(i in A) - (i in B) for i in sc_ar]))




inp = sys.stdin.readlines()

inp1 = str(inp)
inp2 = inp1.split(',')


sc_ar = str(inp2[1])
A = str(inp2[2])
B = inp2[3]
sum1 =0
sum2 = 0
sc_ar = re.findall(r'\d+', sc_ar)
A = re.findall(r'\d+', A)
B = re.findall(r'\d+', B)
#print (sum([(i in A) - (i in B) for i in sc_ar]))


for i in sc_ar:
    if i in A:
        sum1 = sum1+1
        #print('A=',sum1)
    if i in B:
        sum2 = sum2+1

print(sum1-sum2)
'''

