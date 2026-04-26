class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c_to_o = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in c_to_o:
                if stack and stack[-1] == c_to_o[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False