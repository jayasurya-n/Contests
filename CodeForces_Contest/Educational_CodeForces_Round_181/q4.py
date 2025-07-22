import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n,m = lii()
        mod = 998244353

        ends = [[] for _ in range(m+1)]
        nume = deno = 1
        for _ in range(n):
            l,r,p,q = lii()
            w = p*modinv(q-p,mod)%mod
            ends[r].append([l,r,w])
            nume = nume*(q-p)%mod
            deno = deno*q%mod

        dp = [0]*(m+1)
        dp[0] = 1

        for i in range(1,m+1):
            ans = 0
            for l,r,w in ends[i]:
                ans+=dp[l-1]*w
            dp[i]=ans%mod

        return dp[m]*nume*(modinv(deno,mod))%mod
        

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()
        print(ans)