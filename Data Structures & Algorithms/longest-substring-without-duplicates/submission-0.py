class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        sub_lst = []
        max_len = 0

        for R in range(len(s)):
            if s[R] in sub_lst:
                while s[R] in sub_lst:
                    sub_lst.pop(0)
                    L += 1
            sub_lst.append(s[R])
            max_len = max (R - L + 1, max_len)               
        return max_len