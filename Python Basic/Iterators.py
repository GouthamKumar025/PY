class Mylist:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    # iterator
    
    def __iter__(self):
        return self
    
    #next method of iterator
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current

List = Mylist(1, 10)

for num in List:
    print(num)

