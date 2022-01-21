class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        # if k==1:
        #     return arr
        dq=[]
        for i in range(k):
            while len(dq)>0 and arr[dq[-1]]<arr[i]:
                dq.pop()
            dq.append(i)
            
        ans=[]
        for j in range(k,n):
            ans.append(arr[dq[0]])
            i=j-k
            while len(dq)>0 and arr[dq[-1]]<=arr[j]:
                dq.pop()
            while len(dq)>0 and dq[0]<=i:
                dq.pop(0)
            dq.append(j)
            # ans.append(arr[dq[0]])
            
        ans.append(arr[dq[0]])
        return ans
            
