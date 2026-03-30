def get_longest_repited_char(n):
    if len(n) == 1:
        print(1)
        return
    current_max = 1
    i = 0
    j = 1
    while j != len(n):
        if n[i] == n[j]:
            current_max = max(current_max, j-i+1)
        else:
            i = j
        j+=1
    print(current_max)

if __name__ == "__main__":
    n = input()
    get_longest_repited_char(n)
