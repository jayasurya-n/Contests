from typing import List,Optional
import sys
class Solution:
    def merge(self,arr,low,mid,high):
        temp = []
        inversions = 0
        i,j=low,mid+1

        while(i<=mid and j<=high):
            if(arr[i]<=arr[j]):
                temp.append(arr[i])
                i+=1
            else:
                inversions+=mid-i+1
                temp.append(arr[j])
                j+=1

        while(i<=mid):
            temp.append(arr[i])
            i+=1
        
        while(j<=high):
            temp.append(arr[j])
            j+=1
        
        for i in range(low,high+1):
            arr[i] = temp[i-low]
        return inversions

    def inversions(self,arr,low,high):
        if(low>=high):
            return 0
        cnt = 0
        mid = (low+high)//2
        cnt+=self.inversions(arr,low,mid)
        cnt+=self.inversions(arr,mid+1,high)
        cnt+=self.merge(arr,low,mid,high)
        return cnt

    def run(self) -> Optional[list]:
        n = int(input().strip())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        
        if(sorted(a)!=sorted(b)):return "NO"

        if((self.inversions(a,0,len(a)-1)-self.inversions(b,0,len(b)-1))%2==0):return "YES"
        else:return "NO"




# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())