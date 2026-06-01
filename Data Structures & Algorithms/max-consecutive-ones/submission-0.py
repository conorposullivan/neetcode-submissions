class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        curr_con = 0
        for i in nums:
            if i == 1:
                curr_con += 1
            else:
                curr_con = 0
                continue
            if curr_con > max_con:
                max_con = curr_con

        return max_con