def print_weird_sequence(n):
    print(n)
    while n != 1:
        if n & 1:
            n *= 3
            n += 1
            print(n)
        else:
            n//= 2
            print(n)




if __name__ == "__main__":
    n = int(input())
    if n < 1:
        print(n)
    else:
        print_weird_sequence(n)
