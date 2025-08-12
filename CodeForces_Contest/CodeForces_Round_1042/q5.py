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
        a = lii()
        b = lii()

        if(a[n-1]!=b[n-1]):return no

        for i in range(n-2,-1,-1):
            if(a[i]==b[i]):continue
            if(a[i]^b[i+1]==b[i] or a[i]^a[i+1]==b[i]):continue
            else:return no
        
        return yes

if __name__ == "__main__":
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)