class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split(" ")
        for i in range(len(title)):
            if len(title[i])>2:
                title[i] = title[i][0].upper() + title[i][1:].lower()
            else:
                title[i] = title[i].lower()
        return " ".join(title)
