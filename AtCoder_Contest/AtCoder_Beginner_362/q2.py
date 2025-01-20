from typing import List,Optional
import sys
class Solution:
    def solve(self,a,b,c):
        distab = (a[0]-b[0])**2 + (a[1]-b[1])**2
        distbc = (c[0]-b[0])**2 + (c[1]-b[1])**2
        distac = (a[0]-c[0])**2 + (a[1]-c[1])**2
        if(distab+distbc==distac):return True
        return False

        return True
    def run(self) -> Optional[list]:
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        c = list(map(int,input().strip().split()))

        if(self.solve(a,b,c) or 
            self.solve(a,c,b) or
            self.solve(c,a,b)):return "Yes"
        return "No"





# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())