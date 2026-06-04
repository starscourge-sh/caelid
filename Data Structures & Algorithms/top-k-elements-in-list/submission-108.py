class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = []
        count = {}
        for n in nums:
            if n not in count:
                count[n] = nums.count(n)

        freq = [[] for i in range(0, len(nums)+1)]
        for n, c in count.items():
            c = count[n]
            freq[c].append(n)

        start = len(freq) - 1
        for i in range(start, 0, -1):
            for arr in freq[i]:
                print(arr)
                top_k.append(arr)
                if len(top_k) == k:
                    return top_k
                

