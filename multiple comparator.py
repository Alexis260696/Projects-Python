def main():
    print("multiples comparator")
    a = int(input("write a number: "))
    b = int(input("write oter number: "))

    if a >= b and a % b != 0:
        print(f"{a} is not a multiple of {b}")
    elif a >= b and a % b == 0:
        print(f"{a} is a multiple of {b}")
    elif a < b and b % a != 0:
        print(f"{b} is not a multiple of {a}")
    else:
        print(f"{b} is a multiple of {a}")


if __name__ == "__main__":
    main()