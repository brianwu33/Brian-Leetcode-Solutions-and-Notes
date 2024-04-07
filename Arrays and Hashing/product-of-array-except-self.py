class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        output_product = [1] * n

        # Find Prefix Product for each element, 1 if no prefix
        # Find Suffix Product for each element, 1 if no suffix
        # Starting with 1 since we initialize all elements as 1
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1] 
        # Starting with n - 2 since we initialize all elements as 1 (including n - 1)
        for i in range(n - 2, -1, -1):
            suffix_product[i]  = suffix_product[i + 1] * nums[i + 1]
        # Output = Prefix * Suffix
        for i in range(len(nums)):
            output_product[i] = prefix_product[i] * suffix_product[i]
        
        return output_product
        
        # Can Combine either prefix_product & suffix_product in 1 loop OR
        # suffix_product and output_product in 1 loop to reduct Runtime and Space to O(2n)