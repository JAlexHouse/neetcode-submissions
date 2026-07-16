class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        for idx, num in enumerate(nums):
            numsToUse = nums[:idx] + nums[idx+1:] if idx + 1 != len(nums) else nums[:idx]
            solution.append(math.prod(numsToUse))
        return solution