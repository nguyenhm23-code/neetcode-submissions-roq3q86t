class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            if count.get(i, 0) > 1:
                return i
        return -1
        