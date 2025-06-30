#Question Link: https://www.naukri.com/code360/problems/reverse-letter-triangle_6581906?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
"""
Reverse Letter Triangle

Problem Statement: Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Reverse Letter Triangle.
You must print a matrix corresponding to the given Reverse Letter Triangle.

Example:
Input: ‘N’ = 3

Output: 
A B C
A B
A
"""

def nLetterTriangle(n: int):
    for i in range(n):
        alphabet = ord('A')
        for j in range(n-i):
            print(chr(alphabet),end=" ")
            alphabet += 1
        print("")
    pass
