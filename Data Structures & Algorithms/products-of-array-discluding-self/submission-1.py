class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        tmp = 1
        for i in range(1, len(nums)):
            tmp *= nums[i]
        res.append(tmp)
        for i in range(1,len(nums)):
            tmp = 1
            for j in range(0,i):
                tmp *= nums[j]
            for k in range(i+1, len(nums)):
                tmp *= nums[k]
            res.append(tmp)
        return res