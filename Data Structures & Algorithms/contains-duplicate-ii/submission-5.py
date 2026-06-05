class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L, R = 0, 0
        n = len(nums)
        sub = []
        while R < n:
            if abs(L - R) > k:
                sub.pop(0)
                L += 1
            
            if nums[R] in sub:
                return True
            sub.append(nums[R])
            R += 1
        
        return False


        