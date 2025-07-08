#Question Link: https://www.geeksforgeeks.org/problems/factorial5739/1
"""
Factorial

Problem Statement: Given a positive integer, n. Find the factorial of n.

Input: n = 5
Output: 120
Explanation: 1 x 2 x 3 x 4 x 5 = 120
"""

class Solution:
    def factorial(self, n:int)->None:
        if(n==0):
            return 1
        return n * self.factorial(n-1)
