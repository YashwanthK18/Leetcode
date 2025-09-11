class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for i in s:
            if not stack:
                stack.append(i)
            elif i in d:
                if d[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True
