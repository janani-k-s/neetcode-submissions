class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=Counter(nums)
        final=result.most_common(k)
        return [i[0] for i in final]
        