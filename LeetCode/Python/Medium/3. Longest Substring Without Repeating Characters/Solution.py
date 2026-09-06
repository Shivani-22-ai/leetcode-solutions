class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        ans = float('-inf')
        for i in s:
            if i in seen:
                ans = max(ans,l)
                l = 0 
            l+=1
            ans = max(ans,l)
            seen.add(i)
        return ans
