import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def checkcol(G):
    global colored
    global color_count
    colored = 1
    for (i,j) in G.edges():
        if G.node[i]['color'] == G.node[j]['color']:
            colored=0
    return colored


def recursion(G,i):
    global colored
    global color_count
    n = len(G.nodes())
    if i<=n:
        for j in range(1,4):
            G.node[i]['color'] = j
            recursion(G,i+1)
            
    if i==n+1:
        if checkcol(G) == 1:
            color_count = color_count + 1
            if color_count == 1:
                print('The graph is 3-colorable. This is one proper 3-coloring of the vertices:')
                for i in G.nodes():
                    print('node', i, ', color:', G.node[i]['color'])


def brute_force(G):
    global colored
    global color_count
    color_count = 0
    colored = 0
    recursion(G,1)
    if color_count == 0:
        print('The graph is not 3-colorable.')

# Clearly a brute force approach is rather poor.

print()
G1=graph1.Graph()
print('Graph G1:')
brute_force(G1)
print()


G2=graph2.Graph()
print('Graph G2:')
brute_force(G2)
print()


G3=graph3.Graph()
print('Graph G3:')
brute_force(G3)
print()


G4=graph4.Graph()
print('Graph G4:')
brute_force(G4)
print()


G5=graph5.Graph()
print('Graph G5:')
brute_force(G5)
print()