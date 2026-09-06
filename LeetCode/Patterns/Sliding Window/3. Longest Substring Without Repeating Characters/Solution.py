class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        ans = float('-inf')
        for i in s:
            if i in seen:
                l = 0 
            l+=1
            seen.add(i)
            ans = max(ans,l)
        return ans
