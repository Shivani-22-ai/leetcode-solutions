from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = Counter(ransomNote)
        dic2 = Counter(magazine)
        if dic2 >= dic1:
            return True
        else:
            return False