# https://www.youtube.com/watch?v=BSaL1S_IdFQ&t=5s

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
                print(first)
            elif n <= first:
                second = n
                print(second)
            elif n <= second:
                return True
                print(first, second, third)
        return False
        #print(first, second, third)
