class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in m:
                m[key].append(word)
            else:
                m[key] = [word]
        return list(m.values())
        

        