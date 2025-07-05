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
        arr = lii()
        if(n==1):return 0

        all_gcd = arr[0]
        for i in range(1,n):
            all_gcd = gcd(all_gcd,arr[i]) 

        cnt = arr.count(all_gcd)
        if(cnt>0):return n-cnt

        # ans: (n-1)+(l-1)
        # dp = [10**10]*(max(arr)+1)
        # q = deque([])
        # for num in arr:
        #     dp[num] = 1
        #     q.append(num)
        
        # while q:
        #     num1 = q.popleft()
        #     if(num1==all_gcd):break # since we are going step wise
        #     for num2 in arr:
        #         g = gcd(num1,num2)
        #         if(dp[g]>1+dp[num1]):
        #             q.append(g)
        #             dp[g] = 1+dp[num1]
        
        # return dp[all_gcd]+n-2

        dp = defaultdict(int)
        for num in arr:
            new_dp = dp.copy()
            if(num not in dp or dp[num]>1):new_dp[num] = 1
            for g,length in dp.items():
                new_gcd = gcd(g,num)
                if(new_gcd not in new_dp or 
                   (new_dp[new_gcd]>1+length)):new_dp[new_gcd] = 1+length
            dp = new_dp
        
        return dp[all_gcd]+n-2

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)