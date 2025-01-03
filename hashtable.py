# Hash Data Structure and Hash collisions


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]




# print(get_hash("march 9"))

t = HashTable()
t['march 11'] = 100
t['march 20'] = 160
t['march 17'] = 10


del t['march 11']
print(t.arr)
# print(t.get_hash("march 20"))

# Hash collisions
