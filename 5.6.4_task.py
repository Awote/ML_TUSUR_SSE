if __name__=="__main__":
    print("Введите текст")
    print("".join([item for item in input() if item.isupper()]))