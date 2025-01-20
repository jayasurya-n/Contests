from typing import List,Optional
import sys
class Solution:
    def func(self, arr) -> Optional[int]:
        # ans = 0
        # for i in range(0,6):
        #     for j in range(0,6-i):
        #         for ele in [(a,b,c),(a,c,b),(b,c,a),(b,a,c),(c,a,b),(c,a,b)]:
        #             prod = (ele[0]+i)*(ele[1]+j)*(ele[2]+5-i-j)
        #             ans = max(ans,prod)
        # return ans

        for i in range(5):
            arr[arr.index(min(arr))]+=1
        return arr[0]*arr[1]*arr[2]





# time complexity: O(1)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr))