print("Введите int число")
input_number = int(input())

if len(bin(input_number))-2 > 32:
    print(0)
else:
    invers = ""
    for item in reversed(str(input_number)):
        if item == "-":
            invers = item + invers
        else:
            invers+=item
    print(invers)