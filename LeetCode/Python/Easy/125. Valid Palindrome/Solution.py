class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = []
        for c in s:
            if c.isalpha():
                i.append(c.lower())
        s = ''.join(i)
        l = 0
        r = len(s)-1
        while(l<r):
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
