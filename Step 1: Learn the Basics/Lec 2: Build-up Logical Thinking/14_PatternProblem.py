#Question Link: https://www.naukri.com/code360/problems/increasing-letter-triangle_6581897?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
"""
Increasing Letter Triangle

Problem Statement: Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Increasing Letter Triangle.

Example:
Input: ‘N’ = 3

Output: 
A
A B
A B C
"""

def nLetterTriangle(n: int) -> None:
    for i in range(n):
        alphabet = ord('A')
        for j in range(i+1):
            print(chr(alphabet),end=" ")
            alphabet += 1
        print("")
    pass
