def get_number_from_spiral(x,y):
    if y >= x:
        if y%2:
            print(y**2-(x-1))
        else:
            print((y-1)**2+x)
    else:
        if x%2:
            print((x-1)**2+y)
        else:
            print(x**2-(y-1))



if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append([int(j) for j in input().split()])
        
    for i in range(n):
        get_number_from_spiral(arr[i][0],arr[i][1])