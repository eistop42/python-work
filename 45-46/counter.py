class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        self._update_count()

    def decrement(self):
        self.count -= 1

    def _update_count(self):
        if self.count >= 10:
            self.count = 0

c = Counter()
for i in range(20):
    c.increment()
print(c.count)