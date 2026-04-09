class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = -10000
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                res = max(res, prices[j] - prices[i])
        if res > 0:
            return res
        else:
            return 0
