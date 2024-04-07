class Solution:
    def checkValidString(self, s: str) -> bool:
        open_cnt = 0
        close_cnt = 0

        for i in range(len(s)):
            if s[i] == "(" or s[i]=="*":
                open_cnt += 1
            else:
                open_cnt -= 1

            if s[len(s)-1-i] == ")" or s[len(s)-1-i] == "*":
                close_cnt += 1
            else:
                close_cnt -= 1
        
            if open_cnt < 0 or close_cnt < 0:
                return False
        
        return True 