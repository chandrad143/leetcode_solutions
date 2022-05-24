class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        index = 0
        
        while index < len(arr):
            if arr[index]==0:
                arr.insert(index+1,0)
                index = index+2
                arr.pop()
            else:
                index +=1