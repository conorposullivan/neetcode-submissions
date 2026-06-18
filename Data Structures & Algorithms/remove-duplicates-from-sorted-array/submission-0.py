class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        k = 0
        nums_set = set()
        while l < r:
            print(nums[l])
            if nums[l] not in nums_set:
                nums_set.add(nums[l])
                l += 1
                k += 1
                continue
            nums.pop(l)
            r -= 1

        return k
        