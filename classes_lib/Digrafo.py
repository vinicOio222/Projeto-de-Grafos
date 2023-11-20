import heapq as hq
from collections import defaultdict, deque

class Digrafo:
    """
        Classe do objeto Digrafo (grafo direcionado) e seus métodos.

        Parâmetros:
        - caminhoInput (str): O caminho do arquivo de entrada.

    """
    MAX_TAM = float('inf')

    def __init__(self, caminhoInput = str):
        self.listaAdjacencia = defaultdict(lambda: {"positivo":[], "negativo": []})
        self.lerInput(caminhoInput)

    def addAresta(self, x, y, peso, tipo = "positivo"):
        """
        Adiciona uma aresta ao digrafo.

        Parâmetros:
        - x (str): O vértice de origem da aresta.
        - y (str): O vértice de destino da aresta.
        - peso (int): O peso da aresta.
        - tipo (str): O tipo da aresta. Pode ser "positivo" ou "negativo". O padrão é "positivo".

        """
        if tipo not in ["positivo", "negativo"]:
            raise Exception("Tipo de aresta inválido! Use 'positivo' ou 'negativo'.")
        self.listaAdjacencia[x][tipo].append((y, peso))

    def vizinhanca(self, vertice):
        """
        Retorna a vizinhança de um vértice.

        Parâmetros:
        - vertice (str): O vértice de interesse.

        Retorna:
        - positivos (list): Lista de vizinhos positivos do vértice.
        - negativos (list): Lista de vizinhos negativos do vértice.

        """
        positivos = self.listaAdjacencia.get(vertice, {}).get("positivo", [])
        negativos = self.listaAdjacencia.get(vertice, {}).get("negativo", [])
        return positivos, negativos

    def mostrarGrafo(self):
        """
        Mostra o grafo na forma de uma lista de adjacência.

        -> Exemplo de Saída:

        Vértice v1:
        - "Positivos": {(vizinho1, peso1), (vizinho2, peso2), (vizinho3, peso3), ... }
        - "Negativos": {(vizinho1, peso1), (vizinho2, peso2), (vizinho3, peso3), ... }

        """
        for vertice, a in self.listaAdjacencia.items():
            positivos, negativos = self.vizinhanca(vertice)
            print(f"Vértice {vertice}:\nPositivos: {list(positivos)}\nNegativos: {list(negativos)}\n")

    def n (self):
        """
        Retorna o número de vértices do digrafo.

        Retorna:
        - n (int): O número de vértices do digrafo.

        """
        return len(self.listaAdjacencia)

    def m (self):
        """
        Retorna o número de arestas do digrafo.

        Retorna:
        - m (int): O número de arestas do digrafo.

        """
        return sum([len(vizinhos["positivo"]) + len(vizinhos["negativo"]) for vizinhos in self.listaAdjacencia.values()]) // 2

    def minD(self):
        """
        Retorna o menor grau de um vértice do digrafo.

        Retorna:
        - minD (int): O menor grau de um vértice do digrafo.

        """
        return min(self.dist(vert) for vert in self.listaAdjacencia.keys())

    def maxD(self):
        """
        Retorna o maior grau de um vértice do digrafo.

        Retorna:
        - maxD (int): O maior grau de um vértice do digrafo.

        """
        return max(self.dist(vert) for vert in self.listaAdjacencia.keys())

    def dist(self, vertice):
        """
        Retorna a distância de um vértice para seus vizinhos.

        Parâmetros:
        - vertice (str): O vértice de interesse.

        Retorna:
        - dist (int): A distância do vértice para seus vizinhos.

        """
        vizinhancaPositiva, vizinhancaNegativa = self.vizinhanca(vertice)
        return len(vizinhancaPositiva) + len(vizinhancaNegativa)

    def bfs(self, vertice):
        """
        Realiza uma busca em largura a partir de um vértice.

        Parâmetros:
        - vertice (str): O vértice de partida da busca.

        Retorna:
        - dict_dist (dict): Um dicionário contendo as distâncias de cada vértice em relação ao vértice de partida.
        - dict_ant (dict): Um dicionário contendo os antecessores de cada vértice na busca.

        """
        d , pi  = 0, None
        dict_dist, dict_ant = {}, {}
        visitados, Q = set(), deque()

        dict_dist[vertice] = 0
        dict_ant[vertice ] = None
        Q.append(vertice)

        while Q:
            vert = Q.popleft()
            if vert in visitados:
                continue

            visitados.add(vert)
            d += 1
            pi = vert

            vizinhos, _ = self.vizinhanca(vert)
            for i, _ in vizinhos:
                if i in visitados or i in Q:
                    continue

                dict_dist[i] = d
                dict_ant[i] = pi
                Q.append(i)
        return dict_dist, dict_ant

    def dfs(self, vertice):
        """
        Realiza uma busca em profundidade a partir de um vértice.

        Parâmetros:
        - vertice (str): O vértice de partida da busca.

        Retorna:
        - dicAux1 (dict): Um dicionário contendo os tempos de descoberta de cada vértice.
        - dicAux2 (dict): Um dicionário contendo os tempos de finalização de cada vértice.
        - ant (dict): Um dicionário contendo os antecessores de cada vértice na busca.

        """
        visitados, temp, antecessor = set(), 0, None
        dicAux1, dicAux2, ant, Q = {}, {}, {}, deque()
        Q.append(vertice)
        while Q:
            vert  = Q.popleft()
            if vert not in visitados:
                visitados.add(vert)
                temp += 1
                dicAux1[vert] = temp
                ant[vert] = antecessor
                antecessor = vert

                vizinhos =  self.vizinhanca(vert)
                for i, _ in vizinhos[0]:
                    if i not in visitados and i not in Q:
                        Q.append(i)

        visitados= sorted(visitados, reverse = True)
        for vert in visitados:
            temp += 1
            dicAux2[vert] = temp

        return dicAux1, dicAux2, ant

    def bf(self, vertice):
        """
        Realiza o algoritmo de Bellman-Ford a partir de um vértice.

        Parâmetros:
        - vertice (str): O vértice de partida do algoritmo.

        Retorna:
        - d (dict): Um dicionário contendo as distâncias mínimas de cada vértice em relação ao vértice de partida.
        - pi (dict): Um dicionário contendo os predecessores de cada vértice no caminho mínimo.
        - ciclo (str): Uma mensagem indicando se foi detectado um ciclo negativo.

        """
        d, pi = {}, {}
        d  = {vert : self.MAX_TAM for vert in self.listaAdjacencia.keys()}
        pi = {vert : None for vert in self.listaAdjacencia.keys()}

        d[vertice] = 0

        for _ in range(self.n() - 1):
            for vert in self.listaAdjacencia.keys():
                vizinhos, _ = self.vizinhanca(vert)
                for i, peso in vizinhos:
                    if d[i] > d[vert] + peso:
                        d[i] = d[vert] + peso
                        pi[i] = vert

        for vert in self.listaAdjacencia.keys():
            vizinhos, _ = self.vizinhanca(vert)
            for i, peso in vizinhos:
                if d[i] > d[vert] + peso:
                    return None, None, "Detectado ciclo negativo"

        return d, pi, None

    def djikstra(self, vertice):
        """
        Realiza o algoritmo de Dijkstra a partir de um vértice.

        Parâmetros:
        - vertice (str): O vértice de partida do algoritmo.

        """

        d, pi, Q, visitados = {}, {}, [], set()
        d = {vert : self.MAX_TAM for vert in self.listaAdjacencia.keys()}
        pi = {vert : None for vert in self.listaAdjacencia.keys()}

        d[vertice] = 0
        hq.heappush(Q, vertice)
        while Q:
            vert = hq.heappop(Q)
            if vert in visitados:
                continue
            visitados.add(vert)

            vizinhos, _ = self.vizinhanca(vert)
            for vizinho, peso in vizinhos:
                if d[vizinho] > d[vert] + peso:
                    d[vizinho] = d[vert] + peso
                    pi[vizinho] = vert
                    hq.heappush(Q, vizinho)

        return d, pi

    def lerInput(self, caminhoInput):
        """
        Lê o arquivo de entrada e adiciona as arestas ao digrafo.

        Parâmetros:
        - caminhoInput (str): O caminho do arquivo de entrada.

        """
        try:
            with open(caminhoInput, 'r') as arquivo:
                for linha in arquivo.readlines():
                    palavras = linha.split(" ")
                    if not palavras:
                        continue
                    if palavras[0] == 'c':
                        continue
                    if palavras[0] == 'p':
                        continue
                    if palavras[0] == 'a':
                        x, y, p =  palavras[1], palavras[2], palavras[3]
                        p = int(p)
                        self.addAresta(x, y, p)
                        self.addAresta(y, x, p, tipo = "negativo")

        except FileNotFoundError:
            print("Arquivo não encontrado!")
        except Exception as e:
            print("Erro na leitura do arquivo: ", e)


digrafo = Digrafo("_input//Teste-graph.txt")
print(digrafo.mostrarGrafo())
vertice = '4'
d_bfs, antecessor_bfs = digrafo.bfs(vertice)
d_dfs1, d_dfs2, antecessor_dfs = digrafo.dfs(vertice)
print("BFS: ", d_bfs, antecessor_bfs)
print("DFS: ", d_dfs1, d_dfs2, antecessor_dfs)
# print(digrafo.maxD())
d_djikstra, antecessor_djikstra = digrafo.djikstra(vertice)
print("Djikstra: ", d_djikstra, antecessor_djikstra)
print(f"Número de vértices: {digrafo.n()}")
print(f"Número de arestas: {digrafo.m()}")

# print(digrafo.bf(vertice))
