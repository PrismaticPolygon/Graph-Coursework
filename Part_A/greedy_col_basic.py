from Part_A import graph1, graph2, graph3, graph4, graph5


def find_smallest_color(G, i):

    global kmax

    adjacent = set([G.node[x]['color'] for x in G.neighbors(i)])

    for i in range(1, kmax + 1):

        if i not in adjacent:

            return i

        elif i == kmax:

            kmax += 1

            return kmax


def greedy(G):

    global kmax
    kmax = 1

    for i in G.nodes():

        G.node[i]['color'] = find_smallest_color(G, i)

    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)


print('Graph G1:')
G = graph1.Graph()
greedy(G)


print('Graph G2:')
G = graph2.Graph()
greedy(G)


print('Graph G3:')
G = graph3.Graph()
greedy(G)


print('Graph G4:')
G = graph4.Graph()
greedy(G)


print('Graph G5:')
G = graph5.Graph()
greedy(G)