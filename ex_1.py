numbers = list(map(int, input().split()))
num = int(input())
repiting = set()
seen = set()

for i in numbers:
    if i in seen:
        repiting.add(i)
    else:
        seen.add(i)

if num in repiting:
    print(num)
else:
    print('do not repeat')
