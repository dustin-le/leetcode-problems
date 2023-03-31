def groupAnagrams(strs):
    dict = {}

    for word in strs:
        originalWord = word
        word = ''.join(sorted(word))
        if word not in dict:
            dict[word] = [originalWord]
        else:
            dict[word].append(originalWord)
    
    return list(dict.values())


# print(groupAnagrams(["cab", "tin", "pew", "duh",
#       "may", "ill", "buy", "bar", "max", "doc"]))
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]

# Attempted ASCII solution - Didn't work because of coincidental ASCII values equaling, like "duh" and "ill"
    # asciiSum = [(ord(char)) for char in word]
    # asciiSum = sum(asciiSum)
    # print(f"{word} : {asciiSum}")
