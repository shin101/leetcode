class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_cnt = 0
        ten_cnt = 0

        for bill in bills:
            if bill == 5:
                five_cnt +=1
            elif bill == 10:
                if five_cnt:
                    five_cnt-=1
                    ten_cnt+=1
                else:
                    return False
            elif bill == 20:
                if ten_cnt >= 1 and five_cnt >= 1:
                    ten_cnt -= 1
                    five_cnt -= 1
                elif five_cnt>=3:
                    five_cnt-=3
                else:
                    return False
            
        return True 
