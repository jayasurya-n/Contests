from typing import List,Optional
import sys
class Solution:
    def FindBits(self, n : int, x : int) -> int:
        binary = ''
        while x>0:
            binary=str(x%2)+binary
            x= x//2
        zeroes = n-len(binary)
        for i in binary:
            if(i=='0'):zeroes+=1
        return 2**zeroes

# time complexity: O(logn)
# space complexity: O(logn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        x = int(input().strip())
        print(Solution().FindBits(n,x))