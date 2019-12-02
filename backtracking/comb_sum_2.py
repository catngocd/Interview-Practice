class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol_set = []
        
        def backtrack(candidates, subset, start, target):
            if target == 0:
                sol_set.append(subset)
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(candidates, subset.copy(), i + 1, target - candidates[i])
                subset.pop()
            
            
        candidates.sort()
        
        backtrack(candidates, [], 0, target)
        
        return sol_set
