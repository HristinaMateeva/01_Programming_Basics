class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterations < self.count:
            current_value = self.iterations * self.step
            self.iterations += 1
            return current_value
        raise StopIteration


# ------------------------------
numbers = take_skip(2, 6)
for number in numbers:
    print(number)
# ------------------------------
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
