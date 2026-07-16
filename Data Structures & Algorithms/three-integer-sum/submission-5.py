class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        sortedNums = sorted(nums)

        for idx, num in enumerate(sortedNums):
            left = idx + 1
            right = len(sortedNums) - 1;
            while (left < right):

                leftPlusRight = sortedNums[left] + sortedNums[right]
                if leftPlusRight == -num:
                    tripletToAdd = [sortedNums[left], sortedNums[right], num]
                    if (tripletToAdd not in solution):
                        solution.append([sortedNums[left], sortedNums[right], num])
                    left += 1
                elif leftPlusRight < -num:
                    left += 1
                else:
                    right -= 1
        return solution
