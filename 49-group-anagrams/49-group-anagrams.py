class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counter = collections.defaultdict(list)

        for word in strs:
            tmp = ''.join(sorted(word)) # aet
            counter[tmp].append(word)

        return list(counter.values())
