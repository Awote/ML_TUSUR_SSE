if __name__ == "__main__":
    input_number = int(input())
    if input_number > 20 and input_number %2 == 0:
        print("Отличное")
    elif input_number>=6 and input_number<= 20 and input_number %2 == 0:
        print("Так себе")
    elif input_number>=2 and input_number <=5 and input_number%2 == 0:
        print("Неплохо")
    elif input_number %2 == 1:
        print("Плохо")
    