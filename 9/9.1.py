class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def __str__(self):
        if self.is_empty():
            return ""
        result = ""
        curr = self.head
        while curr.next != None: 
            result += " " + str(curr)
            curr = curr.next
        result += " " + str(curr)
        return result

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self): 
        if self.length == 0:
            raise ValueError("empty list")
        
        if self.head == self.tail:
            removed = self.head
            self.head = self.tail = None
            self.length -= 1
            return removed 

        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        removed = curr.next
        curr.next = None
        self.tail = curr
        self.length -= 1
        return removed

    def merge(self, other):   # klasy O(1)
    # Węzły z listy other są przepinane do listy self na jej koniec.
        if self.head == None:
            self.head = other.head
            self.length = other.length
            return
        if other.head == None:
            return

        self.tail.next = other.head
        self.length += other.count()
        self.tail = other.tail
        other.clear()

    def clear(self):      # czyszczenie listy
        self.head = self.tail = None
        self.length = 0


# Zastosowanie.
alist = SingleList()
alist.insert_tail(Node(11))         # [11]
alist.insert_tail(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
print(alist)


blist = SingleList()
blist.insert_tail(Node(44))         # [11]
blist.insert_tail(Node(55))         # [22, 11]
blist.insert_tail(Node(66))         # [22, 11, 33]
print(str(blist))

alist.remove_tail()
alist.remove_tail()
alist.remove_tail()
print(str(alist))

alist.merge(blist)
print(str(alist))
