class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            val = hashmap.get(target - num)
            if val is None:
                hashmap[num] = i
            else:
                return [val, i]
        return []