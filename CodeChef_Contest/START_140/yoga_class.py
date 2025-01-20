class Solution:
    def yogaMoney(self,n,x,y):
        if(n==0):return 0
        if(n==1):return x

        dp = [0]*(n+1)
        dp[1] = x

        for i in range(2,n+1):
            dp[i] = max(dp[i-1]+x, dp[i-2]+y)
        return dp[n]


t = int(input().strip())
for i in range(t):
    n,x,y = list(map(int,input().strip().split()))
    print(Solution().yogaMoney(n,x,y))
