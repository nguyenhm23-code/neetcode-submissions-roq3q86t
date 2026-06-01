class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        def dfs(i):
            if i >= len(nums):
                if sorted(tmp) in res:
                    return 
                res.append(sorted(tmp.copy())) 
                return

            
            tmp.append(nums[i])
            dfs(i+1)
            
            tmp.pop()
            dfs(i+1)
        dfs(0)
        
        return res