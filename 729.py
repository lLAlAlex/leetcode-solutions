class MyCalendar(object):

    def __init__(self):
        self.data = []
    
    def binary_search(self, start, end):
        low = 0
        high = len(self.data) - 1
        
        while low <= high:
            mid = (high + low) // 2
            booked_start, booked_end = self.data[mid]
            if end <= booked_start: 
                high = mid - 1
            elif start >= booked_end:
                low = mid + 1
            else:
                return True
        return False

    def book(self, start, end):
        if self.binary_search(start, end):
            return False
    
        self.data.append((start, end))
        self.data.sort()
        
        return True
    
def main():
    calendar = MyCalendar()
    calendar.book(47, 50)
    calendar.book(33, 41)
    calendar.book(39, 45)
    calendar.book(33, 42)
    calendar.book(25, 32)
    calendar.book(26, 35)
    calendar.book(19, 25)
    calendar.book(3, 8)
    calendar.book(8, 13)
    calendar.book(18, 27)

if __name__ == '__main__':
    main()

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)