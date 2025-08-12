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
        a = si()
        b = si()

        def solve(a):
            zeros = ones = 0
            prefix = [0]*n
            for i in range(n):
                if(a[i]=='1'):ones+=1
                else:zeros+=1
                prefix[i] = zeros-ones
            return prefix

        prea = solve(a)
        preb = solve(b)

        prea.sort()
        preb.sort()

        tasum = sum(prea)
        ans = psum = i = 0
        for j in range(n-1,-1,-1):
            while i<n and prea[i]+preb[j]<=0:
                psum+=prea[i]
                i+=1
            
            k = i
            ans+=tasum-2*psum+preb[j]*(n-2*k)

        return (n*n*(n+1)-ans)//2


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)