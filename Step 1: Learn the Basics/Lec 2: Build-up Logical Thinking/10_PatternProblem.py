#Question Link: https://www.naukri.com/code360/problems/rotated-triangle_6573688?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
"""
Rotated Triangle

Problem Statement: Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Rotated Triangle.

Example:
Input: ‘N’ = 3

Output: 
*
**
***
**
*
"""

def nStarTriangle(n: int) -> None:
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for j in range(n-i-1):
            print("",end=" ")
        print("")
    for i in range(n-1):
        for j in range(n-i-1):
            print("*",end="")
        for j in range(i+1):
            print("",end=" ")
        print("")
    pass
