def tovalue(c):
    if c.isupper():
        return ord(c)-(64-26)
    elif c.islower():
        return ord(c)-96

similar = []
with open("input.txt") as f:
    for backpack in f.read().split("\n"):
        first = backpack[:len(backpack)//2]
        seccond = backpack[len(backpack)//2:]

        for c in first:
            if c in seccond:
                similar.append(c)
                break

total = sum([tovalue(c) for c in similar])
print(total)
