class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ex = []
        al = "abcdefghijklmnopqrstuvwxyz1234567890"
        for i in s:
            if i in al:
                ex.append(i)
        rev = ex[::-1]
        return ex == rev

