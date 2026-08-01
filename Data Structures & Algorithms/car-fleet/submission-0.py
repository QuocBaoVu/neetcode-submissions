class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_table = defaultdict(int)
        n = len(position)
        for i in range(n):
            speed_table[position[i]] = speed[i]
        
        position.sort(reverse=True)
        time = [0] * n
        for i in range(n):
            time[i] =  (target-position[i]) / speed_table[position[i]]
                
        
        stack = [0]
        for i in range(n):
            while stack and time[i] > stack[-1]:
                stack.append(time[i])
        return len(stack)-1