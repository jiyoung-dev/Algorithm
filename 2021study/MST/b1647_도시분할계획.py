# date: 2021/08/11
# problem: https://www.acmicpc.net/problem/1647
# description: 최소 스패닝 트리

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# main
n, m = map(int, input().split())  # 노드수(n), 간선수(m)
parent = [0] * (n+1)  # 부모 테이블 초기화
edges = []  # 간선 저장할 리스트
result = 0  # 최소 비용 초기화

# 간선정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

# 부모를 자기자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 사이클이 발생하지 않는 경우만 집합에 포함
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        # 가장 마지막 비용(최대비용) 저장
        last = c
print(result - last)
