sublists = input().split("|")

while sublists:
    sublist = sublists.pop().split()
    if sublist:
        print(' '.join(sublist), end=" ")
