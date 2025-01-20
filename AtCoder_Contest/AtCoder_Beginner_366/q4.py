from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def run(self):
        n = int(input().strip())
        p = []
        for i in range(n):
            arr = [[] for _ in range(n)]
            for j in range(n):
                arr[j] = list(map(int,input().strip().split()))
                
            innerP = [[0]*n for _ in range(n)]
            for a in range(0,n):
                for b in range(0,n):
                    innerP[a][b] = arr[a][b]
                    if a>0:innerP[a][b] += innerP[a-1][b]
                    if b>0:innerP[a][b] += innerP[a][b-1]
                    if a>0 and b>0:innerP[a][b] -= innerP[a-1][b-1]
            p.append(innerP)
        
        q = int(input().strip())
        for _ in range(q):
            x1,x2,y1,y2,z1,z2 = list(map(int,input().strip().split()))
            x1,x2,y1,y2,z1,z2 = x1-1,x2-1,y1-1,y2-1,z1-1,z2-1
            ans = 0
            for i in range(x1,x2+1):
                sum = 0
                sum = p[i][y2][z2]
                if(y1>0):sum-=p[i][y1-1][z2]
                if(z1>0):sum-=p[i][y2][z1-1]
                if (y1>0 and z1>0):sum+=p[i][y1-1][z1-1]
                ans+=sum
            print(ans)
        
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        Solution().run()