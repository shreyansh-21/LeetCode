class Solution:
    def subarraySum(self, numbers: List[int], target: int) -> int:
        answer = 0
        running_sum = 0

        # stores how many times each sum has appeared
        sum_count = {0: 1}
        
        for value in numbers:
            running_sum += value

            needed_sum = running_sum - target
            if needed_sum in sum_count:
                answer += sum_count[needed_sum]

            sum_count[running_sum] = sum_count.get(running_sum, 0) + 1
        
        return answer
