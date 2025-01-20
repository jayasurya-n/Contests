from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        maxi = n-1
        time = 0
        for i in range(n-2,-1,-1):
            if(arr[i]>=arr[maxi]):maxi = i
            else:time = max(time,maxi-i)
        return time
                
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