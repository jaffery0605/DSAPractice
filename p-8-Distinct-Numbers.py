def get_distinct_count(n, n_arr):
    res = []
    for el in n_arr:
        if el not in res:
            res.append(el)
    print(len(res))

if __name__ == "__main__":
    n = int(input())
    n_arr = [int(x) for x in input().split()]
    if n == 1:
        print(1)
    else:
        get_distinct_count(n, n_arr)