class MyCalendar:

    def __init__(self):
        self.cal = []
        

    def book(self, start: int, end: int) -> bool:
        for s,e in self.cal:
            if start < e and end > s :
                return False

        self.cal.append((start,end))
        return True
    
