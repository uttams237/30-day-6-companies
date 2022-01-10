class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        if n<3:
            return 0
        dpinc=[0 for i in range(n)]
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                dpinc[i]=dpinc[i-1]+1
        
        dpdec= [0 for i in range(n)]
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                dpdec[i]=dpdec[i+1]+1
                
        ans,ind=-1,0
        for i in range(n):
            if dpinc[i]+dpdec[i]>ans and dpinc[i]!=0 and dpdec[i]!=0:
                ans=dpinc[i]+dpdec[i]
                ind=i

                
        if ind!=0 and ind!=(n-1):
            return ans+1
        
        return 0
