#Question Link: https://www.naukri.com/code360/problems/ninja-and-the-number-pattern-i_6581959?leftPanelTabValue=PROBLEM
"""
Ninja And The Number Pattern

Problem Statement: Ninja has been given a task to print the required pattern and he asked for your help with the same.
You must print a matrix corresponding to the given number pattern.

Example:
Input: ‘N’ = 4

Output: 
4444444
4333334
4322234
4321234
4322234
4333334
4444444
"""

def getNumberPattern(n: int) -> None:
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            right = (2*n-2)-j
            bottom = (2*n-2)-i
            print(n-min(min(top,bottom),min(left,right)),end="")
        print("")
    pass
