class Stack(list):
    def push(self, item):
        self.append(item)

# Example
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.reverse()
print(s)
# s.pop()     # -> 3
# s.pop()     # -> 2
# print(s)
# print(dir(s))