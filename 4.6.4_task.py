invers = ""
input_number = input()

for item in reversed(input_number):
    if item == "-":
        invers = item + invers
    else:
        invers+=item
print(invers)