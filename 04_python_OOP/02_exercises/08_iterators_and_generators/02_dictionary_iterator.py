class dictionary_iter:
    def __init__(self, dict_obj):
        self.items = list(dict_obj.items())
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations < len(self.items):
            value = self.items[self.iterations]
            self.iterations += 1
            return value
        raise StopIteration


# ------------------------------
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
# ------------------------------
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
