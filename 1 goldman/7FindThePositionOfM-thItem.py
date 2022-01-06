class Solution:
    def findPosition(self, N , M , K):
        # code here
        return ((M+K-2)%N)+1
