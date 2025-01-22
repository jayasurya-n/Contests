from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def canSort(self, arr, frozen):
        cnt = 0
        for i,num in enumerate(frozen):
            if(num==0 and arr[i]==1):cnt+=1
        
        for i in range(len(frozen)-1,-1,-1):
            if(frozen[i]==0):
                if(cnt>0):
                    arr[i]=1
                    cnt-=1
                else:arr[i]=0
        
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):return False
        return True

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))