


'''
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given  scores.
Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array  A of n integers
each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5.
Hence, we print 5 as the runner-up score.

'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    list1 = list(arr)
    list1.sort()

    size = len(list1)
    a = list1[-1]

    while size>0:

        b = list1[size-1]

        if b < a:
            print (b)
            break
        else:
            size = size-1



    #for i in range(size,0):
     #   if a < list1[-i]:
      #      print (a)
       #     break


