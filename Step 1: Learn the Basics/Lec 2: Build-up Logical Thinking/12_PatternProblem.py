#Question Link: https://www.naukri.com/code360/problems/number-crown_6581894?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
"""
Number Crown

Problem Statement: Aryan and his friends are very fond of the pattern. They want to make the Reverse N-Number Crown for a given integer' N'.
Given 'N', print the corresponding pattern.

Example:
Input: ‘N’ = 3

Output: 
1         1 
1 2     2 1 
1 2 3 3 2 1 
"""

def numberCrown(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(4*n-4*i):
            print("",end=" ")
        for j in range(i,0,-1):
            print(j,end=" ")
        print("")
    pass
