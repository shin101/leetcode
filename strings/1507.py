class Solution:
    def reformatDate(self, date: str) -> str:
        res = ""
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        date = date.split(" ")
        print(date)

        if len(date[0])==3:
            day = "0" + date[0][0]
        else:
            day = date[0][0:2]

        res+=date[2]+"-"+months[date[1]]+"-"+day


        return res