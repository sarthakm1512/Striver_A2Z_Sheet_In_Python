#Question Link: https://www.naukri.com/code360/problems/print-1-to-n_628290?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&count=25&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=PROBLEM
"""
1 to N Without Loop

Problem Statement: You are given an integer ‘n’.
Your task is to return an array containing integers from 1 to ‘n’ (in increasing order) without using loops.

Example:
Input: ‘n’ = 5
Output: 1 2 3 4 5
Explanation: An array containing integers from ‘1’ to ‘n’ is [1, 2, 3, 4, 5].
"""

from typing import List

def printNos(n:int,i:int=1) -> List[int]: 
    if i>n:
        return []
    return[i] + printNos(n,i+1)
    pass
