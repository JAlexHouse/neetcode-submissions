class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSorted = sorted(nums)
        numsToLength = {}
        if len(nums) == 0:
            return 0
        longest = 1
        for num in numsSorted:
            numBeforeLength = numsToLength.get(num - 1)
            if (numBeforeLength is not None):
                numsToLength[num] = numBeforeLength + 1
                longest = numBeforeLength + 1 if numBeforeLength + 1 > longest else longest
            else:
                numsToLength[num] = 1

        return longest