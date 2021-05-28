# queue.py

class queue:
    def __init__(self, iterable, maximum):
        if iterable == None:
            self.l = []
        else:
            self.l = list(iterable)
            
        self.maximum = maximum

        self.__normalize()
    
    def push(self, item):
        self.l.insert(0, item)
        self.__normalize()
        
    def remove(self, index):
        return self.l.pop(index)
    
    def insert(self, index, item):
        self.l.insert(index, item)
        self.__normalize()
        
    def pop(self):
        return self.l.pop()
    
    def clear(self):
        return self.l.clear()
        
    def __normalize(self):
        if self.maximum:
            while len(self.l) > self.maximum:
                self.l.pop()
                
    def __len__(self):
        return len(self.l)

    def __bool__(self):
        return bool(self.l)

    def __iter__(self):
        yield from self.l
        
    def __setitem__(self, index, item):
        self.l[index] = item
        
    def __getitem__(self, index):
        return self.l[index]

    def __str__(self):
        return 'queue({})'.format(self.l)
