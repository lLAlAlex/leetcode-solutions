class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        primes = []
        min_distance = 999
        res = []
        
        def sieveOfErastothenes(left, right):
            prime = [True for i in range(right+1)]

            p = 2
            
            while p * p <= right:
                if prime[p] == True:
                    for i in range(p * p, right+1, p):
                        prime[i] = False
                p += 1
            
            for p in range(left, right + 1):
                if p == 1:
                    continue
                if prime[p]:
                    primes.append(p)
        
        sieveOfErastothenes(left, right)
        
        for i in range(1, len(primes)):
            if min_distance > (primes[i] - primes[i-1]):
                min_distance = (primes[i] - primes[i-1])
                
                if res:
                    res.pop()
                    res.pop()
                res.append(primes[i-1])
                res.append(primes[i])
        
        return res if res else [-1, -1]

obj = Solution()
print(obj.closestPrimes(1, 1000000))