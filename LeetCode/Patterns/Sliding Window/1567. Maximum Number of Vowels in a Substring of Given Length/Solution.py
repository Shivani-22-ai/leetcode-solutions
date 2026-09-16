class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = "aeiou"
        cv = 0
        mx = float('-inf')
        for i in range(k):
            if s[i] in v:
                cv+=1
        mx = max(mx,cv)
        for i in range(k,len(s)):
            if s[i-k] in v:
                cv-=1
            if s[i] in v:
                cv+=1
            mx = max(mx,cv)
        return mx
