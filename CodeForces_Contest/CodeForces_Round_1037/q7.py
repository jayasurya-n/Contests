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

        ans = 0
        for median in range(min(n,100)+1):
            psum = [0]*(n+1)
            pmin = [0]*(n+1)

            for j in range(1,n+1):
                psum[j] = psum[j-1]+(1 if arr[j-1]>=median else -1)
                pmin[j] = min(pmin[j-1],psum[j])
            
            smax = [0]*(n+1)
            smax[n] = psum[n] 
            for j in range(n-1,-1,-1,):
                smax[j] = max(smax[j+1],psum[j])
            

            for j in range(1,n+1):
                if(psum[j]>=pmin[j-1] or psum[j-1]<=smax[j]):
                    ans = max(ans,median-arr[j-1])
        
        return ans

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)