# https://leetcode.com/problems/contains-duplicate/

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    mySet = set()
    for i in nums:
        if i not in mySet:
            mySet.add(i)
        else:
            return True
        
    return False

assert containsDuplicate([1,2,3,1]) == True
assert containsDuplicate([1,2,3,4]) == False
assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True