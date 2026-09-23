import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        primes = [True]*(n+1)
        primes[0] = False
        primes[1] = False
        for i in range(2,math.floor(math.sqrt(n))+1):
            if primes[i]:
                for j in range(i*i,n+1,i):
                    primes[j] = False
        return sum(primes)    