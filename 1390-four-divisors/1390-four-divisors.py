# only possible when p^3 = {1,p,p^2,p^3} or pxq where p&q are distinctive prime numbers for{1,p,q,pq}

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for n in nums:
            divisors = set()
            i = 1

            while i * i <= n:
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)#aisa karne se ek hi time pe do mil jaten hain aur i*i wala logic sustain karta hai

                # early break: agar 4 se zyada ho gaye
                if len(divisors) > 4:
                    break

                i += 1

            if len(divisors) == 4:
                total_sum += sum(divisors)

        return total_sum

        