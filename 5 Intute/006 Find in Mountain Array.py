# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        # for peeak
        i,j=0,mountain_arr.length()-1
        
        while i<j:
            mid= (i+j)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                i=mid+1
            else:
                j=mid
                
        peak=i
        
        i,j=0,peak
        # print(peak)

        while i<j:
            mid= (i+j)//2
            temp=mountain_arr.get(mid)
            if temp==target:
                return mid
            elif temp<target:
                i=mid+1
            else:
                j=mid
        
        if mountain_arr.get(i)==target:
            return i
                # 6 5 4 3 2 1
                
        i,j=peak+1,mountain_arr.length()-1
        while i<j:
            mid=(i+j)//2
            temp=mountain_arr.get(mid)
            # print(temp)
            if temp==target:
                return mid
            elif temp<target:
                j=mid
            else:
                i=mid+1
                
        if mountain_arr.get(i)==target:
            return i
                
                
        return -1
