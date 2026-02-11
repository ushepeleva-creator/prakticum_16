sweets = set(input().split())
N = int(input())
friends_likes = set()

for _ in range(N):
    products = set(input().split())
    friends_likes.update(products)
sladkoeska_like = sweets - friends_likes
print(len(sladkoeska_like))
