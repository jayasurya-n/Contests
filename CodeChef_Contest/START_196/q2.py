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
        arr.sort()

        ans = sum(arr)

        low,high = arr[0],arr[1]
        cnt = 0
        while cnt<k:
            mid = (low+high+1)//2
            cnt+=1
            ans+=mid
            if(mid==high):break
            high = mid
        
        if(cnt<k):ans+=(k-cnt)*high
        return ans


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)