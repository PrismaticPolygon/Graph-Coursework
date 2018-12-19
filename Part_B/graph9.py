import networkx as nx

def Graph():
    G = nx.Graph()

    G.add_edges_from([(1, 2), (1, 5), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (4, 9), (4, 5), (5, 10), (6, 9), (6, 8), (7, 9), (7, 10), (8, 10)])

    n = len(G.nodes())

    for (i,j) in G.edges():
        G.add_edge(n+i,n+j)

    for i in range(1,n+1):
        for j in range(n+1,2*n+1):
            G.add_edge(i,j)


    G.add_nodes_from(G.nodes(), color='never coloured')
    G.add_nodes_from(G.nodes(), label = -1)
    G.add_nodes_from(G.nodes(), visited = 'no')

    return G

