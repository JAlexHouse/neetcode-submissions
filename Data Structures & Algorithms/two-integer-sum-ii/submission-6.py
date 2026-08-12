class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        resMap = {} # diff -> index
        for i, num in enumerate(numbers):
            diff = target-num
            resIdx = resMap.get(num)
            if resIdx:
                return [resIdx, i+1]
            else:
                resMap[diff] = i+1
        return []