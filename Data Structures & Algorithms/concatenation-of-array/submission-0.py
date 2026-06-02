class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        for i in range(len(ans)):
            j = i % len(nums)
            ans[i] = nums[j]
        return ans 
                