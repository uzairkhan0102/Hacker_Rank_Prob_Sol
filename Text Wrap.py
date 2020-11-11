
'''

You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.

Input Format

The first line contains a string, S.
The second line contains the width, w.

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''


def wrap(string, max_width):
    dedented_text = textwrap.dedent(string).strip()
    return(textwrap.fill(dedented_text, width=max_width))


    

