class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0,0
        tmp = []
        if len(s1) == 1:
            return s1 in s2
        
        for char in s1:
            tmp.append(char)
        tmp.sort()
        
        for index in range(len(s2) - len(s1) + 1):    
            if s2[index] in s1:
                mapping = []
                for i in range(index , index + len(s1)):
                    mapping.append(s2[i])
                mapping.sort()
                if mapping == tmp:
                    return True
        return False
        