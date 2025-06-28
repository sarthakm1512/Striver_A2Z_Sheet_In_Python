#Question Link: https://www.naukri.com/code360/problems/star-diamond_6573686?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
"""
Star Diamond

Problem Statement: Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.

Example:
Input: ‘N’ = 3

Output: 
  *
 ***
*****
*****
 ***
  *
"""

def nStarDiamond(n: int) -> None:
    for i in range(n):
        for j in range(n-i-1):
            print("",end=" ")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print("",end=" ")
        print("")
    for i in range(n):
        for j in range(i):
            print("",end=" ")
        for j in range(2*n-2*i-1):
            print("*",end="")
        for j in range(i):
            print("",end=" ")
        print("")
    pass
