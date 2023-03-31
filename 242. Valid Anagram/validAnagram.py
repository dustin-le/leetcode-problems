# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str):
    # # First attempt
    # dic1, dic2 = {}, {}
    
    # for char in s:
    #     dic1[char] = dic1.get(char, 0) + 1
    # for char in t:
    #     dic2[char] = dic2.get(char, 0) + 1
    # return dic1 == dic2
    
    # # Third attempt in a while
    # sChars = []
    # if len(s) == len(t):
    #     for char in s:
    #         sChars.append(char)
    #     for char in t:
    #         if char in sChars:
    #             sChars.remove(char)
        
    #     return len(sChars) == 0
    # return False
    
    # # Fourth attempt after looking at second attempt
    #   if len(s) != len(t):
    #       return False
    # dict1, dict2 = {}, {}
    
    # for char in s:
    #     if char not in dict1:
    #         dict1[char] = 1
    #     elif char in dict1:
    #         dict1[char] += 1
    
    # for char in t:
    #     if char not in dict2:
    #         dict2[char] = 1
    #     elif char in dict2:
    #         dict2[char] += 1
    
    # return dict1 == dict2

    dict = {}
    
    if (len(s) != len(t)):
        return False
    
    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    for char in t:
        if char in dict:
            if dict[char] == 1:
                dict.pop(char)
            else:
                dict[char] -= 1
        else:
            return False
    return True

assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False
assert isAnagram("ac", "bb") == False
assert isAnagram("a", "ab") == False