class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = 'aeiou'
        c = 0
        window = []
        for i in range(k):
            if s[i] in v:
                c+=1
            window.append(s[i])
        mx = c
        
        for r in range(k,len(s)):
            if s[r] in v:
                c+=1
            if s[r-k] in v:
                c-=1
            mx = max(c,mx)
            window.append(s[r])
            window.remove(s[r-k])
        return mx
             

        
        