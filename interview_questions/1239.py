# samsung 

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # keep track of all the unique words
        # for every word in arr keep appending to unique words
        # if they're all unique, increase max length and append to unique arr

        maxLength = 0
        uniq = [""]

        def isValid(s):
            return(len(s) == len(set(s)))

        for word in arr: 
            for j in uniq:
                temp = word + j
                if isValid(temp):
                    uniq.append(temp)
                    maxLength = max(maxLength, len(temp))

        return maxLength

