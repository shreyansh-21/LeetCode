class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result =[]
        minimum = float('inf')
        for i in range(len(arr)-1):
            a = arr[i+1] -arr[i]
            if a < minimum:
                minimum = a
                result.clear()
            if a == minimum:
                result.append([arr[i] ,arr[i+1]])
        return result


        