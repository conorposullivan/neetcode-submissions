class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums_dict:
                return [nums_dict[comp],i]
            nums_dict[nums[i]] = i

        return []
        