from typing import List,Optional
import sys
class Solution:
    def func(self, arr:List,n:int,k:int) -> Optional[int]:
        ans = sys.maxsize
        arr.sort()
        for i in range(k+1):
            ans = min(ans,arr[n-k-1+i]-arr[i])
        return ans





# time complexity: O(nlogn+k)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,k = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n,k))