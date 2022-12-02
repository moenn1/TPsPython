for i in range(1, 9):
    for j in range(1, 9):
        toPrint = str(i*j)
        if(len(toPrint) == 1):
            print("|" + toPrint + " |", end="")
        else:
            print("|" + toPrint + "|", end="")
    print()