class PriorityQueue:
    
    def __init__(self, n):
        self.items = []
        self.n = n

    def __str__(self):   # podglądamy kolejkę
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        if len(self.items) == self.n:
            raise IndexError("full queue")
        self.items.append(item)
        self.items.sort()

    def remove(self):
        if self.is_empty(): 
            raise IndexError("empty queue")
    
        return self.items.pop() 

q = PriorityQueue(3)
q.insert(1)
print(str(q))
q.insert(5)
print(str(q))
q.remove()
print(str(q))
