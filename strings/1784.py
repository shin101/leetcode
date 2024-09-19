class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen = False
        separator = False

        for i in range(len(s)):
            if s[i]=="1" and separator == False:
                seen = True
            elif s[i]=="1" and separator == True:
                return False
            elif s[i]=="0" and seen == True:
                separator = True
        
        return True

            

            


