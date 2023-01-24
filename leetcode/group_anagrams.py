class Solution:
    def groupAnagrams(self, strs):
        """

        :type strs: object
        """
        outerList = []
        dict = {}
        for str in strs:
            character_array = list(str)
            character_array.sort()
            s = ""
            for e in character_array:
                s = s + e
            if s not in dict:
                dict[s] =[]
            dict[s].append(strs)

        for s in dict:
            outerList.append(dict[s])
        return outerList




