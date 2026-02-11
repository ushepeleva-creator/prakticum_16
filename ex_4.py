first = set(map(int, input().split()))
second = set(map(int, input().split()))
num = int(input())
intresection = first & second

if num in intresection:
    print("YES")
else:
    print("NO")
