#Question Link: https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
"""
Sum 1 to n Divisors

Problem Statement: Given a positive integer n, The task is to find the value of Σi F(i) where i is from 1 to n and function F(i) is defined as the sum of all divisors of i.

Input: n = 4
Output: 15
Explanation:
F(1) = 1
F(2) = 1 + 2 = 3
F(3) = 1 + 3 = 4
F(4) = 1 + 2 + 4 = 7
So, F(1) + F(2) + F(3) + F(4)
    = 1 + 3 + 4 + 7 = 15
"""
#Code with Time Complexity = O(n^2)
"""
def sumOfDivisors(self, n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if(i % j == 0):
                sum += j
    return sum
"""

#Code with Time Complexity = O(n)
class Solution:
  def sumOfDivisors(self, n):
    sum=0
    for i in range(1,n+1):
        sum += i * (n//i)
    return sum
