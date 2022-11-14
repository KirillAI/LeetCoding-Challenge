'''
Best Time to Buy and Sell Stock
#DynamicProgramming #easy
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

'''
The maximum price difference at step i is defined as the difference between some maximum price with index i and a minimum price with index less than i. And also min(prices[:i-1]) <= min(prices[:i-2]). That is, when viewing prices sequentially, the minimum price either decreases or remains the same, and the maximum price difference either increases or remains the same. The maximum price difference at step i will be max(maxDiff, prices[i] - min(prices[:i-1])). At each step i, we will update the minimum price and the maximum price difference. For this purpose, we need two additional variables.

Time: O(N)
Memory: O(1)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = prices[0]
        for i in range(1, len(prices)):
            temp = prices[i] - minVal
            if temp > res:
                res = temp
            minVal = min(minVal, prices[i])
        return res