class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix, suffix approach
        res = [1] * len(nums)
        # prefix
        prefix = 1
        for i, num in enumerate(nums):
            res[i] = prefix
            prefix = prefix * num
        # suffix
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = suffix * res[i]
            suffix = suffix * nums[i]

        return res