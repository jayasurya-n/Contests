from typing import List,Optional
import sys
class Solution:
    def longestSubarray(self, n : int, arr : List[int]) -> int:
        xor = 0
        ans = 0
        hashMap = dict()
        hashMap[0] = -1
        for i in range(n):
            xor^=arr[i]
            if xor in hashMap:
                ans = max(ans,i-hashMap[xor])
            else:
                hashMap[xor] = i 
        return ans


# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().longestSubarray(n,arr))