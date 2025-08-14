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

        freq = [0]*(n+1)
        ans1 = 0
        for c in arr:
            freq[c]+=1
            if(c!=1):ans1+=1
        
        newc = freq.index(max(freq))
        ans2 = 0 if newc==1 else 1
        for c in arr:
            if(c!=newc):ans2+=1
        
        return min(ans1,ans2)

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)