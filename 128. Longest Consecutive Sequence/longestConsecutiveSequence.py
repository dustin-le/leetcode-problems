# https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
    longestRecord = 1

    nums = set(nums)
    for num in nums:
        longestCurrent = 1
        if ((num - 1) not in nums):
            while ((num + 1) in nums):
                num += 1
                longestCurrent += 1
        if (longestCurrent > longestRecord):
            longestRecord = longestCurrent
    
    return longestRecord


def checkNext(num, nums):
    global longestCurrent
    if ((num) in nums):
        longestCurrent += 1
        checkNext(num+1, nums)
    else:
        return
    
# def longestConsecutive(nums):
#     longestRecord = 1

#     nums = set(nums)
#     for num in nums:
#         global longestCurrent
#         longestCurrent = 1
#         if ((num - 1) not in nums):
#             checkNext(num+1, nums)
#         if (longestCurrent > longestRecord):
#             longestRecord = longestCurrent

#     return longestRecord


# def checkNext(num, nums):
#     global longestCurrent
#     if ((num) in nums):
#         longestCurrent += 1
#         checkNext(num+1, nums)
#     else:
#         return

    
assert(longestConsecutive([100,4,200,1,3,2]) == 4)