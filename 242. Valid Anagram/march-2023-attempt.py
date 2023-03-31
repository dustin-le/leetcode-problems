def validAnagram(word1, word2):
    dict1, dict2 = {}, {}

    for char in word1:
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1

    for char in word2:
        if char not in dict2:
            dict2[char] = 1
        else:
            dict2[char] += 1
            
    return dict1 == dict2
    
assert validAnagram("anagram", "nagaram") == True
assert validAnagram("rat", "car") == False