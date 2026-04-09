class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for i in s:
            if i.isalnum() :
                tmp += i
        tmp = tmp.lower()
        if tmp == tmp[::-1]:
            return True
        return False

        
        