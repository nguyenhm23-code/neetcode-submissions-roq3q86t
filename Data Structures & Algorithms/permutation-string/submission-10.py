class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for char in s1:
            count1[char] = 1 + count1.get(char, 0)
        
        tmp = len(count1)
    
        for i in range(len(s2)):
            cur = 0
            count2 = {}
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)

                if count1.get(s2[j], 0) < count2.get(s2[j], 0):
                    break
                if count1.get(s2[j], 0) == count2.get(s2[j], 0):
                    cur += 1
                
                if cur == tmp:
                    return True
        return False