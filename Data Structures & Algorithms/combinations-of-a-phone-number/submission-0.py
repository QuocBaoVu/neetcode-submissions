class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        out = []

        n = len(digits)
        if n == 0:
            return out
        def backtrack(path, start):
            if start == n:
                out.append(path[:])
                return
            
            for c in phone[digits[start]]:
                path += c
                backtrack(path, start+1)
                path=path[:-1]
        backtrack("", 0)
        return out

