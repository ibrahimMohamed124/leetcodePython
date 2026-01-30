from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # sort by frequency (descending)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        res = []
        for num, freq in sorted_items[:k]:
            res.append(num)

        return res


