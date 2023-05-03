class stack(object):

    def __init__(self):
        self.item=[]

    def push(self, item = ''):
        self.item.append(item)
        pass

    def pop(self):
        self.item.pop()
        pass

    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

    def isempty(self):
        if self.item==[]:
            return True
        else:
             return False

obj = stack()
obj.push("1")
obj.push("2")
print(obj.size())
print(obj.peek())