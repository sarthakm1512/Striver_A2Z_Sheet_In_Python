#Question Link: https://www.naukri.com/code360/problems/symmetry_6581914?leftPanelTabValue=PROBLEM
"""
Symmetry

Problem Statement: Sam is curious about symmetric patterns, so he decided to create one.
For every value of ‘N’, return the symmetry as shown in the example.

Example:
Input: ‘N’ = 3

Output: 
*         * 
* *     * * 
* * * * * * 
* *     * * 
*         * 
"""

def symmetry(n: int):
    #upper part with n
    for i in range(n):
        #for star:
        for j in range(i+1):
            print("*",end=" ")
        #for space:
        for j in range(n-i-1):
            print("  ",end=" ")
        #for star:
        for i in range(i+1):
            print("*",end=" ")
        print("")
    #lower part with n-1
    for i in range(n-1):
        #for star:
        for j in range(n-i-1):
            print("*",end=" ")
        #for space:
        for j in range(i+1):
            print("  ",end=" ")
        #for star:
        for i in range(n-i-1):
            print("*",end=" ")
        print("")
    pass
