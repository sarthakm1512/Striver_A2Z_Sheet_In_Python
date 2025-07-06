#Question Link: https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-1-to-n-without-using-loops
"""
Print 1 To N Without Loop

Problem Statement: You are given an integer n. You have  to print all numbers from 1 to n.
Note: You must use recursion only, and print all numbers from 1 to n in a single line, separated by spaces.

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Input: n = 5
Output: 1 2 3 4 5

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

class Solution:    
    def printNos(self,n:int,i:int=1)->None:
        if i>n:
            return
        print(i,end=" ")
        self.printNos(n,i+1)
