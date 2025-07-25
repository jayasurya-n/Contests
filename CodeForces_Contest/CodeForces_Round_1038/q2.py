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
        changes = extra = 0
        for _ in range(n):
            a,b,c,d = lii()
            changes+=abs(a-c)+abs(b-d)
            if(d<b and c>=a):extra+=a
            elif(d<b and a>=c):extra+=c
        
        return extra+(changes//2)


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)