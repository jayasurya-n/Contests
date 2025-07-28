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
        q = deque(lii())
        
        ans = []
        small = 0
        while len(q)>1:
            if(small%2==0):
                left = q[0]
                right = q[-1]
                if(left<right):
                    ans.append('L')
                    ans.append('R')
                else:
                    ans.append('R')
                    ans.append('L')
            
            else:
                left = q[0]
                right = q[-1]

                if(left<right):
                    ans.append('R')
                    ans.append('L')
                else:
                    ans.append('L')
                    ans.append('R')
            
            q.popleft()
            q.pop()
            small+=1
        
        if(q):ans.append('L')
        return "".join(ans)

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)