# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    stack = []
    
    dict = {")":"(", "}":"{", "]":"["}
    
    for char in s:
        if char in dict and stack != []:
            if dict[char] != stack.pop():
                return False
        else:
            stack.append(char)
    
    return stack == []

        # stack = []
        
        # for char in s:
        #     if char == '(' or char == '[' or char == '{':
        #         stack.append(char)
        #     else:
        #         if (len(stack) != 0):
        #             check = stack.pop()
        #             if (check == '(' and char != ')') or (check == '[' and char != ']') or (check == '{' and char != '}'):
        #                 return False
        #         else:
        #             return False
        
        # if ( len(stack) != 0 ):
        #     return False
        # else:
        #     return True
