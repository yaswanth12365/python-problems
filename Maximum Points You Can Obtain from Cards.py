class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left, right = (-k) % n, (-1) % n 
        s = sum(cardPoints[left:right+1])
        maxv = s
        for i in range(k):
            s = s - cardPoints[left%n] + cardPoints[(right+1)%n]
            maxv = max(maxv, s)
            left += 1
            right += 1
        return maxv 
