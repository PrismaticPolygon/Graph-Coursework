from Part_A import graph1, graph2, graph3, graph4, graph5

colored = 0
color_count = 0
k = 0


def check_col(G):

    global colored, color_count

    colored = 1

    for (i, j) in G.edges():

        if G.node[i]['color'] == G.node[j]['color']:

            colored = 0

    return colored


def recursion(G, i):

    global colored, color_count

    n = len(G.nodes())

    if i <= n:

        for j in range(1, k + 1):

            G.node[i]['color'] = j

            recursion(G, i + 1)

    if i == n + 1:

        if check_col(G) == 1:

            color_count += 1

            if color_count == 1:

                print('The graph is {}-colorable. This is one proper {}-coloring of the vertices:'.format(k, k))

                for i in G.nodes():

                    print('node', i, 'color:', G.node[i]['color'])


def brute_force(G):

    global colored, color_count

    color_count = 0
    colored = 0

    recursion(G, 1)

    if color_count == 0:

        print('The graph is not {}-colorable'.format(k))


k = int(input("\nChoose the number of colors for G1: "))
G1 = graph1.Graph()
print('\nGraph G1:')
brute_force(G1)

k = int(input("\nChoose the number of colors for G2: "))
G2 = graph2.Graph()
print('\nGraph G2:')
brute_force(G2)

k = int(input("\nChoose the number of colors for G3: "))
G3 = graph3.Graph()
print('\nGraph G3:')
brute_force(G3)

k = int(input("\nChoose the number of colors for G4: "))
G4 = graph4.Graph()
print('\nGraph G4:')
brute_force(G4)

k = int(input("\nChoose the number of colors for G5: "))
G5 = graph5.Graph()
print('\nGraph G5:')
brute_force(G5)