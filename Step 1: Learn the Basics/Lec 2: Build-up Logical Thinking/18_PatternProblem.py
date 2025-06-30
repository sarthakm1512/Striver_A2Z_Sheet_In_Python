#Question Link: https://www.naukri.com/code360/problems/alpha-triangle_6581429?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
"""
Alpha-Triangle

Problem Statement: Sam is researching on Alpha-Triangles. So, he needs to create them for different integers ‘N’.
An Alpha-Triangle is represented by the triangular pattern of alphabets in reverse order.
For every value of ‘N’, help sam to print the corresponding Alpha-Triangle.

Example:
Input: ‘N’ = 3

Output: 
C
C B 
C B A
"""

def alphaTriangle(n:int):
  for i in range(n):
    alphabet = ord('A')+n-1
    for j in range(i+1):
      print(chr(alphabet),end=" ")
      alphabet -= 1
    print("")
  pass
