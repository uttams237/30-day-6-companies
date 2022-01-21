class Solution:
    def max_of_subarrays(self,arr,n,k):
        if n==k:
            return [max(arr)]
            
        dq=[]
        for i in range(k):
            while len(dq)>0 and arr[dq[-1]]<=arr[i]:
                dq.pop(-1)
            dq.append(i)
            
        ans=[]

        for j in range(k,n):
            ans.append(arr[dq[0]])
            i=j-k
            while len(dq)>0 and dq[0]<=i:
                dq.pop(0)
            while len(dq)>0 and arr[dq[-1]]<=arr[j]:
                dq.pop(-1)
            dq.append(j)
            
        ans.append(arr[dq[0]])
            
        return ans
