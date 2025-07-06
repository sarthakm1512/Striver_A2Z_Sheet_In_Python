#Question Link: https://www.naukri.com/code360/problems/advanced-gcd_6557?interviewProblemRedirection=true&search=GCD&leftPanelTabValue=PROBLEM
"""
GCD

Problem Statement: Calculate and return GCD(Greatest Common Divisor) of two given numbers x and y.
Numbers should be in range of Integer.

Input 1:
20 
5
Output 1:
5

Input 2:
96 
14
Output 2:
2
"""

x = int(input())
y = int(input())
arr=0
def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)

if __name__=="__main__":
    print(gcd(x,y))
