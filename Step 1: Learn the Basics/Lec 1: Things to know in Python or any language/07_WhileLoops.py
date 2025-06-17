#Question Link: https://www.geeksforgeeks.org/problems/while-loop-printtable-java/1
"""
While loop- printTable

Problem Statement: While loop is another loop like for loop but unlike for loop it only checks for one condition.
Here, we will use a while loop and print a number n's table in reverse order.
"""

class Solution:
    def calculateMultiples(self, n):
        i = 10
        while i > 0:
            ans = n * i
            print(ans, end=" ")
            i -= 1
        print()
