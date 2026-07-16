class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumString = "".join([char for char in s if char.isalnum()]).lower()
        return alnumString[::-1] == alnumString