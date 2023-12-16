class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dict_s = {}
            dict_t = {}
            for i in range(len(s)):
                try:
                    dict_s[s[i]] += 1
                except KeyError:
                    dict_s[s[i]] = 1
                try:
                    dict_t[t[i]] += 1
                except KeyError:
                    dict_t[t[i]] = 1

            res = (dict_s == dict_t)
            return res
        else:
            return False