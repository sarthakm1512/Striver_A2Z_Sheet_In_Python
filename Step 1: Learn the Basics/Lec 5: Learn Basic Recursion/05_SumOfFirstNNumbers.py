#Question Link: https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
"""
Sum of first n terms

Problem Statement: Given an integer n, calculate the sum of series 1^3 + 2^3 + 3^3 + 4^3 + … till n-th term.

Input: n = 5
Output: 225
Explanation: 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225

Expected Complexities:
Time Complexity: O(1)
Auxiliary Space: O(1)
"""

class Solution:
    def sumOfSeries(self,n:int)->None:
        if(n==0):
            return 0
        return n*n*n + self.sumOfSeries(n-1)
