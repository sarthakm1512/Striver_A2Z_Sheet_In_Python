#Question Link: https://www.naukri.com/code360/problems/symmetric-void_6581919?leftPanelTabValue=PROBLEM
"""
Symmetric Void

Problem Statement: Sam is curious about symmetric patterns, so he decided to create one.
For every value of ‘N’, return the symmetry as shown in the example.

Example:
Input: ‘N’ = 3

Output:
* * * * * * 
* *     * * 
*         * 
*         * 
* *     * * 
* * * * * * 
"""

def symmetry(n: int):
    #upper part
    for i in range(n):
        #for stars before space:
        for j in range(n-i):
            print("*",end=" ")
        #for space:
        for j in range(2*i):
            print(" ",end=" ")
        #for stars after space:
        for j in range(n-i):
            print("*",end=" ")
        print("")
    #lower part
    for i in range(n):
        #for stars before space:
        for j in range(i+1):
            print("*",end=" ")
        #for space:
        for j in range(2*n-2*i-2):
            print(" ",end=" ")
        #for stars after space:
        for j in range(i+1):
            print("*",end=" ")
        print("")
    pass
