class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in groups:
                groups[key].append(str)
            else:
                groups[key] = [str]

        return list(groups.values())
        