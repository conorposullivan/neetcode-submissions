class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        k = 0
        while i < n:
            if nums[i] != val:
                k += 1
                i += 1
                continue
            nums.pop(i)
            nums.append('_')
            n -= 1

        return k
        