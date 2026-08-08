class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and q[-1][0] < nums[r]:
                q.pop()
            q.append((nums[r], r))

            if q and q[0][1] < l:
                q.popleft()
            if (r - l + 1) >= k:
                output.append(q[0][0])
                l = l + 1
            r = r + 1
            
        return output