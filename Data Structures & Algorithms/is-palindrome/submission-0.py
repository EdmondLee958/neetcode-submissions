class Solution:
    def isPalindrome(self, s: str) -> bool:
        def good(ch):
            return ch.isalnum()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not good(s[i]):
                i += 1
            while i < j and not good(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True