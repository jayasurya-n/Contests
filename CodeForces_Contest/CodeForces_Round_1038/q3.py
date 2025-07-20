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
        points = []
        for i in range(n):
            x,y = lii()
            points.append([x,y,i+1])

        x = [p[2] for p in sorted(points,key=lambda x:x[0])]
        y = [p[2] for p in sorted(points,key=lambda x:x[1])]


        half = n//2
        xL = set(x[:half])
        xR = set(x[half:])
        yL = set(y[:half])
        yR = set(y[half:])

        # print(xL,xR)
        # print(yL,yR)

        Q1 = list(xR&yR)
        Q3 = list(xL&yL)
        Q2 = list(xL&yR)
        Q4 = list(xR&yL)

        for i in range(len(Q1)):
            print(Q1[i],Q3[i])
        
        for i in range(len(Q2)):
            print(Q2[i],Q4[i])


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
