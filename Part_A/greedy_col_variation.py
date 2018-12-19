from Part_A import graph1, graph2, graph3, graph4, graph5


def find_next_vertex(G):

    global visitation_counter
    visitation_counter += 1

    for i in G.nodes():

        adjacent = set([G.node[x]['visited'] for x in G.neighbors(i)])

        if G.node[i]['visited'] == 'no' and adjacent != {"no"}:

            G.node[i]['visited'] = 'yes'

            return i

    G.node[1]['visited'] = 'yes'

    return 1


def find_smallest_color(G,i):

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
    global visitation_counter
    kmax = 1
    visitation_counter = 0

    while visitation_counter < len(G.nodes()):

        i = find_next_vertex(G)

        color = find_smallest_color(G, i)

        G.node[i]['color'] = color

    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()


print('Graph G1:')
G = graph1.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)


print('Graph G2:')
G = graph2.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)


print('Graph G3:')
G = graph3.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)


print('Graph G4:')
G = graph4.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)


print('Graph G5:')
G = graph5.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)