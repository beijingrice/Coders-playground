def check():
    first = 0
    second = 1
    third = 2
    winTime = 0
    for x in range(5):
        if li[first] + li[second] + li[third] == 19:
            winTime += 1
            first += 1
            second += 1
            third += 1
    if winTime == 5:
        print("Win!")
        print(li)
        return "BREAK"
for a in range(19):
    for b in range(19):
        for c in range(19):
            for d in range(19):
                for e in range(19):
                    li = [a,9,b,c,d,e,7]
                    result = check()
                    if result == "BREAK":
                        break
