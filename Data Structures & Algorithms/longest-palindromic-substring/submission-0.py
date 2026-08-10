class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal = s[0]

        for i in range(len(s) - 1):
            # check for odd-length palindromes
            l = r = i
            tempOddMax = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tempOddMax = s[l:r+1]
                l -= 1
                r += 1
            
            # check for even-length palindromes
            l, r = i, i + 1
            tempEvenMax = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tempEvenMax = s[l:r+1]
                l -= 1
                r += 1
            if len(tempOddMax) > len(maxPal):
                maxPal = tempOddMax
            if len(tempEvenMax) > len(maxPal):
                maxPal = tempEvenMax

        return maxPal