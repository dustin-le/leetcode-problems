# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
            
    return True
    
    # temp = []
    # for char in s:
    #     if char.isalnum():
    #         temp.append(char.lower())
            
    # for char in s:
    #     if char.isalnum():
    #         if temp.pop() != char.lower():
    #             return False
            
    # return True
    
    # forward = []
    # backward = []
    
    # for char in s:
    #     if char.isalnum():
    #         forward.append(char.lower())
    
    # temp = forward.copy()
    # for char in range(len(temp)):
    #     backward.append(temp.pop())
    
    # if forward == backward:
    #     return True
    # else:
    #     return False
    
assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindrome(" ") == True
assert isPalindrome(".,") == True