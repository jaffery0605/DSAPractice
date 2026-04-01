def get_number_of_placements(n):
    for i in range(1, n+1):
        c = i * i
        if n == 1:
            print(0)
        else:
            total = (c * (c-1))//2
            s = (i-2)*(i-1)*2*2
            print(total-s)


if __name__ == "__main__":
    n = int(input())
    
    get_number_of_placements(n)