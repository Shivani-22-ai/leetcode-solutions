class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = []
        for c in s:
            if c.isalnum():
                i.append(c.lower())
        s = ''.join(i)
        rev = s[::-1]
        if rev == s:
            return True
        else:
            return False
