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
        arr = lii()

        # a subarray atleast of length k has median>=mid  
        def check(mid):
            pre = [0]*(n+1)
            for i in range(1,n+1):
                if(arr[i-1]>=mid):pre[i] = 1
                else:pre[i] = -1
                pre[i]+=pre[i-1]
            
            i = 0
            for j in range(k,n+1):
                if(pre[j]-pre[i]>=0):return [True,i+1,j]
                if(pre[j-k+1]<pre[i]):i = j-k+1
            return [False,-1,-1]
        
        
        low,high = 1,n
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)[0]):low = mid+1
            else:high = mid-1
        
        ans = check(high)
        return [high,ans[1],ans[2]]           


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)