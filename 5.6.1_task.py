if __name__ == "__main__":
    print("Введите целое число")
    fizz_buzz_number = int(input())

    if (fizz_buzz_number % 3) == 0 and fizz_buzz_number %5 == 0:
        print("Fizz Buzz")
    elif fizz_buzz_number % 3 == 0:
        print("Fizz")
    elif fizz_buzz_number % 5 == 0:
        print("Buzz")
    else:
        print(f'"{fizz_buzz_number}"')
