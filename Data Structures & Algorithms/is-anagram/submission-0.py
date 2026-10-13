class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def getDict(word: str) -> dict:
            word_dict = {}
            for w in word:
                if w in word_dict:
                    word_dict[w] += 1
                    continue
                word_dict[w] = 1
            return word_dict
        s_dict = getDict(s)
        t_dict = getDict(t)
        return s_dict == t_dict
        