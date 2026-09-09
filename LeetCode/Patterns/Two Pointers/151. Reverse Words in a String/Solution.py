class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        l = s.split()
        l.reverse()
        return ' '.join(l)       