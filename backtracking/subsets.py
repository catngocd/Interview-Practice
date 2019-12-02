import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # List that stores all subsets
        powerset = []
        
        def backtrack(nums: List, subset: List, start: int):
            powerset.append(subset)
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(copy.deepcopy(nums), copy.deepcopy(subset), i + 1)
                
                # Remove nums[i] from present subset to explore subsets that don't contain nums[i]
                subset.pop() 
        
        
        backtrack(nums, [], 0)
        
        return powerset
