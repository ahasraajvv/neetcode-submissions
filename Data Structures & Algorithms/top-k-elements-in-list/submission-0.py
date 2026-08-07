from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {} # empty hashmap

        for num in nums:

            if num in hash_map:

                hash_map[num] += 1

            else:
                hash_map[num] = 1

    

        sorted_items = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

        K_keys = [item[0] for item in sorted_items[:k]]

        return K_keys 



        
