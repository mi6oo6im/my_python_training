elements = []
rows = int(input())
for _ in range(rows):
    elements.extend(input().split())

elements_set = set(elements)
print(*elements_set, sep='\n')