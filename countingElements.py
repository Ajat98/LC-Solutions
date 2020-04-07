class Solution:
    def countElements(self, arr: List[int]) -> int:
    
        arr_sort = sorted(set(arr))
        count = 0
        
        for i in range(len(arr_sort)-1):
            if (arr_sort[i]+1) == arr_sort[i+1]:
                count +=  arr.count(arr_sort[i])
        
        return count
