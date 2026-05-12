class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []
        def dfs(i, total):
            if i >= len(nums) or total > target:
                return 
            
            if total == target:
                return res.append(tmp.copy())

            tmp.append(nums[i])
            dfs(i, total + nums[i])
            tmp.pop()
            
            dfs(i + 1, total)
        dfs(0, 0)
        return res
                