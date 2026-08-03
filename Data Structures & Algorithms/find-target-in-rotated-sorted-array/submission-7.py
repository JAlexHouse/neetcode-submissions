class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            lNum, midNum, rNum = nums[l], nums[mid], nums[r]
            
            if midNum == target:
                return mid
            
            # left sorted
            if lNum <= midNum:
                if target > midNum or target < lNum:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # check left side
                if target < midNum or target > rNum:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1