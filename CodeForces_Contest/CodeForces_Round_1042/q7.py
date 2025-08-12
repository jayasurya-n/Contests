import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

def solve(n,mod):
    P = [0] *(n+1)
    P[1] = 1
    for x in range(2,n+1):
        P[x] = x*pow(P[x-1], 2, mod) % mod
        P[x] = P[x]*pow(x-1,mod-2,mod) % mod
    return P

class Solution:
    def run(self):
        n,k = lii()
        arr = lii()
        mod = 10**9+7

        min_heap = arr
        heapq.heapify(min_heap)
        
        score = 1
        while k>0:
            num = heapq.heappop(min_heap)
            ope = 1<<(min(num-1,30))
            if(k>=ope):
                k-=ope
                score=score*P[num]%mod
            else:
                k-=1
                score=score*num%mod
                for i in range(1,min(31,num)):
                    heapq.heappush(min_heap,i)
        
        return score

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    P = solve(32,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)