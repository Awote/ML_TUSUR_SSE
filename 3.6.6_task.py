if __name__ == "__main__":
    print("Введите число")
    rez = 1
    for item in input():
        if item == "0":
            continue
        else:
            rez=rez * int(item)
    print(rez)
