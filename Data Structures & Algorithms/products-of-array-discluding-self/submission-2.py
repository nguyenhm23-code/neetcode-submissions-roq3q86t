class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt += 1
                continue
            product *= i 
        if zero_cnt > 1:
            return [0] * len(nums)  
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt > 0:
                if c == 0:
                    res[i] = int(product)
                else:
                    res[i] = 0 
            else:
                res[i] = int(product / c)
        return res
            


        
        