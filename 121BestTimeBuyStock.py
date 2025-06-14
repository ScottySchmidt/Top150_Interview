'''
YOUTUBE SOLUTION:  https://www.youtube.com/watch?v=pPz0NUmgtwI&t=2s

Leetcode 121: Best Time to Buy and Sell Stock, Two Pointer!  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

# Two Pointer Python Solution:
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0 # Buy Left Pointer
        right = 0 # Sell Right Pointer
        max_profit = 0 
        while right < len(prices):
            buy = prices[left]  # Buy comes first, left pointer
            sell = prices[right] 
            curr_profit = sell - buy
            
            if sell > buy:  # If profit, check if max profit
                max_profit = max(curr_profit, max_profit)
            else: # Need a new LEFT pointer
                left = right
            right = right +1 # Always need a new right pointer
        return max_profit  # Final Answer Once All Right pointers Check
