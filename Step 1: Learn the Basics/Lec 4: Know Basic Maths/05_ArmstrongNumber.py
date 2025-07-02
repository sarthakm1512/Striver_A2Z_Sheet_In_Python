#Question Link: https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1?
"""
Armstrong Numbers

Problem Statement: You are given a 3-digit number n, Find whether it is an Armstrong number or not.
An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. 
"""

class Solution:
    def armstrongNumber (self, n):
        original = n
        sum = 0
        
        while(n > 0):
            ld = n % 10
            sum = sum + (ld * ld * ld)
            n //= 10
        
        if original == sum:
            return True
        else:
            return False
