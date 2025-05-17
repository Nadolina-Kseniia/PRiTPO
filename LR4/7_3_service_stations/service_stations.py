# service_stations.py
def min_stations(cities, city_pairs):
    graph = [[] for _ in range(cities + 1)]
    for u, v in city_pairs:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (cities + 1)
    stations = 0

    for town in range(1, cities + 1):
        if not visited[town]:
            stations += 1
            visited[town] = True
            for neighbor in graph[town]:
                visited[neighbor] = True

    return stations


def main():
    import sys
    for line in sys.stdin:
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        edges = []
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))

        print(min_stations(n, edges))


if __name__ == "__main__":
    main()