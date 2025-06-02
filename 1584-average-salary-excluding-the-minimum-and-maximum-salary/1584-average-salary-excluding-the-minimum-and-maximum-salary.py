class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return (sum(salary[1:-1]) / len(salary[1:-1])) if len(salary) > 2 else 0
        