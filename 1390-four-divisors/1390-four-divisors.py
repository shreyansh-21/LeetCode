# only possible when p^3 = {1,p,p^2,p^3} or pxq where p&q are distinctive prime numbers for{1,p,q,pq}

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divisors = set()
            for i in range(1,int(math.sqrt(n)+1)):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)#aisa karne se ek hi time pe do mil jaten hain aur i*i wala logic sustain karta hai
                # early break: agar 4 se zyada ho gaye    
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                total += sum(divisors)
        return total