def sod(n):
    s = 0
    while(n>0):
        s = s + n%10
        n = n//10
    return s
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n!=1 and sod(n) not in s:
            n = sod(n)
            s.add(n)
        if n==1:
            return True
        else:
            return False


        