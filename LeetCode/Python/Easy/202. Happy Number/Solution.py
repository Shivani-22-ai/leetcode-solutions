def sos(n):
    s=0
    while(n>0):
        s = s + (n%10)*(n%10)
        n = n//10
    return s

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen and n!=1:
            seen.add(n)
            n = sos(n)
        if(n==1):
            return True
        else:
            return False

        