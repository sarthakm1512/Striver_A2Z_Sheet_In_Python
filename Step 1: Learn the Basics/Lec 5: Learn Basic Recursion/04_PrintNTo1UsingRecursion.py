#Question Link: https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-n-to-1-without-loop
"""
Print N to 1 without loop

Problem Statement: Print numbers from N to 1 (space separated) without the help of loops.

Input: N = 10
Output: 10 9 8 7 6 5 4 3 2 1
Your Task: This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints number from N to 1 recursively. Don't print newline, it will be added by the driver code.
"""

class Solution:
    def printNos(self, n:int, i:int=1)->None:
        if i>n:
            return
        print(n,end=" ")
        self.printNos(n-1,i)
      
