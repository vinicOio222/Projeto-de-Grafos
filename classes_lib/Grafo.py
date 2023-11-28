import heapq
import operator

class Grafo:
    
    def __init__(self, caminho = str):
        self.listaAdjacencia: dict[str, list[tuple[str, int]]] = {}
        self.LerArquivo(caminho)

    def ExibirGrafo(self):
        for vertice in self.listaAdjacencia.keys():
            print(f"{vertice}: {self.listaAdjacencia[vertice]}")

    def ExibirVertice(self, vertice):
        print(f"{vertice}: {self.listaAdjacencia[vertice]}")
                
    def LerArquivo(self, caminho):
        with open(caminho, "+r") as input:
            linhas = input.readlines()[7:]       # Começa a ler a partir da linha 8
        
        #print("Arestas: ", len(linhas), "\n\n")
        for input in linhas:
            palavras = input.split(" ")     #Splita cada elemento divididos por um " ", e coloca em cada variável, execeto o "a"
            vertice1, vertice2, peso = palavras[1], palavras[2], palavras[3]
            peso = int(peso)
                                                        
            if vertice1 in self.listaAdjacencia.keys():
                self.listaAdjacencia[vertice1].append((vertice2, peso))
            else:
                self.listaAdjacencia.update({vertice1: [(vertice2, peso)]})    
            
            # if vertice2 in self.listaAdjacencia.keys():
            #     self.listaAdjacencia[vertice2].append((vertice1, peso))
            # else:
            #     self.listaAdjacencia.update({vertice2: [(vertice1, peso)]})
            
    def n(self):
        return len(self.listaAdjacencia)
    
    def m(self):    # Está retornando um valor menor do que o numero esperado de arestas
        arestas = set()
        for arestasLista in self.listaAdjacencia.values():
            for i in arestasLista:
                arestas.add(i)
        return len(arestas)
        # for i in self.listaAdjacencia.values():
        #     arestas.add(i)
        # return len(i)
    

    def d(self, vertice):
        grau = len(self.listaAdjacencia[vertice])
        return grau
    
    def w(self, vertice1, vertice2):
        for vertice in self.listaAdjacencia[vertice1]:
            if vertice[0] == vertice2:
                return vertice[1]
            
    def vizinhanca(self, vertice):
        vizinhos = self.listaAdjacencia.get(vertice)
        return vizinhos
    
    def dist(self, vertice):
        vizinhanca = self.vizinhanca(vertice)
        return len(vizinhanca)
    
    def minD(self):
        grauMin = min(self.dist(vertice) for vertice in self.listaAdjacencia.keys())
        return grauMin

    def maxD(self):
        grauMax = max(self.dist(vertice) for vertice in self.listaAdjacencia.keys())
        return grauMax
    
    #def bfs(self, vertice):
        
    # def dfs(self, vertice):
    #     visitados = []
        
    #     while not visitados.empty():
            