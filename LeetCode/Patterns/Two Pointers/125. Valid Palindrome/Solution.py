class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ex = []
        for i in s:
            if i.isalnum():
                ex.append(i)
        i,j = 0,len(ex)-1
        while(i<=j):
            if ex[i] != ex[j]:
                return False
            i+=1
            j-=1
        return True

