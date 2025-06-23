#Question Link: https://www.geeksforgeeks.org/problems/pass-by-reference-and-value/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pass-by-reference-and-value
"""
Pass by Reference and Value

Problem Statement: Geek is learning about functions and calling a function with arguments. He learns that passing can take one of two forms: pass by value or pass by reference.
Geek wishes to add 1 and 2, respectively, to the parameter passed by value and reference. Help Geek in fulfilling his goal.
"""

class Solution:
    def passedBy(self, a, b):
        return (a+1,b+2);
