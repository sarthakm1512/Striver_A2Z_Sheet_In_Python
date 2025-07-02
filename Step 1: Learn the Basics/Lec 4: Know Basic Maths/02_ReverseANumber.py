#Question Link: https://leetcode.com/problems/reverse-integer/description/
"""
Reverse Integer

Problem Statement: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)

        r = 0
        while(x>0):
            ld= x%10    
            r= (r*10) + ld
            x //= 10
        
        r *= sign

        if r <= -2**31 or r >= 2**31 -1:
            return 0
        return r
        
