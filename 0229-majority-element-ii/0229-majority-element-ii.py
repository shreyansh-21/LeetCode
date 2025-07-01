class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result=[]
        for k,v in freq.items():
            if v > len(nums)//3:#problem requires more that n//3 so dont use >=
                result.append(k)
        return result
        