class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)


    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) < self.limit:
            return False
        else:
            return True

    def search(self, target):
        for index, item in enumerate(self.items):
            value = index + 1
            if item == target:
                return len(self.items) - value 
        return -1 


