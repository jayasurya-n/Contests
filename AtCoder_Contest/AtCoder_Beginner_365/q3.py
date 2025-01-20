from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n,m = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        
        if(sum(arr)<=m):return "infinite"
        arr.sort()
        prefixSum = [0]*(n+1)
        for i in range(1,n+1):
            prefixSum[i] = prefixSum[i-1]+arr[i-1]
        
        index = -1    
        for i in range(n-1,-1,-1):
            if(prefixSum[i]+arr[i]*(n-i)<=m):
                index = i
                break
        
        if(index==-1):return m//n
        mini =  arr[index]
        maxi  = arr[index+1]
        
        for x in range(maxi-1,mini-1,-1):
            if(prefixSum[index+1]+x*(n-index-1)<=m):return x
              
        

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())