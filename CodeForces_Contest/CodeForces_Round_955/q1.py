from typing import List
import sys
class Solution:
    def f(self, nums: List[int]) -> bool:
        pass

# time complexity: O(n) 
# space complexity: O(1) 
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        print(Solution().f(nums))