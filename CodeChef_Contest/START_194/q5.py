from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n = ii()
        matrix = [list(map(int,input().strip())) for _ in range(n)]
        mod = 10**9+7

        ans = 1
        for i in range(n):
            ans*=matrix[i].count(1)
            ans%=mod
        
        # dp[i][x]: no of ways of choosing A1 to Ai-1, A(n/2+1) to A(n/2+i-1)
        # such that diff is x 
        dp = [[0]*(n*n+1) for _ in range((n//2)+2)]
        dp[1][0] = 1

        ways = [[0]*(2*n+1) for _ in range(n//2)]
        for i in range(n//2):
            for a1 in range(1,n+1):
                for a2 in range(1,n+1):
                    if(matrix[i][a1-1]==1 and matrix[i+(n//2)][a2-1]==1):
                        ways[i][a1-a2+n]+=1  

        for i in range(2,(n//2)+2):
            for x in range(0,n*n+1):
                for diff in range(-n,n+1):
                    if(x-diff>=0 and x-diff<=(n*n)):
                        dp[i][x]+=dp[i-1][x-diff]*ways[i-2][diff+n]
                        dp[i][x]%=mod

        return (ans-dp[(n//2)+1][0]+mod)%mod

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)