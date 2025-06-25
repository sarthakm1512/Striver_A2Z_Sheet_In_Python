#Question Link: https://www.naukri.com/code360/problems/find-character-case_58513?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf%5C
"""
Find Character Case 

Problem Statement: Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.

1, if the character is an uppercase alphabet (A - Z).
0, if the character is a lowercase alphabet (a - z).
-1, if the character is not an alphabet.
"""

i = input('')

if (i >= 'A' and i <= 'Z'):
    print("1")
elif (i >= 'a' and i <= 'z'):
    print("0")
else:
    print("-1")
