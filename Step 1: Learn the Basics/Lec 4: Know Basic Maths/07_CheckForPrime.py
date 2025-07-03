#Question Link: https://www.naukri.com/code360/problems/check-prime_624674?interviewProblemRedirection=true&search=check%20prime&leftPanelTabValue=PROBLEM
"""
Check Prime

Problem Statement: Given an integer, check if it is prime or not. Return True if the number is prime, otherwise False.

Input 1 :
7
Output 1 :
True

Input 2 :
15
Output 2 :
False

"""

def check_prime(num):
    factor = 0
    for i in range(1,num+1):
        if (num%i==0):
            factor += 1
    if (factor == 2):
        return True
    else:
        return False
