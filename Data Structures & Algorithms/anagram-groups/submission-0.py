class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            sortedwords="".join(sorted(word))
            if sortedwords not in groups:
                groups[sortedwords]=[]
            groups[sortedwords].append(word)
        return list(groups.values())