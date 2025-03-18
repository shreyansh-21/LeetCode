class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l_mult = 1
        r_mult = 1

        l_arr = [0]*n
        r_arr = [0]*n

        for  i in range(n):
            j = -i-1 #Traversing with negative index from back
            l_arr[i] = l_mult
            r_arr[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]
        return[l*r for l,r in zip(l_arr , r_arr)]
        