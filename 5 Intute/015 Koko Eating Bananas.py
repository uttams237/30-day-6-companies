import math

def func(pile,mid):
    ans=0
    for ele in pile:
        ans+=math.ceil(ele/mid)
    return ans



class Solution:        
    def minEatingSpeed(self, pile: List[int], h: int) -> int:
        low,high= 0,max(pile)
        
        while low<high:
            mid= (low+high)//2
            
            tt= func(pile,mid)
            
            if tt<=h:
                high=mid
            else:
                low= mid+1
        
        return low
