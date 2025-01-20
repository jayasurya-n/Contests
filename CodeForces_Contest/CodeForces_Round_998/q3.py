from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,k = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        arr.sort()
        i,j = 0,n-1
        ans = 0
        while(i<j):
            if(arr[i]+arr[j]==k):
                ans+=1
                i+=1
                j-=1
            elif(arr[i]+arr[j]<k):i+=1
            else:j-=1
        return ans

if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)