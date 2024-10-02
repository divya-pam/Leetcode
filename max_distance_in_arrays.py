class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum=arrays[0][0]
        maximum=arrays[0][-1]
        max_dif = 0
        for i in range(1, len(arrays)):
            max_dif = max(max_dif, max(arrays[i][-1]-minimum, maximum-arrays[i][0]))
            maximum = max(arrays[i][-1], maximum)
            minimum = min(minimum, arrays[i][0])

        return max_dif
