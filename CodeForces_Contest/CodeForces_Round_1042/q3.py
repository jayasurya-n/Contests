import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n,k = lii()
        s = lii()
        t = lii()

        hash = defaultdict(int)
        for num in s:
            hash[(num%k)^seed]+=1
        
        for num in t:
            rem = num%k
            if(hash[rem^seed]>0):
                hash[rem^seed]-=1
                if(hash[rem^seed]==0):hash.pop(rem^seed)
            elif(hash[(k-rem)^seed]>0):
                hash[(k-rem)^seed]-=1
                if(hash[(k-rem)^seed]==0):hash.pop((k-rem)^seed)
            else:
                return no

        return yes


if __name__ == "__main__":
    yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)