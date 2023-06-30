def productExceptSelf(nums):
    pre = 1
    post = 1
    ans = [1 for x in range(len(nums))]

    for index, val in enumerate(nums[:-1]):
        pre *= val
        ans[index + 1] *= pre

    nums.reverse()
    ans.reverse()

    for index, val in enumerate(nums[:-1]):
        post *= val
        ans[index + 1] *= post

    ans.reverse()

    return ans


def productExceptSelf2(nums):
    ans = [1 for x in range(len(nums))]
    prefix = 1
    for i in range(len(nums)):
        ans[i] *= prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]
    return ans

assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]