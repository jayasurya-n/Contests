from typing import List,Optional
import sys
class Solution:
    def func(self, arr,n,k) -> Optional[int]:
        arr.sort()
        ans = 0
        for i in range(len(arr)-1):
            ans+=2*arr[i]-1
        return ans




# time complexity: O(n)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,k = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n,k))