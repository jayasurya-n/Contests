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

        factors = []
        i = 1
        while i*i<=n:
            if(n%i==0):
                factors.append(i)
                factors.append(n//i)
            i+=1

        for L in range(1,66):
            x = (L//2)-1 if L%2==0 else (L-1)//2 
            y = (L//2) if L%2==0 else (L-1)//2

            l1,r1 = x+1,1<<x
            l2,r2 = y+1,1<<y

            for d in factors:
                if(l1<=d<=r1 and l2<=n//d<=r2):
                    return L

        return -1

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)