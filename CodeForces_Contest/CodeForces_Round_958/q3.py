from typing import List,Optional
import sys
class Solution:
    def func(self, n,m,k) -> Optional[int]:
        ans = []
        ans.extend(range(n,m,-1))
        ans.extend(range(1,m+1))
        return ans



# time complexity: O(n)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,m,k = list(map(int,input().strip().split()))
        arr = Solution().func(n,m,k)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()