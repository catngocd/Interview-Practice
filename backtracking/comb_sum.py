class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol_set = []
        
        def backtrack(candidates, subset, start, target):
            if target == 0:
                sol_set.append(subset)
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                subset.append(candidates[i])
                # i instead of i + 1 because first number needs to be evaluated whether it hits target
                backtrack(candidates, subset.copy(), i, target - candidates[i])
                subset.pop()
        
        backtrack(candidates, [], 0, target)
        
        return sol_set
