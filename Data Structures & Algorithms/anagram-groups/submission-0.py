class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortToIdx = {}
        for idx, stri in enumerate(strs):
            sortedStr = "".join(sorted(stri))
            anaIdxs = sortToIdx.get(sortedStr)
            if (anaIdxs is None):
                sortToIdx[sortedStr] = [idx]
            else:
                sortToIdx[sortedStr] = anaIdxs + [idx]
        
        solution = []
        for ana, idxs in sortToIdx.items():
            solution.append([strs[i] for i in idxs])

        return solution
