import time

import networkx as nx


def main():
    with open("input/23_1.txt", "r") as f:
        lines = f.read().splitlines()

    start_time = time.perf_counter()

    edges = [(line.split("-")[0], line.split("-")[1]) for line in lines]

    graph = nx.Graph()
    graph.add_edges_from(edges)

    # Enumerate all cliques, and filter for size 3
    triangles = []
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) == 3 and any(n.startswith("t") for n in clique):
            triangles.append(clique)

    print(f"Unique triangles   : {len(triangles)}")

    elapsed = time.perf_counter() - start_time

    print(f"Time elapsed       : {elapsed:.3f} s")


if __name__ == "__main__":
    main()
