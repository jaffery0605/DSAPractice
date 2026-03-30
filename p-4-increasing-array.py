def get_least_moves(n, arr_list):
    m = 0
    prev = arr_list[0]
    for i in range(1,n):
        if prev > arr_list[i]:
            m += prev - arr_list[i]
        else:
            prev = arr_list[i]
    print(m)
        



if __name__ == "__main__":
    n = int(input())
    arr_list = [int(x) for x in input().split()]
    get_least_moves(n, arr_list)
