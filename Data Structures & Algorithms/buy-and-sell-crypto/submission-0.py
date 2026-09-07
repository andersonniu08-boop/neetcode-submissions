class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0
        maxp = 0
        for j in range(len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                if profit > maxp:
                    maxp = profit
                j += 1
            else:
                i = j
                j += 1

        return maxp
            

        