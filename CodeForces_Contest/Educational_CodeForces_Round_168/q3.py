from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n = int(input().strip())
        s = input().strip()
        ans  = 0
        stack = [('(',1)] 
        for i in range(1,len(s)):
            if(stack==[] or s[i]=='('):
                stack.append(('(',i+1))
            else:
                top = stack.pop()
                ans+=i+1-top[1]
        return ans

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())