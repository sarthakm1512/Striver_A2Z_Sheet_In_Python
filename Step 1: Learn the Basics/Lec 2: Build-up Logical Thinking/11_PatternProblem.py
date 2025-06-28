#Question Link: https://www.naukri.com/code360/problems/binary-number-triangle_6581890?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
"""
Binary Number Triangle

Problem Statement: Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the N-Binary Number Triangle.
You are required to print the pattern as shown in the examples below.

Example:
Input: ‘N’ = 3

Output: 
1
0 1
1 0 1
"""

def nBinaryTriangle(n: int) -> None:
    for i in range(n):
        if (i%2==0):
            a=1
        else:
            a=0
        for j in range(i+1):
            print(a,end=" ")
            a=1-a
        print("")
    pass
