import sys
input = sys.stdin.readline
output = sys.stdout.write # must be string
 
 
def get_distinct_count():
    n = int(input())
    arr = sorted(int(x) for x in input().split())
    ans = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            ans += 1
 
    output(f"{ans}")
 

get_distinct_count()