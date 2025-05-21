def greet_user(name: str) -> str:
    if not name:
        return "Xin chào, bạn!"
    return f"Xin chào, {name}!"

def calculate_sum(a: int, b: int) -> int:
    return a + b

def main():
    name = input("Nhập tên của bạn: ")
    print(greet_user(name))

    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    result = calculate_sum(a, b)
    print(f"Tổng của {a} và {b} là: {result}")

if __name__ == "__main__":
    main()
