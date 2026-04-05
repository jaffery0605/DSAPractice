
def get_elgible_count(m_arr, k_arr, n, m, k):
    m_arr.sort()
    k_arr.sort()
    c = 0

    while n > 0 and m > 0:
        a = m_arr[n-1]
        b = k_arr[m-1]

        if abs(a - b) <= k:
            c += 1
            n -= 1
            m -= 1
        elif a > b + k:
            n -= 1
        else:
            m -= 1

    print(c)
            

if __name__ == "__main__":
    n,m,k = [int(x) for x in input().split()]
    m_arr = [int(y) for y in input().split()]
    k_arr = [int(z) for z in input().split()]
    get_elgible_count(m_arr, k_arr, n, m, k )
    