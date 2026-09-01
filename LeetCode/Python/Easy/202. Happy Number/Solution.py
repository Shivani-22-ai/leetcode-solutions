def sod(n):
    s = 0
    while(n>0):
        s = s + n%10
        n = n//10
    return s
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n!=1 and n not in s:
            s.add(n)
            n = sod(n)
        if n==1:
            return True
        else:
            return False


        