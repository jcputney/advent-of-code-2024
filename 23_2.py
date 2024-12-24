import time

import networkx as nx


def main():
    with open("input/23_2.txt", "r") as f:
        lines = f.read().splitlines()

    start_time = time.perf_counter()

    edges = [(line.split("-")[0], line.split("-")[1]) for line in lines]

    graph = nx.Graph()
    graph.add_edges_from(edges)

    # Reverse the cliques and get the largest one
    sorted_clique = sorted(list(nx.enumerate_all_cliques(graph))[::-1][0])

    print(f"Password           : {','.join(sorted_clique)}")

    elapsed = time.perf_counter() - start_time

    print(f"Time elapsed       : {elapsed:.3f} s")


if __name__ == "__main__":
    main()
