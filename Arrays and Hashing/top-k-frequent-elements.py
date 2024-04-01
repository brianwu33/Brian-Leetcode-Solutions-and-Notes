# Note: Counter.most_common() use heap
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
    
# When heap implementation required
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
    
        # Initialize a min-heap
        heap = []
        
        # Iterate over the frequency map
        for num, freq in freq_map.items():
            # Push (frequency, element) as a tuple
            heapq.heappush(heap, (freq, num))
            # If the heap size exceeds k, remove the smallest frequency element
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the elements from the heap
        top_k_elements = [num for _, num in heap]
        return top_k_elements
    
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		frequency = {}
		for num in nums:
			if num not in frequency:
				frequency[num] = 1
			else:
				frequency[num] = frequency[num] + 1
		frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
		result = list(frequency.keys())[:k]
		return result
		
#Time Complexity : O(n * log(n))
#Space Complexity : O(n)

        