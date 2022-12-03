totals = []
with open("input.txt") as f:
    for paragraph in f.read().split("\n\n"):
        totals.append(sum([int(x) for x in paragraph.split("\n")]))
totals = sorted(totals)
print(sum(totals[-3:]))