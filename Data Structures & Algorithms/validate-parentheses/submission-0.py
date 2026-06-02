class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["(","{","["]
        bracket_map = {")":"(", "}":"{","]":"["}
        stack = []
        for b in s:
            if b in open_brackets:
                stack.append(b)
                continue
            if not stack or bracket_map[b] != stack[-1]:
                return False
            stack.pop()
        return len(stack) == 0
            
        