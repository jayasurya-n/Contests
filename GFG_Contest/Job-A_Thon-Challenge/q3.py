from typing import List,Optional
import sys
class Solution:
    def RangeSumDigits(self, n : int, arr : List[int], q : int, queries : List[List[int]]) -> List[int]:
        prefixSum = [-1]*n
        prefixSum[0] = arr[0]
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1]+arr[i]
        
        totalSum = sum(arr)
        map = {}

        for i in range(0,n):
            map[arr[i]] = len(str(arr[i]))
        
        # print(map)
        digitsPrefixSum = [-1]*n
        digitsPrefixSum[0] = map[arr[0]]
        for i in range(1,n):
            digitsPrefixSum[i] = digitsPrefixSum[i-1]+map[arr[i]]
        # print(digitsPrefixSum)

        digits=  [0]*n
        map2 = {}
        for i in range(n):
            map[i] = 2
        
        ans = []
        for i in range(q):
            if(queries[i][0]==1):
                l = queries[i][1]-1
                r = queries[i][2]-1
                if(l==0):
                    ans.append(totalSum-prefixSum[r])
                else:
                    ans.append(totalSum-
                (prefixSum[r]-prefixSum[l-1]))
            else:
                l = queries[i][1]-1
                r = queries[i][2]-1
                all = True
                for i in range(l,r+1):
                    if(map2[i]>0):
                        all = False
                        map2[i]-=1

                if(all==False):
                    for i in range(l,r+1):
                        arr[i] = len(str(arr[i]))
                        prefixSum = [-1]*n
                        prefixSum[0] = arr[0]
                        for i in range(1,n):
                            prefixSum[i] = prefixSum[i-1]+arr[i]
                

                

                
                
                
        
    



# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        q = int(input().strip())
        queries =  [list(map(int,input().strip().split())) for _ in range(q)]
        print(Solution().RangeSumDigits(n,arr,q,queries))