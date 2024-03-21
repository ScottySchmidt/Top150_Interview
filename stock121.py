"""
Leetcode 122. Best Time to Buy and Sell Stock II
TOP150 Big Tech Question

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
"""

class Solution(object):
    def maxProfit(self, prices):
        # TWO POINTER
        left = 0# buy index
        right = 1# sell index
        max_profit = 0# max profit
        while right<len(prices): # search every right 
            buy = prices[left]# buy
            sel = prices[right]# sel
            profit = sel - buy#profit
            if profit > 0:#if profits
                max_profit = max(max_profit, profit)# new max?
            else:
                left = right# update pointer to new low
            right = right+1# always new sell        
        return max_profit 
