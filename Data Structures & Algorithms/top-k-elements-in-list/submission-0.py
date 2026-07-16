class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqTable = {}
        for num in nums:
            numFreq = freqTable.get(num)
            if (numFreq is None):
                freqTable[num] = 1
            else:
                freqTable[num] += 1
        
        sortedFreqTable = sorted(freqTable.items(), key=lambda x:x[1], reverse=True)
        return [key for key, idx in sortedFreqTable][:k]