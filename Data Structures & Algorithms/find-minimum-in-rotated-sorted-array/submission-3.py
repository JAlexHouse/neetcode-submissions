class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            lNum, rNum, midNum = nums[l], nums[r], nums[mid]
            if midNum > rNum:
                l = mid + 1
            elif midNum < lNum or midNum <= rNum:
                r = mid
            elif midNum <= rNum:
                r = mid
            elif midNum >= lNum:
                l = mid + 1

        return nums[r]

        