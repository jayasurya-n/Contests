import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n = ii()
        arr = lii()
        hash = set()

        for num in arr:
            if(num!=-1):
                hash.add(num^seed)
        
        hash = list(hash)
        if len(hash)==0 or (len(hash)==1 and hash[0]^seed!=0):return yes
        return no

if __name__ == "__main__":
    yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)