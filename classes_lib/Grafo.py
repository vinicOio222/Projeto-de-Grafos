import heapq
import operator

class Grafo:
    
    def __init__(self, caminho = str):
        self.listaAdjacencia: dict[str, list[tuple[str, int]]] = {}
        self.LerArquivo(caminho)

    def ExibirGrafo(self):
        for vertice in self.listaAdjacencia.keys():
            print(f"{vertice}: {self.listaAdjacencia[vertice]}")
                
    def LerArquivo(self, caminho):
        with open(caminho, "+r") as input:
            linhas = input.readlines()[7:]       # Começa a ler a partir da linha 8
        
        for input in linhas:
            palavras = input.split(" ")     #Splita cada elemento divididos por um " ", e coloca em cada variável, execeto o "a"
            vertice1, vertice2, peso = palavras[1], palavras[2], palavras[3]
            peso = int(peso)
                                                        
            if vertice1 in self.listaAdjacencia.keys():
                self.listaAdjacencia[vertice1].append((vertice2, peso))
            else:
                self.listaAdjacencia.update({vertice1: [(vertice2, peso)]})    
            
            if vertice2 in self.listaAdjacencia.keys():
                self.listaAdjacencia[vertice2].append((vertice1, peso))
            else:
                self.listaAdjacencia.update({vertice2: [(vertice1, peso)]})
            
    def n(self):
        return len(self.listaAdjacencia)
    
    def m(self):
        arestas = set()
        for arestasLista in self.listaAdjacencia.values():
            for i in arestasLista:
                arestas.add(i)
        return len(arestas)
    
    def vizinhanca(self, vertice):
        vizinhos = self.listaAdjacencia.get(vertice, {})
        return vizinhos

        