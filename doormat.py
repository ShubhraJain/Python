"""
Mat size must be NXM. (N is an odd natural number, and M is 3 times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Input Format:
A single line containing the space separated values of  and .

Output Format
Output the design pattern.

Sample Input
9 27
Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""

N, M = map(int,input().split()) 
for i in range(1,N,2): 
    print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')
print('WELCOME'.center(M, '-'))
for i in range(N-2,-1,-2): 
    print(((M-3*i)//2)*'-'+i*'.|.'+((M-3*i)//2)*'-')