# https://leetcode.com/problems/valid-anagram/submissions/

def isAnagram(s: str, t: str) -> bool:
    # dic1, dic2 = {}, {}
    
    # for char in s:
    #     dic1[char] = dic1.get(char, 0) + 1
    # for char in t:
    #     dic2[char] = dic2.get(char, 0) + 1
    # return dic1 == dic2

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