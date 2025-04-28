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
        
        ans = [None]*n
        mini,maxi = 1,n
        ind = arr.index(-1)
        
        for i in range(1,max(arr)+1):
            if(i%2==1):
                for j in range(ind):
                    if(arr[j]==i):
                        ans[j] = maxi
                        maxi-=1
                
                for j in range(n-1,ind,-1):
                    if(arr[j]==i):
                        ans[j] = maxi
                        maxi-=1
            else:
                for j in range(ind):
                    if(arr[j]==i):
                        ans[j] = mini
                        mini+=1
                
                for j in range(n-1,ind,-1):
                    if(arr[j]==i):
                        ans[j] = mini
                        mini+=1
        
        ans[ind] = mini
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)