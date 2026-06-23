class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = ''.join([char for char in s if char.isalnum()])
        raw = raw.lower()
        l = 0
        r = len(raw) - 1

        while l < r:
            if raw[l] != raw[r]:
                return False
            l += 1
            r -= 1

        return True






