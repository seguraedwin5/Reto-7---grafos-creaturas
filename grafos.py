from re import U
from turtle import color
import networkx as nx
import matplotlib.pyplot as plt
import csv
import pprint
import pandas as pd


def CrearGrafo():
    G = nx.Graph()
    with open("archivocreaturas.csv") as csv_file:
        lector = csv.reader(csv_file,delimiter=",")
        for linea in lector:
            

            for num in range(0,len(linea)):
                if num  != 1:
                    G.add_node(linea[num])
                if num > 1:
                    color = ''
                    if linea[1] == 'Enemigo':
                        color = '#EB2135' #color Rojo
                    elif linea[1] == 'Amigo':
                        color = '#00A354' #Color verde
                    else:
                        color = '#13AAD4' #color Azul
                    G.add_edge(linea[0],linea[num], tipo = linea[1], coloredge = color)
    return G

def mostrarGrafo(grafo):
    pos = nx.circular_layout(grafo)
    _edges = grafo.edges()
    colores = [grafo[u][v]["coloredge"] for u,v in _edges]
    tipos = [grafo[u][v]["tipo"] for u,v in _edges]
    nodes = nx.draw_networkx_nodes(grafo,pos,node_color ='#E7E06B',node_size=250)
    nodes.set_edgecolor('#02D4AB')
    nx.draw_networkx_edges(grafo,pos,edge_color=colores,alpha=0.5)
    nx.draw_networkx_labels(grafo,pos,verticalalignment="baseline",font_color="black")
    #nx.draw(grafo, pos, with_labels= True, font_color ="black", font_weight="bold", edge_color=colores, node_color="#0CE6F8", node_size =800 )
    plt.show()
    
    #pprint.pprint(G.edges().data())
def rutamascorta(grafo,creatura1,creatura2):
    print(nx.dijkstra_path(grafo,creatura1,creatura2))
def verNodosConectados(grafo,creatura):
    #imprime todos los nodos conectados
    print(grafo.edges(creatura))

def listarNodosimportantes(grafo):
    #diccionario centralidad
    dicc = nx.closeness_centrality(grafo)
    df = pd.DataFrame.from_dict({
        "nodo" :list(dicc.keys()),
        "centralidad": list(dicc.values())
    })
    dfordenado =df.sort_values('centralidad', ascending=False)
    print(dfordenado.head(5))
    
    