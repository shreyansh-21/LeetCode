#Python3 Code
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cur_five, cur_ten = 0, 0
        for doller in bills:
            if doller == 5:
                cur_five += 1
            elif doller == 10:
                cur_five -= 1
                cur_ten += 1
            elif cur_ten > 0:
                cur_ten -= 1
                cur_five -= 1
            else:
                cur_five -= 3
            
            if cur_five < 0:
                return False
        
        return True