def get_minimum_gandolas(n, w, n_arr):
    n_arr.sort()
    l,h = 0, n-1
    g = 0
    while l <= h:
        if n_arr[l] + n_arr[h] <= w:
            l += 1
        h -= 1
        g += 1
    print(g)
    
        


if __name__ == "__main__":
    n, w = [int(x) for x in input().split()]
    n_arr = [int(y) for y in input().split()]
    get_minimum_gandolas(n, w, n_arr)