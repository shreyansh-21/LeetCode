class Solution:
    def isValid(self, word: str) -> bool:
        regex = r"(?i)(?=^.*[b-df-hj-np-tv-z])(?=.*[aieou])^[a-z0-9]{3,}$"
        return re.search(regex, word) is not None