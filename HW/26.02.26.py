class SmartString:
    def __init__(self, text):
        self.text = str(text)
    def __len__(self):
        u = set()
        for ch in self.text:
            u.add(ch)
        return len(u)
    def __str__(self):
        u = set()
        for ch in self.text:
            u.add(ch)
        return self.text + " (" + str(len(self.text)) + ", " + str(len(u)) + ")"
    def __add__(self, other):
        if isinstance(other, SmartString):
            new_text = self.text + other.text
        else:
            new_text = self.text + str(other)
        return SmartString(new_text)

class MyDeque:
    def __init__(self):
        self.__data = []
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return "Deque(" + str(self.data) + ")"

    def append(self, x):
        self.__data.append(x)
    def appendleft(self, x):
        self.__data.insert(0, x)
    def pop(self):
        return self.data.pop()
    def popleft(self):
        return self.data.pop(0)


# пример
if __name__ == "__main__":
    s1 = SmartString("abac")
    s2 = SmartString("zz")
    print(str(s1))      # abac 4 3
    print(len(s1))      # 3
    s3 = s1 + s2    
    print(str(s3))      # abaczz 6 4
    s4 = s1 + "!!!"
    print(str(s4))      # abac!!! 7 4
    d = MyDeque()
    d.append(1)
    d.append(2)
    d.appendleft(0)
    print(d)            # Deque0 1 2
    print(len(d))       # 3
    print(d.pop())      # 2
    print(d.popleft())  # 0
    print(d)            # Deque1
