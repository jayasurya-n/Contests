from typing import List,Optional
import sys
class Solution:
    def maximiseExpression(self,arr) -> int:
        arr.sort()
        return arr[n-1]+arr[n-2]-arr[0]


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().maximiseExpression(arr))