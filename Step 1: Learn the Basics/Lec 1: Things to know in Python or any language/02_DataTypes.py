#Question link: https://www.geeksforgeeks.org/problems/data-type-1666706751/1

"""
Data Type

Geek is learning a new programming language. As data type forms the most fundamental part of a language, Geek is learning them with focus and needs your help.
Given a data type, help Geek in finding the size of it in byte.

Data Type - Character, Integer, Long, Float and Double
"""
#Python doesn't have fixed sizes for data types like C/C++, we'll return the typical sizes as in C/C++ based on the input string.
class Solution:
    def dataTypeSize(self, str):
      
        if str == 'Character':
            return 1
        elif str == 'Integer':
            return 4
        elif str == 'Long':
            return 8
        elif str == 'Float':
            return 4
        elif str == 'Double':
            return 8
        else:
            return -1
