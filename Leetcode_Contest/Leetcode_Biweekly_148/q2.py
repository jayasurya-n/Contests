from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        ans = 0
        for i in range(len(arr)):
            ans+=abs(arr[i]-brr[i])
        
        arr.sort()
        brr.sort()
        cost = 0
        
        for i in range(len(arr)):
            cost+=abs(arr[i]-brr[i])
        
        if(cost==ans):return ans
        if(cost<ans):return min(ans,cost+k)

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        brr = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().minCost(arr,brr,k))