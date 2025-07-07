#Question Link: https://www.geeksforgeeks.org/problems/print-gfg-n-times/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-gfg-n-times
"""
Print GFG n times

Problem Statement: Print GFG n times without the loop.

Input:
5
Output:
GFG GFG GFG GFG GFG
"""

class Solution:
    def printGfg(self, n:int,i:int=1)->None:
        if i>n:
            return
        print("GFG",end=" ")
        self.printGfg(n,i+1)
        
