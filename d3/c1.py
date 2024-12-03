runningTotal = 0

for line in open("d3/input.txt"):
    possibles = line.split("mul(")
    for possible in possibles:
        closing = possible.split(")")
        if len(closing) < 2:
            continue
        
        numbers = closing[0].split(",")
        if len(numbers) != 2:
            continue

        try:
            n1 = int(numbers[0])
            n2 = int(numbers[1])
            if n1 > 999 or n2 > 999 or n1 < 0 or n2 < 0:
                continue 
            print("Valid multiplier: ", closing[0])
            runningTotal += n1 * n2
        except:
            continue 

print(runningTotal)
# 171297687