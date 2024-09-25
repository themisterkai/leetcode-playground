class Solution:
    def maxProfit(self, prices) -> int:
        min = float('inf')
        max_profit = 0

        for price in prices:
            if price < min:
                min = price
            if price - min > max_profit:
                max_profit = price - min
        return max_profit


pricesInput = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(pricesInput))