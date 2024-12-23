from collections import defaultdict, deque

connections = [x.strip('\n').split('-') for x in open('day_twentythree_in.txt').readlines()]

graph = defaultdict(set)
for n1, n2 in connections:
    graph[n1].add(n2)
    graph[n2].add(n1)

out = 0
cliques = set()
seen = set()
for k, vs in graph.items():
    if k.startswith('t'):
        for second in vs:
            thirds = graph[second] & vs
            for third in thirds:
                if tuple(sorted([k,second,third])) not in cliques:
                    cliques.add(tuple(sorted([k,second,third])))
                    out += 1
print(out)

def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph
        )
        X.add(v)

graph = {key: set(graph[key]) for key in graph}
all_cliques = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))
print(','.join(sorted(max(all_cliques, key=len))))