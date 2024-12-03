runningTotal = 0
inputStr = ""
for line in open("d3/input.txt"):
    inputStr += line

doBlocks = inputStr.split("do()")
for block in doBlocks:
    block = block.split("don't()")[0]
    possibles = block.split("mul(")
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
