#Question Link: https://www.naukri.com/code360/problems/alpha-hill_6581921?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
"""
Alpha Hill

Problem Statement: Sam is curious about Alpha-Hills, so he decided to create Alpha-Hills of different sizes.
An Alpha-hill is represented by a triangle, where alphabets are filled in palindromic order.
For every value of ‘N’, help sam to return the corresponding Alpha-Hill.

Example:
Input: ‘N’ = 3

Output: 
    A
  A B A
A B C B A
"""

def alphaHill(n: int):
    for i in range(n):
        #for space before alphabet
        for j in range(2*n-2*i-2):
            print("",end=" ")
        #for  alphabet in increasing part
        alphabet = ord('A')
        for j in range(i+1):
            print(chr(alphabet),end=" ")
            alphabet += 1
        #for alphabet in decreasing part
        alphabet -= 2
        for j in range(i):
            print(chr(alphabet),end=" ")
            alphabet -= 1
        #for space after alphabet
        for j in range(2*n-2*i-2):
            print("",end=" ")
        print("")
    pass
