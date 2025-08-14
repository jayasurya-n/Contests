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
        A = lii()
        B = lii()

        for i in range(n):
            if(A[i]>B[i]):
                A[i],B[i] = B[i],A[i]

        A = [0]+A
        B = [0]+B

        dp = [[0]*2 for _ in range(n+1)]
        ans = 0
        for i in range(1,n+1):
            if(A[i]>B[i-1]):dp[i][0] = 1+max(dp[i-1])
            elif(A[i]>A[i-1]):dp[i][0] = 1+dp[i-1][0]
            else:dp[i][0] = 1
            
            if(B[i]>B[i-1]):dp[i][1] = 1+max(dp[i-1])
            elif(B[i]>A[i-1]):dp[i][1] = 1+dp[i-1][0]
            else:dp[i][1] = 1

            maxi = max(dp[i])
            ans+=maxi

        return ans
        

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)