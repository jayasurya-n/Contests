from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,m,k = list(map(int,input().strip().split()))
        path = input().strip()

        logs = [i for i in range(n) if path[i]=='L']
        logs.append(n)

        i = -1
        next_log = 0

        while i<n:
            if(log[next_log]-i<=m):
                i = log[next_log]
            else:
                i+=m
                if(i>n-1):
                    return "YES"
                
            next_log+=1

        





# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())