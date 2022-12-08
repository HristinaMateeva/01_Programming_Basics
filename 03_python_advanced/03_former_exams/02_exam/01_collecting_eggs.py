eggs = list(map(int, input().split(", ")))
papers = list(map(int, input().split(", ")))
boxes = 0

eggs.reverse()

while eggs and papers:
    current_egg = eggs.pop()

    if current_egg <= 0:
        continue

    if current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_paper = papers.pop()

    if current_egg + current_paper <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    eggs.reverse()
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")
