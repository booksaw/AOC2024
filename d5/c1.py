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

for book in books:
    if is_valid(book):
        midpointCount += int(book[int(len(book)/2)]) 

print(midpointCount)