#Question Link: https://www.naukri.com/code360/problems/reverse-star-triangle_6573685?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
"""
Reverse Star Triangle

Problem Statement: Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 
*****
 ***
  *
"""

def nStarTriangle(n: int) -> None:
    for i in range(n):
        #for loop for space before stars
        for j in range(i):
            print("",end=" ")
        #for loop for stars
        for j in range(2*n-2*i-1):
            print("*",end="")
        #for loop for space after stars
        for j in range(i):
            print("",end=" ")
        print("")
    pass
