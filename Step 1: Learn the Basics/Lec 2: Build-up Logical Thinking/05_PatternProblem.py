#Question Link: https://www.naukri.com/code360/problems/seeding_6581892?leftPanelTabValue=PROBLEM
"""
Seeding

Problem Statement: Sam is planting trees on the upper half region (separated by the left diagonal) of the square shared field.
For every value of ‘N’, print the field if the trees are represented by ‘*’.

Example:
Input: ‘N’ = 3

Output: 
* * *
* *
*
"""

def seeding(n: int) -> None:
    
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print("")
    pass
