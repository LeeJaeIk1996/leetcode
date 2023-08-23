class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list_dict = defaultdict(list)

        # strs를 순회하여 정렬
        for str in strs:
            list_dict[''.join(sorted(str))].append(str)

        return list(list_dict.values())