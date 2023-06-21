G = [['A', 'B', 5], ['A', 'D', 2], ['A', 'E', 4],
     ['B', 'D', 3], ['B', 'C', 3],
     ['C', 'D', 3], ['C', 'E', 4], ['C', 'F', 2],
     ['D', 'E', 1],
     ['E', 'F', 2]]

parent = [chr(65+i) for i in range(6)]
G.sort(key=lambda x : x[2])

def union(x, y):
    x_parent, y_parent = find(x), find(y)
    parent[ord(x_parent)-65] = y_parent

def find(x):
    if x == parent[ord(x)-65]:
        return x
    parent[ord(x)-65] = find(parent[ord(x)-65])
    return parent[ord(x)-65]

result = 0

for n in G:
    x, y, w = n[0], n[1], n[2]
    if find(x) != find(y):
        union(x, y)
        print(f"{x} <-> {y}  연결")
        result += w
        
print(f"가중치의 합은 {result} 입니다")
