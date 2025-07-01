#Question Link: https://www.naukri.com/code360/problems/ninja-and-the-star-pattern-i_6581920?leftPanelTabValue=PROBLEM
"""
Ninja And The Star Pattern I

Problem Statement: Ninja has been given a task to print the required star pattern and he asked your help for the same.
You must return an ‘N’*’N’ matrix corresponding to the given star pattern.

Example:
Input: ‘N’ = 4

Output: 
****
*  *
*  *
****
"""

def getStarPattern(n: int) -> None:
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n-1 or j==n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    pass
