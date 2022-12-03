def tovalue(c):
    if c.isupper():
        return ord(c)-(64-26)
    elif c.islower():
        return ord(c)-96

items = []
with open("input.txt") as f:
    backpacks = f.read().split("\n")
    for i in range(0,len(backpacks),3):
        group = backpacks[i:i+3]
        
        for item in group[0]:
            if item in group[1] and item in group[2]:
                items.append(item)
                break

total = sum([tovalue(c) for c in items])
print(total)