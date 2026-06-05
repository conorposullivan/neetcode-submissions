class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, R = 0, 0
        curr_sum = 0
        sub_num  = 0
        curr_sub = []
        while R < len(arr):
            if (R - L + 1) > k:
                curr_sum -= curr_sub[0]
                curr_sub.pop(0)
                L += 1
            curr_sum += arr[R]
            curr_sub.append(arr[R])
            if len(curr_sub) == k and (curr_sum/ k) >= threshold:
                sub_num += 1
            R += 1
        return sub_num 

            

        