class PriorityQueue:
    def __init__(self, maxlen):
        self.queue = [None] * maxlen
        self.maxlen = maxlen
        self.length = 0

    def insert(self, x, p):
        if self.length == self.maxlen:
            raise Exception("Queue Overflow")

        self.queue[self.length] = (x, p)
        i = self.length
        self.length += 1

        # Heapify Up
        while i > 0:
            parent = (i - 1) // 2

            if self.queue[parent][1] <= self.queue[i][1]:
                break

            self.queue[parent], self.queue[i] = self.queue[i], self.queue[parent]
            i = parent

    def pop(self):
        if self.length == 0:
            raise Exception("Queue Empty")

        result = self.queue[0]

        self.length -= 1

        if self.length == 0:
            return result

        self.queue[0] = self.queue[self.length]
        self.queue[self.length] = None

        i = 0

        # Heapify Down
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < self.length and self.queue[left][1] < self.queue[smallest][1]:
                smallest = left

            if right < self.length and self.queue[right][1] < self.queue[smallest][1]:
                smallest = right

            if smallest == i:
                break

            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            i = smallest

        return result

    def empty(self):
        return self.length == 0

    def __len__(self):
        return self.length