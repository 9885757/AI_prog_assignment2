from collections import deque

visited = [[0]*5 for _ in range(5)]

def bfs(jug1, jug2, target):
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        print("State", (x,y))

        if x == target or y == target:
            print("Goal Reached")
            return

        states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (x - min(x, jug2-y), y + min(x, jug2-y)),
            (x + min(y, jug1-x), y - min(y, jug1-x))
        ]

        for a, b in states:
            if 0 <= a <= jug1 and 0 <= b <= jug2 and not visited[a][b]:
                visited[a][b] = 1
                q.append((a,b))

bfs(4,3,2)