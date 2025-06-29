#Question Link: https://www.naukri.com/code360/problems/increasing-number-triangle_6581893?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
"""
Increasing Number Triangle

Problem Statement: Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Increasing Number Triangle.

Example:
Input: ‘N’ = 3

Output: 
1
2 3
4 5 6
"""

def nNumberTriangle(n: int) -> None:
    num = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(num,end=" ")
            num += 1
        print("")
    pass
