class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        tmp = []
        
        def dfs(start_index, total):
            if total == target:
                res.append(tmp.copy())
                return 
            
            for i in range(start_index, len(candidates)):
                if total + candidates[i] > target :
                    break
                
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                tmp.append(candidates[i])
                dfs(i + 1, total + candidates[i])

                tmp.pop()
        dfs(0, 0)
        return res



