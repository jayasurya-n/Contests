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
        k-=1
        arr = lii()
        maxi = max(arr)

        arr = [(arr[i],i) for i in range(n)]
        arr.sort()

        start = 0
        for i in range(n):
            if(arr[i][1]==k):
                start = i
                break
        
        arr = [arr[i][0] for i in range(n)]
        reach = start
        water = 1
        for i in range(start,n):
            if(reach==n-1):break
            diff = arr[i+1]-arr[i]
            if(water+diff-1>arr[i] or water+diff>arr[i+1]):break
            water+=diff
            reach = i+1
        
        return yes if arr[reach]==maxi else no 


if __name__ == "__main__":
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)