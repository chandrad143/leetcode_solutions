class Solution(object):
    def findNumbers(self,nums):
        """ Prorgam to find th count of even digit numbers in an array
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count
