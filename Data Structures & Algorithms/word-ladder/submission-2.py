class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        queue = deque()
        visited = set()
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        visited.add(beginWord)
        queue.append(beginWord)

        c_list = 'abcdefghijklmnopqrstuvwxyz'

        count = 1

        while queue:
            ln = len(queue)
            for _ in range(ln):
                curr = queue.popleft()
                if curr == endWord:
                    return count
                n = len(curr)
                for i in range(n):
                    for c in c_list:
                        nxt = curr[:i] + c + curr[i+1:]
                        if nxt in wordList and nxt not in visited:
                            queue.append(nxt)
                            visited.add(nxt)
            count += 1
        return 0


