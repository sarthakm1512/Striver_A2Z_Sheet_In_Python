#Question Link: https://www.naukri.com/code360/problems/reverse-number-triangle_6581889?leftPanelTabValue=PROBLEM
"""
Reverse Number Triangle

Problem Statement: Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the Reverse N-Number Triangle.

Example:
Input: ‘N’ = 3

Output: 

1 2 3
1 2
1
"""

def nNumberTriangle(n: int) -> None:
    
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j, end=" ")
        print("")
    pass
