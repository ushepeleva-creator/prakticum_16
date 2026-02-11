N = int(input())
courses = set()

for _ in range(N):
    course = input().split()
    courses.update(course)
print(len(courses))
