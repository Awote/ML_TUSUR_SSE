if __name__ == "__main__":
    counter = 0
    print("Введите строку")
    for item in input().split():
        
        if not item.isdigit():
            counter += 1
        else:
            counter = 0
    print(True) if counter >=3 else print(False)