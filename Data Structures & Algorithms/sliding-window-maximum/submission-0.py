class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []

        for l in range(len(nums) - k + 1):
            r = l + k
            maxes.append(max(nums[l:r]))
        return maxes