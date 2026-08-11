class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # First pass: left product (prefix)
        prefix = 1
        for i in range(n):
            answer[i] = prefix      # store product of elements to the left
            prefix *= nums[i]       # update prefix to include current element

        # Second pass: right product (suffix)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix     # multiply by product of elements to the right
            suffix *= nums[i]       # update suffix for next left index

        return answer


        