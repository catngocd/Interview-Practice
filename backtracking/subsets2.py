class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerset = []
        
        def backtrack(nums: List[int], subset: List, start: int):
            powerset.append(subset)
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(nums, subset.copy(), i + 1)

                subset.pop()
                
        nums.sort()
        backtrack(nums, [], 0)
        
        return powerset
