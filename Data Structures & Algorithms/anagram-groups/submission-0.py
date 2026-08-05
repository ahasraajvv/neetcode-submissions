class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {} # empty hash 

        for word in strs: # lets iterate through the list

            key = "".join(sorted(word)) # "".join (["a","c","t"]) -> "act"
            # Convert every anagram to the same sorted string to use as a hash map key.

            if key not in groups:
                groups[key] = [] 
            groups[key].append(word)

        return list(groups.values())



        