print("Введите число")
input_float_number = float(input())

print("{0:.2f}".format(input_float_number))
print(int(round(input_float_number,0)))

len_input = len(str(input_float_number))

if len_input < 11:
    need_zeros = 11 - len_input
    str_input_float_number = "0"*need_zeros + str(input_float_number)
print(str_input_float_number)