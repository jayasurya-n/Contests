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

    def countPrimedivisors(self,ele,allPrimes):
        cnt = 0
        for i in range(len(allPrimes)):
            if(ele%allPrimes[i]==0):cnt+=1
        return cnt

    def PrimeInversions(self, n : int, arr : List[int]) -> int:
        maxi = max(arr)
        prime = [True]*(maxi+1)
        prime[0]=prime[1] = False

        p = 2
        while p*p<=maxi:
            if(prime[p]):
                for i in range(p*p,maxi+1,p):
                    prime[i] = False
            p+=1
        allPrimes = []
        for p in range(2,len(prime)):
            if(prime[p]):allPrimes.append(p)
        
        map = {}
        for num in arr:
            if num in map:continue
            temp = num
            cnt = 0
            for p in allPrimes:
                if p*p > num:break
                if temp % p == 0:
                    cnt += 1
                    while temp % p == 0:
                        temp //= p
            if temp>1:cnt+=1
            map[num] = cnt
        
        B = []
        for i in range(len(arr)):
            B.append(map[arr[i]])

        return self.inversions(B,0,len(B)-1)

# time complexity: O(nlogn+nlog(logn))
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().PrimeInversions(n,arr))