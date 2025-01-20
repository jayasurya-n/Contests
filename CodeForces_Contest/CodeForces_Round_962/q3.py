from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,q = list(map(int,input().strip().split()))
        a = input().strip()
        b = input().strip()

        freqA = [[0]*26 for _ in range(len(a))]
        freqB = [[0]*26 for _ in range(len(b))]

        freqA[0][ord(a[0])-97]=1
        
        for i in range(1,len(a)):
            for j in range(26):
                if(j==ord(a[i])-97):
                    freqA[i][j]+=freqA[i-1][j]+1
                else:
                    freqA[i][j]=freqA[i-1][j]

        freqB[0][ord(b[0])-97]=1

        for i in range(1,len(b)):
            for j in range(26):
                if(j==ord(b[i])-97):
                    freqB[i][j]+=freqB[i-1][j]+1
                else:
                    freqB[i][j]=freqB[i-1][j]
        
        for _ in range(q):
            l,r = list(map(int,input().strip().split()))
            ope = 0
            cntA = [0]*26
            cntB = [0]*26
            for j in range(26):
                if(l==1):cntA[j] = freqA[r-1][j]
                else:cntA[j] = freqA[r-1][j] - freqA[l-2][j]  

                if(l==1):cntB[j] = freqB[r-1][j]
                else:cntB[j] = freqB[r-1][j] - freqB[l-2][j]  

            same = 0
            for i in range(26):
                if(cntA[i]!=0 and cntB[i]!=0):
                    same+=min(cntA[i],cntB[i])
            print(r-l+1-same)
                


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        Solution().run()