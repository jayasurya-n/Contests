from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n = int(input().strip())
        s = input().strip()

        zeros,ones = 0,0
        for i in range(0,len(s)-1):
            if(s[i]==s[i+1]):continue
            else:
                if(s[i]=='0'):zeros+=1
                else:ones+=1
        
        if(s[-1]=='1'):ones+=1
        else:zeros+=1
        # print(zeros,ones)
        if(ones>zeros):return 0
        elif(ones==zeros):return 1
        else:
            if(len(s)==1):return 1
            else:return 2



# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())