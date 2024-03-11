def isValid(s: str) -> bool:

    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    stack = []
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or bracket_map[char] != stack[-1]:
                return False
            stack.pop()
    
    return not stack

input_string = "{[]} []{}() ({})"
result = isValid(input_string)
print(result)
