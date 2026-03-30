def get_beautiful_permutation(n):
    e_arr = []
    o_arr = []
    for i in range(1, n+1):
        if i % 2:
            o_arr.append(i)
        else:
            e_arr.append(i)
    if e_arr[-1] - o_arr[0] == 1:
        print("NO SOLUTION")
    else:
        e_arr.extend(o_arr)
        print(e_arr)


if __name__ == "__main__":
    n = int(input())
    get_beautiful_permutation(n)