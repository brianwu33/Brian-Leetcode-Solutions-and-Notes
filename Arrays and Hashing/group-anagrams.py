class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        result = []
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(s)
            else:
                anagram_map[sorted_str] = [s]
        
        for str_list in anagram_map.values():
            result.append(str_list)

        return result
        