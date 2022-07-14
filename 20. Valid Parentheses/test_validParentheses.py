from validParentheses import isValid

def test_happyPath():
    assert isValid("()") == True
    assert isValid("()[]{}{}()[]()[]") == True
    assert isValid("({[([[{{{{}}}}]])]})") == True
    
def test_unhappyPath():
    assert isValid("(") == False
    assert isValid("]") == False
    assert isValid("][") == False
    assert isValid("()]") == False
    assert isValid("()[}]") == False
    assert isValid("()[}]") == False