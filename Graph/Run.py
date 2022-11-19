from TopologiIndex import TopologiIndex
from Graph import Graph
import networkx as nx
import matplotlib.pyplot as m


class Run:
    def __init__(self) -> None:
        pass

    def run(self, ring, graf, topologi):
        doc = open(f'{ring}_{graf}_{topologi}.txt','w')
        G = Graph(ring, graf)
        if len(topologi) != 0:
            T = TopologiIndex(G)
            listTopologi = [
                'narumi katayama',
                'first multiplicative zagreb',
                'second multiplicative zagreb',
                'second multiplicative zagreb coindex'
            ]
            ti = ''
            if isinstance(topologi, list):
                for i in topologi:
                    if i in listTopologi:
                        ti += f'\t{i}: {T.run(i)}\n'
                    else:
                        ti += 'topologi tidak ada'
            else:
                ti += f'{topologi}: {T.run(topologi)}'
        txt = ''
        txt += f'ring: {ring}\n\tV: {G.vertecies()}\n\tE: {G.edges()}\n\tnot edge: {G.notEdges()}\n\tdeg of V: {G.seqDegree("vertex")}\n\tdeg of E: {G.seqDegree("edge")}\n\tdeg of non-E: {G.seqDegree("not edge")}\n\tStuktur graf{G.structurGraph()}'
        if len(topologi) != 0:
            txt += f'\nTopologi Index: \n{ti}'
        doc.write(txt)
    
        h = nx.Graph()
        h.add_nodes_from(G.vertecies())
        h.add_edges_from(list(map(lambda x: tuple(x), G.edges())))
        options = {
            "font_size": 12,
            "node_size": 300,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 2,
            "width": 5,
        }
        m.title(f'graf {graf}({ring})')
        nx.draw_shell(h,**{'with_labels' : True})
        m.show()

prime = [3,5,7,11,13,17]
for i in list(map(lambda x: x*x,prime)):
    Run().run(f'Z_{i}','nilpotent','')