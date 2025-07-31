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
        casinos = []
        for _ in range(n):
            casinos.append(lii())
        
        casinos.sort(key=lambda x:x[0])

        curr = k
        i = 0
        while i<n:
            l,r,out = casinos[i]
            if(r<curr):
                i+=1
                continue
            
            if(l<=curr<=r):
                curr = max(curr,out)
                i+=1
            else:break
        return curr


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)