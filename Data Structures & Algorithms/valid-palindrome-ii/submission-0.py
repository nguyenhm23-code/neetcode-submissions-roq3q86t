class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s:
            return True
        for i in range(len(s)):
            tmp = s[0:i] + s[i+1:]
            if tmp[::-1] == tmp:
                return True
        return False
            