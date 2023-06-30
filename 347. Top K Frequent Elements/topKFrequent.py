def topKFrequent(nums, k):
    ans, dicti = [], {}
    for num in nums:
        if num not in dicti:
            dicti[num] = 1
        else:
            dicti[num] = dicti[num] + 1

    sortedDict = sorted(dicti.items(), key=lambda x: x[1], reverse=True)

    for key in sortedDict[:k]:
        ans.append(key[0])

    return ans


print(topKFrequent([1,1,1,2,2,3], 2))