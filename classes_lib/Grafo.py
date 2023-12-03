from collections import deque
import heapq as hq
import operator

class Grafo:
    
    
    MAX_TAM = float('inf')
    
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
            # Começa a ler a partir da linha 8
            # linhas = input.readlines()[7:]
            linhas = input.readlines()[1:]
        
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
    
    # Está retornando um valor menor do que o numero esperado de arestas
    def m(self):
        arestas = set()
        for arestasLista in self.listaAdjacencia.values():
            for i in arestasLista:
                arestas.add(i)
        return len(arestas)
    

    def d(self, vertice):
        grau = len(self.listaAdjacencia[vertice])
        return grau
    
    def w(self, vertice1, vertice2):
        for vertice in self.listaAdjacencia[vertice1]:
            if vertice[0] == vertice2:
                return vertice[1]
            
    def vizinhanca(self, vertice):
        # Retorna todos os vizinhos do vertice de entrada sem os pesos das arestas
        vizinhos = [vizinho[0] for vizinho in self.listaAdjacencia[vertice]]
        return vizinhos
    
    def vizinhaca_com_peso(self, vertice):
        # Retorna todos os vizinhos do vertice de entrada junto com o respectivo peso de cada aresta
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
    
    def bfs(self, raiz):
        d = 0
        pi = None
        dict_dist = {}
        dict_ant = {}
        visitados = set()
        fila = deque()
        
        dict_dist[raiz] = 0
        dict_ant[raiz] = None
        fila.append(raiz)
        
        # Continua o processo até a fila ficar vazia
        while fila:
            vertice = fila.popleft()

            visitados.add(vertice)
            d += 1
            pi = vertice
            vizinhos = self.vizinhanca(vertice)
            for i in vizinhos:
                if i not in visitados:
                    dict_dist[i] = d
                    dict_ant = pi
                    fila.append(i)
                
        return dict_dist, dict_ant
            
    def dfs(self, raiz):
        visitados = set()
        cont = 0
        antecessor = None
        dicIni = {}
        dicFim = {}
        fila = deque()
        
        dicpi = {}
        
        fila.append(raiz)
        
        while fila:
            
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                cont += 1
                dicIni[vertice] = cont
                
                dicpi[vertice] = antecessor
                antecessor = vertice
                
                vizinhos = self.vizinhanca(vertice)
                for i in vizinhos:
                    if i not in visitados and i not in fila:
                        fila.append(i)
                        
        visitados = sorted(visitados, reverse = True)
        for vertice in visitados:
            cont += 1
            dicFim[vertice] = cont
            
        return dicIni, dicFim, dicpi
    
    def bf(self, raiz):
        d = {}
        pi = {}
        d  = {vertice : self.MAX_TAM for vertice in self.listaAdjacencia.keys()}
        pi = {vertice : None for vertice in self.listaAdjacencia.keys()}
        
        d[raiz] = 0
        
        for _ in range(self.n() - 1):
            for vertice in self.listaAdjacencia.keys():
                vizinhos = self.vizinhaca_com_peso(vertice)
                for i, peso in vizinhos:
                    if d[i] > d[vertice] + peso:
                        d[i] = d[vertice] + peso
                        pi[i] = vertice
                        
        for vertice in self.listaAdjacencia.keys():
            vizinhos = self.vizinhaca_com_peso(vertice)
            for i, peso in vizinhos:
                if d[i] > d[vertice] + peso:
                    return None, None, "Detectado ciclo negativo"
        
        return d, pi, None
    
    def djikstra(self, raiz):
        d = {}
        pi = {}
        fila = []
        visitados = set()
        
        d = {vertice : self.MAX_TAM for vertice in self.listaAdjacencia.keys()}
        pi = {vertice : None for vertice in self.listaAdjacencia.keys()}
        
        d[raiz] = 0
        
        hq.heappush(fila, raiz)
        
        while fila:
            vertice = hq.heappop(fila)
            if vertice in visitados:
                continue
            
            visitados.add(vertice)
            vizinhos = self.vizinhaca_com_peso(vertice)
            for vizinho, peso in vizinhos:
                if d[vizinho] > d[vertice] + peso:
                    d[vizinho] = d[vertice] + peso
                    pi[vizinho] = vertice
                    hq.heappush(fila, vizinho)
                             
        return d, pi
    
    def caminhoVertice(self, valor, T):
        visitados = set()
        caminho = []
        
        for vertice in self.listaAdjacencia.keys():
            if vertice not in visitados:
                visitados.add(vertice)
                
                pai = T[vertice]
                
                while pai != None:
                    caminho.append(pai)
                    pai = T[pai]
                
                if len(caminho) >= valor:
                    return caminho
                else:
                    caminho.clear()
                    continue
        
        return None
    
    def checarCiclo(self, T):
        
        ciclos = self.caminhoVertice(5, T)
        
        ciclosReversos = ciclos.copy()
        ciclos.reverse()
        
        for vertice in ciclos:
            vizinhos = self.vizinhanca(vertice)
            for vizinho in vizinhos:
                if ciclosReversos[0] == vizinho:
                    index = ciclos.index(vertice)
                    
                    if index >= 5:
                        ciclos = ciclosReversos[0:index]
                        ciclos.append(ciclosReversos[0])
                        return ciclos
        
        return "Não há ciclos com tamanho >= 5"
    
    def verticeMaisDistante(self, raiz):
        d, _ = self.djikstra(raiz)
        
        maior = max(d.items(), key = lambda x: x[1])
        return maior
        