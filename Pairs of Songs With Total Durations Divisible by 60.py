class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        a = [0 for i in range(60)]
        for t in time: a[t % 60] += 1
        
        ans = max(0, a[0] * (a[0] - 1) // 2) + max(0, a[30] * (a[30] - 1) // 2)
        for i in range(1, 30): ans += a[i] * a[60 - i]
            
        return ans
