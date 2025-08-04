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
        arr = lii()

        ans = 0
        for i in range(1,n+1):
            pos = arr.index(i)

            left = right = 0
            for j in range(pos):
                if(arr[j]>arr[pos]):left+=1

            for j in range(pos+1,len(arr)):
                if(arr[j]<2*n-arr[pos]):right+=1
            
            ans+=min(left,right)
            arr = arr[:pos]+arr[pos+1:]
            
        return ans

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)