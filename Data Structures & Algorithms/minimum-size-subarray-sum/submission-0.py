class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 0
        length = float("inf")
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            if curr_sum >= target:
                while curr_sum >= target:
                    length = min(R - L + 1, length)
                    curr_sum -= nums[L]
                    L += 1

        return 0 if length == float("inf") else length
        