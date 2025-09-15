class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        res = []
        for string in strs:
            sorted_str = sorted(string)
            sorted_str = "".join(sorted_str)
            if sorted_str in dic:
                dic[sorted_str].append(string)
            else:
                dic[sorted_str] = [string,]
        for key, value in dic.items():
            res.append(value)
        return res
