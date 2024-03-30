class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N)
        my_counter = Counter(nums)
        # O(N log k)
        most_frequent_elements = my_counter.most_common(k)
        result = []
        # O(k)
        for x in most_frequent_elements:
            result.append(x[0])
        return result

        