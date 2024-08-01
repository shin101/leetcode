class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for person in details:
            if int(person[-4:-2]) > 60 and (person[-5]=="F" or person[-5]=="M" or person[-5]=="O"):
                print(int(person[-4:-2]))
                res +=1


        return res
