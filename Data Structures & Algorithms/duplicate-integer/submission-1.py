class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for ele in d:
            if d[ele]>1:
                return True

        return False