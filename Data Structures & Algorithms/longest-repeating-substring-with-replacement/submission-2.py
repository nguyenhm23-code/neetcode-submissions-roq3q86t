class Solution:
    def characterReplacement(self, s: str, k: int) -> int:    
        charset = set()
        res = 0
        for c in s:
            charset.add(c)
        for c in charset:
            l , r, count = 0, 0, 0    
            while l <= r and r <= len(s) - 1:
                if s[r] == c:
                    count += 1

                if r - l + 1 - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
                r += 1 
        return res
                                       
