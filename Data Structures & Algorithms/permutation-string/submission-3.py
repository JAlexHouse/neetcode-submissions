class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        for i in range(0, len(s2) - windowSize + 1):
            print(i, s2[i:(i+windowSize)])
            if sorted(s2[i:(i+windowSize)]) == sorted(s1):
                return True
        return False
