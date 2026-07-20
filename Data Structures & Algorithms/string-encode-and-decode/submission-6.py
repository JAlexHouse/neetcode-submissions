class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ""
        for s in strs:
            finalStr += str(len(s)) + "#" + s
        print(finalStr)
        return finalStr

    def decode(self, s: str) -> List[str]:
        finalStrs = []

        idx = 0
        while (idx < len(s) - 1):
            strLen = ""
            while s[idx] != "#":
                strLen += str(s[idx])
                idx += 1
            
            idx += 1
            strLen = int(strLen)

            word = ""
            for i in range(idx, idx + strLen):
                word += s[i]
            idx = idx + strLen
            finalStrs.append(word)

        return finalStrs
