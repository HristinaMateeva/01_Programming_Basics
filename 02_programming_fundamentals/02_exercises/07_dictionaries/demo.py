#Change the value
a = {'a': 'A', 'b': 'B'}

value = a['b']
a.pop('b')
a['c'] = value
print(a)
