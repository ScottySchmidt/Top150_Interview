""" 
1402. Reducing Dishes, Hard level: https://leetcode.com/problems/reducing-dishes/

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Example 1:
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.

Example 2:
Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
"""


# Final solution, doing a big first approach:
def maxSatisfaction(self, satisfaction):
    n = len(satisfaction)
    satisfaction.sort(reverse=True) # Sort values by biggest first

    final = 0 # total count
    accSum = 0 # current list count

    for i in range(n): # loop through every number 
        accSum = accSum + satisfaction[i] # add every number in list including current num
        if accSum < 0:
           break # this curr num provides no value
        final = final + accSum # if 
    return final # final value should be greater than 0 since we only add positives 



# My original solution is incorrect because it does not find the accumulative sum if that dish adds value greater than 0:
class Solution(object):
    def maxSatisfaction(self, satisfaction):
        total = 0
        count = 0
        length = len(satisfaction)
        satisfaction.sort(reverse=False)
        print(satisfaction, "  list sorted")

        for i in range(length):
            n = satisfaction[i] 
            if n > 0:
                count = count + 1
                total = total + (n*count)
        return max(total, 0)
