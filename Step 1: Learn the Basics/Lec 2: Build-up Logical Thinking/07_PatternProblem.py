#Question Link: https://www.naukri.com/code360/problems/star-triangle_6573671?leftPanelTabValue=PROBLEM
"""
Star Triangle

Problem Statement: Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 
  *
 ***
*****
"""

def nStarTriangle(n: int) -> None:
    for i in range(n):
        #for loop for space before stars
        for j in range(n-i-1):
            print("",end=" ")
        #for loop for stars
        for j in range(2*i+1):
            print("*",end="")
        #for loop for space after stars
        for j in range(n-i-1):
            print("",end=" ")
        print("")
    pass 
