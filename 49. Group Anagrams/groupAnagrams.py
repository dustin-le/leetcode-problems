from collections import defaultdict


def groupAnagrams(strs):
    dict = defaultdict(list)

    for word in strs:
        count = [0] * 26
        
        for char in word:
            count[ord(char) - 97] += 1
        
        dict[tuple(count)].append(word)
    
    return list(dict.values())


print(groupAnagrams(["cab", "tin", "pew", "duh",
      "may", "ill", "buy", "bar", "max", "doc"]))
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]

# Attempted ASCII solution - Didn't work because of coincidental ASCII values equaling, like "duh" and "ill"
    # asciiSum = [(ord(char)) for char in word]
    # asciiSum = sum(asciiSum)
    # print(f"{word} : {asciiSum}")

# Successful solution but O(m * n log n) time complexity, m being number of items in list and n being average length of strings.
    # dict = {}

    # for word in strs:
    #     count = [0] * 26

    #     for char in word:
    #         if char not in count:
    #             count[char] = 1
    #         else:
    #             count[char] += 1

    #     if count not in dict:
    #         dict[count] = [word]
    #     else:
    #         dict[count].append(word)

    # return list(dict.values())
