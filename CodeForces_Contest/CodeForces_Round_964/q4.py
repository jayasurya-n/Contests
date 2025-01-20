from typing import List,Optional
from collections import deque
import sys
class Solution:

    def run(self):
        s = input().strip()
        t = input().strip()
        
        i,j = 0,0
        cnt = 0
        l = [c for c in s]
        while(i<len(s) and j<len(t)):
            if(s[i]==t[j] or s[i]=='?'):
                l[i] = t[j]
                j+=1
                cnt+=1
            i+=1
        
        if(cnt!=len(t)):print("NO")
        else:
            print("YES")
            for i in range(len(l)):
                if(l[i]=='?'):l[i]='a'
            print("".join(l))
            
            
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        Solution().run()