class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i)
        i=0
        j=len(l)-1
        while(i<=j):
            if l[i].lower() != l[j].lower():
                return False
            i+=1
            j-=1
        return True