from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,m = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))

        arr.sort()
        n = len(arr)
        ans = 0
        hash = dict()

        i,j=0,0
        petals = 0

        while(i<n):
            if(hash=={}):
                if(arr[i]+petals<=m):
                    petals+=arr[i]
                    ans = max(ans,petals)
                    hash[arr[i]] = 1
                elif(arr[i]+petals>m):return ans
            else:
                if(arr[i]+petals<=m):
                    if(arr[i]<=1+min(hash.keys())):
                        petals+=arr[i]
                        ans = max(ans,petals)
                        hash[arr[i]] = hash.get(arr[i],0)+1
                    else:
                        while(j<n and 1+min(hash.keys())<arr[i]):
                            hash[arr[j]]-=1
                            petals-=arr[j]
                            if(hash[arr[j]]==0):hash.pop(arr[j])
                            j+=1
                            if(hash=={}):break
                        
                        hash[arr[i]] = 1
                        petals+=arr[i]
                        ans = max(ans,petals)
                
                elif(arr[i]+petals>m):
                    print(arr[i],hash)
                    while(j<n and petals+arr[i]>m):
                        if(hash=={}):break
                        hash[arr[j]]-=1
                        petals-=arr[j]
                        if(hash[arr[j]]==0):hash.pop(arr[j])
                        j+=1
                        print(hash)
                    
                    if(hash=={}):
                        if(arr[i]<=m):
                            petals+=arr[i]
                            ans = max(ans,petals)
                        else:return ans
                    else:
                        while(j<n and 1+min(hash.keys())<arr[i]):
                            hash[arr[j]]-=1
                            petals-=arr[j]
                            if(hash[arr[j]]==0):hash.pop(arr[j])
                            j+=1
                            if(hash=={}):break
                        hash[arr[i]] = 1
                        petals+=arr[i]
                        ans = max(ans,petals)
            i+=1
        return ans

                






# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())