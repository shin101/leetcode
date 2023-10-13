# permutation problems are good for using backtracking 

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # length must not be over 12
        # for num in range of 3 increments 
        # if satisfies condition, then continue to put it in backtrack recursion until curr idx pos is in length of s or there are 4 dots

        res = []
        if len(s)>12:
            return 
        
        def recurse(idx, dots, output):
            if dots == 4 and (idx == len(s)):
                res.append(output[:-1])
                return 
            if dots > 4 :
                return
            
            for i in range(idx,min(idx+3 ,len(s))):
                if int(s[idx:i+1]) < 256 and (s[idx]!="0" or idx==i):
                    recurse(i+1, dots+1, output+s[idx:i+1]+ ".")

    
        recurse(0, 0, "")
        return res


