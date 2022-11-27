while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except Exception as ex:
        print(ex)
    finally:
        print("Finally clause")