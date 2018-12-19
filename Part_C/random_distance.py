import random as rd
from Part_C import graph6, graph7, graph8, graph9, graph10


def bfs(G, a, b):

    G.add_nodes_from(G.nodes(), label=-1)  # initialization of all labels
    i = 0

    G.node[a]['label'] = i

    while G.node[b]['label'] is -1:

        for node in list(filter(lambda n: G.node[n]['label'] == i, G.nodes())):

            for adj in G.neighbors(node):

                G.node[adj]['label'] = i + 1

        i += 1

    return G.node[b]['label']


def max_distance(G):
    max_dist = 0
    for a in G.nodes():
        for b in G.nodes():
            k = bfs(G, a, b)
            if max_dist < k:
                max_dist = k
    return max_dist


def random_distance(G):
    n = len(G.nodes())
    dists = []

    for x in range(5):

        a = rd.randint(1, n)
        b = a

        while b == a:

            b = rd.randint(1, n)

        dists.append(bfs(G, a, b))

    return max(dists)


print()
G6 = graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
G6 = graph6.Graph()  # we initialize again the attributes of the graph G6
print('I found the distance between two random vertices in G6 to be:', random_distance(G6))
print()


G7 = graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
G7 = graph7.Graph() # we initialize again the attributes of the graph G7
print('I found the distance between two random vertices in G7 to be:', random_distance(G7))
print()


G8 = graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
G8 = graph8.Graph() # we initialize again the attributes of the graph G8
print('I found the distance between two random vertices in G8 to be:', random_distance(G8))
print()


G9 = graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
G9 = graph9.Graph() # we initialize again the attributes of the graph G9
print('I found the distance between two random vertices in G9 to be:', random_distance(G9))
print()


G10 = graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
G10 = graph10.Graph() # we initialize again the attributes of the graph G10
print('I found the distance between two random vertices in G10 to be:', random_distance(G10))
print()
