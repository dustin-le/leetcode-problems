def isValid(s: str) -> bool:
        stack = []
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if (len(stack) != 0):
                    check = stack.pop()
                    if (check == '(' and char != ')') or (check == '[' and char != ']') or (check == '{' and char != '}'):
                        return False
                else:
                    return False
        
        if ( len(stack) != 0 ):
            return False
        else:
            return True
    
print(isValid("]"))