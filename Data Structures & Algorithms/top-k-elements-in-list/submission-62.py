class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = []
        records = {}
        for num in nums:
            if num in records:
                records[num]+=1
            else:
                records[num] =1
        print(f"""records: {records}""")

        occs = []
        for num in records:
            occs.append(records[num])
        
        occs.sort()
        occs.reverse()

        itt = 0
        for occ in occs:
            if itt == k:
                break
            for num in records:
                if records[num] == occ and  num not in top_k:
                    top_k.append(num)

            itt += 1

        print(f"""top k: {top_k}""")
        return top_k
