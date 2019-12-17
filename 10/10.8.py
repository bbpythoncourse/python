from random import randint

class RandomQueue:
    
    def __init__(self, n): 
        self.items = []
        self.n = n

    def __str__(self):
        return str(self.items)

    def insert(self, item): 
        if len(self.items) == self.n:
            raise IndexError("full queue")
        self.items.append(item)

    def remove(self): 
        if self.is_empty(): 
            raise IndexError("empty queue")
        index = randint(0, len(self.items) - 1)
        return self.items.pop(index)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self): 
        return len(self.items) == self.n

    def clear(self): 
        self.items = []

q = RandomQueue(10)
q.insert(1)
print(str(q))
q.insert(5)
print(str(q))
q.insert(4)
print(str(q))
q.insert(7)
print(str(q))
q.insert(9)
print(str(q))
q.insert(2)
print(str(q))
q.remove()
print(str(q))
q.remove()
print(str(q))
q.remove()
print(str(q))
q.remove()
print(str(q))
q.remove()
print(str(q))
q.remove()
print(str(q))
