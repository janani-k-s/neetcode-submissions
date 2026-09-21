class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=[ch for ch in s if ch.isalnum()]
        return s==s[::-1]
        