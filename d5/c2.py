from functools import cmp_to_key

rules = {}
books = []

onBooks = False
for line in open("d5/input.txt"):
    line = line.replace("\n", "")
    if len(line) == 0:
        onBooks = True
    elif onBooks:
        books.append(line.split(","))
    else:
        split = line.split("|")
        if split[0] not in rules:
            rules[split[0]] = [split[1]]
        else:
            rules[split[0]].append(split[1])

midpointCount = 0

def is_valid(book):
    seenPages = []
    valid = True
    for page in book:
        if page in rules:
            for rule in rules[page]:
                if rule in seenPages:
                    valid = False
        seenPages.append(page)
    return valid


def comparator(a, b):
    if a in rules and b in rules[a]:
        return 1
    elif b in rules and a in rules[b]:
        return -1
    else:
        return 0

for book in books:
    if not is_valid(book):
        newBook = sorted(book, key=cmp_to_key(comparator))
        midpointCount += int(newBook[int(len(book)/2)]) 

print(midpointCount)