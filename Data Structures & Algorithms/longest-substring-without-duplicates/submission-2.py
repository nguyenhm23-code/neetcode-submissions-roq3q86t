class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        mapping = {}
        for i, c in enumerate(s):
            if mapping.get(c, -1) >= l:
                l = mapping[c] + 1
            res = max(res, i - l + 1)
            mapping[c] = i
            
        return res


        