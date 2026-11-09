from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies in O(N) time
        count = Counter(nums)
        
        # Step 2: Use a heap or most_common to get top k elements in O(N log k) time
        return [item for item, freq in count.most_common(k)]
