class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in brackets:
                #if the top of the stack does not match the character in the map return false
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)
            
        return not stack
                



        