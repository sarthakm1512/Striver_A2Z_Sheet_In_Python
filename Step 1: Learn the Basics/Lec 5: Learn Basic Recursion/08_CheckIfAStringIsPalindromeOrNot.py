#Question Link: https://leetcode.com/problems/valid-palindrome/description/
"""
Valid Palindrome

Problem Statement: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean the string
        s = s.lower()
        new_s = ''
        for ch in s:
            if ch.isalnum():
                new_s += ch
        
        #using recursion to check palindrome
        def check(left:int, right:int)->bool:
            if (left>=right):
                return True
            if new_s[left] != new_s[right]:
                return False
            return check(left+1, right-1)

        return check(0, len(new_s)-1)        
