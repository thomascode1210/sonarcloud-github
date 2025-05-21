def calculate_area(length, width):
    area = length * width
    return area

def unused_function():
    # This function is never used
    pass

def main():
    length = 10
    width = 5
    area = calculate_area(length, width)
    print("Area is:", area)

    # Hardcoded password (bad practice - SonarCloud sẽ cảnh báo)
    password = "123456"

    # Duplicate code example
    a = 2 + 3
    b = 2 + 3

if __name__ == "__main__":
    main()
