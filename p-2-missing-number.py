def get_missing_number(n, s_n):
    sum_of_cons = ((n)*(n+1))//2
    sum_of_ser = sum(s_n)
    print(sum_of_cons - sum_of_ser)

if __name__ == "__main__":
    n = int(input())
    s_n = [int(x) for x in input().split()]
    get_missing_number(n, s_n)
