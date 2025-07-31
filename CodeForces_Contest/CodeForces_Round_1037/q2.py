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

        ans = 0
        cnt = 0
        i = 0
        while i<n:
            if(arr[i]==0):cnt+=1
            else:cnt = 0

            if(cnt==k):
                ans+=1
                i+=1
                cnt = 0
            
            i+=1
        return ans    


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)