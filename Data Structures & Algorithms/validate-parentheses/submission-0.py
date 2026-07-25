class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        table = {'(':')', '{':'}', '[':']'}

        for i in s:
            if i in table:
                stack.append(i)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if table[curr] != i:
                    return False
        if stack:
            return False
        return True