# Biblioteca de fila de prioridades
import heapq as hq

# Biblioteca de dicionários com valores padrão
from collections import defaultdict, deque

class Grafo:
    """
    Classe da estrutura de dados Grafo e seus métodos.

    Parâmetros:
    - caminhoInput (str): O caminho do arquivo de entrada.

    Atributos:
    - listaAdjacencia (defaultdict): Dicionário que armazena a lista de adjacência do grafo.

    """
    MAX_TAM = float('inf')

    """- MAX_TAM (float): Valor máximo para representar a distância inicial infinita."""


    def __init__(self, caminhoInput=str):

        self.listaAdjacencia = defaultdict(list)
        self.lerInput(caminhoInput)

    def addAresta(self, x, y, peso):
        """
        Adiciona uma aresta ao grafo.

        Parâmetros:
           -  x (str): O vértice de origem da aresta.
           -  y (str): O vértice de destino da aresta.
           -  peso (int): O peso da aresta.

        """
        self.listaAdjacencia[x].append((y, peso))

    def vizinhanca(self, vertice):
        """
        Retorna a vizinhança de um vértice.

        Parâmetros:
            - vertice (str): O vértice de interesse.

        Retorna:
            - list: Uma lista contendo os vizinhos do vértice.
        """
        #vizinhança de um vértice
        return self.listaAdjacencia.get(vertice)

    def mostrarGrafo(self):
        """
        Mostra o grafo na forma de uma lista de adjacência.

        -> Exemplo de Saída:

        - Vértice v1: {(vizinho1, peso1), (vizinho2, peso2), (vizinho3, peso3), ... }
        - Vértice v2: {(vizinho1, peso1), (vizinho2, peso2), (vizinho3, peso3), ... }

        """
        for vertice, vizinhos in self.listaAdjacencia.items():
            print(f"Vértice {vertice}: {vizinhos}")

    def n(self):
        """
        Retorna o número de vértices do grafo.

        Returns:
            - n (int): O número de vértices do grafo.
        """
        return len(self.listaAdjacencia)

    def m(self):
        """
        Retorna o número de arestas do grafo.

        Retorna:
            - m (int) : O número de arestas do grafo.
        """
        return sum(len(vizinhos) for vizinhos in self.listaAdjacencia.values()) // 2

    def w(self, vertice1, vertice2):
        """
        Retorna o peso da aresta entre dois vértices.

        Parametros:
            - vertice1 (str): O vértice de origem da aresta.
            - vertice2 (str): O vértice de destino da aresta.

        Retorna:
            - peso (int): O peso da aresta.
        """
        for vizinho, peso in self.vizinhanca(vertice1):
            if vizinho == vertice2:
                return peso
        return None

    def minD(self):
        """
        Retorna o menor grau de um vértice do grafo.

        Retorna:
           - minD (int): O menor grau de um vértice do grafo.
        """
        return min(self.dist(vert) for vert in self.listaAdjacencia.keys())

    def maxD(self):
        """
        Retorna o maior grau entre dois vértices do grafo.

        Retorna:
           - maxD (int): O maior grau de um vértice do grafo.
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
        return len(self.vizinhanca(vertice))

    def bfs(self, vertice):
        """
        Realiza uma busca em largura a partir de um vértice.

        Parâmetros:
        - vertice (str): O vértice de partida da busca.

        Retorna:
        - dict_dist (dict): Um dicionário contendo as distâncias de cada vértice em relação ao vértice de partida.
        - dict_ant (dict): Um dicionário contendo os antecessores de cada vértice na busca.

        """
        #Inicializa os atributos da distância e do antecessor
        d, pi = 0, None
        dict_dist, dict_ant = {}, {}
        #Inicializa os vértices visitados e a fila
        visitados, Q = set(), deque()
        #Adiciona o vértice de partida na fila e instancia sua distância como 0 e seu antecessor como None
        dict_dist[vertice] = 0
        dict_ant[vertice] = None
        Q.append(vertice)
        #Enquanto a fila não estiver vazia, o algoritmo continua
        while Q:
            vert = Q.popleft()
            if vert in visitados:
                continue
            # Se o vértice não estiver na lista de visitados, ele é adicionado
            #    e a distância é incrementada e o antecessor é atualizado
            visitados.add(vert)
            d += 1
            pi = vert
            #Para cada vizinho do vértice, se ele estiver na lista de visitados ou na fila, ele é ignorado
            for vizinho, _ in self.vizinhanca(vert):
                if vizinho in visitados or vizinho in Q:
                    continue
                #Se o vizinho não estiver na lista de visitados ou na fila, ele é adicionado
                dict_dist[vizinho] = d
                dict_ant[vizinho] = pi
                Q.append(vizinho)

        return dict_dist, dict_ant

    def dfs(self, vertice):
        """
        Realiza uma busca em profundidade a partir de um vértice.

        Parâmetros:
        - vertice (str): O vértice de partida da busca.

        Retorna:
        - dicIni (dict): Um dicionário contendo os tempos de descoberta de cada vértice.
        - dicFim (dict): Um dicionário contendo os tempos de finalização de cada vértice.
        - dicpi (dict): Um dicionário contendo os antecessores de cada vértice na busca.

        """
        #Inicializa os atributos da descoberta, finalização e antecessor
        #   e instancia sua descoberta como 0 e seu antecessor como None
        visitados, cont, antecessor = set(), 0, None
        dicIni, dicFim, dicpi, Q = {}, {}, {}, deque()
        #Adiciona o vértice de partida na fila
        Q.append(vertice)
        #Enquanto a fila não estiver vazia, o algoritmo continua
        while Q:
            #Remove o primeiro vértice da fila para o próximo seja explorado
            vert = Q.popleft()
            if vert not in visitados:
                #Se o vértice não estiver na lista de visitados, ele é adicionado
                visitados.add(vert)
                #A variável contadora é incrementada e os tempos de descoberta e finalização são atualizados
                cont += 1
                dicIni[vert] = cont
                dicpi[vert] = antecessor
                antecessor = vert
                #Para cada vizinho do vértice, se ele não estiver na lista de visitados ou na fila,
                #     ele é adicionado na fila
                for vizinho, _ in self.vizinhanca(vert):
                    if vizinho not in visitados and vizinho not in Q:
                        Q.append(vizinho)
        #Ordena os vértices de acordo com o tempo de descoberta
        visitados = sorted(visitados, reverse=True)
        for vert in visitados:
            cont += 1
            dicFim[vert] = cont
        #Retorna os tempos de descoberta e finalização e os antecessores
        return dicIni, dicFim, dicpi

    def bellmanford(self, vertice):
        """
        Realiza o algoritmo de Bellman-Ford a partir de um vértice.

        Parâmetros:
        - vertice (str): O vértice de partida do algoritmo.

        Retorna:
        - d (dict): Um dicionário contendo as distâncias mínimas de cada vértice em relação ao vértice de partida.
        - pi (dict): Um dicionário contendo os predecessores de cada vértice no caminho mínimo.
        - mensagem (str) - condicional: Uma mensagem indicando que foi detectado um ciclo negativo.

        """
        #Inicializa os atributos da distância e do antecessor
        d, pi = {}, {}
        # Coloca a distância inicial para os outros vértices como infinita e o antecessor como None
        d = {vert: self.MAX_TAM for vert in self.listaAdjacencia.keys()}
        pi = {vert: None for vert in self.listaAdjacencia.keys()}
        # Coloca a distância inicial para o vértice de partida como 0
        d[vertice] = 0
        # Relaxa as arestas repetidamente
        for _ in range(self.n() - 1):
            for vert in self.listaAdjacencia.keys():
                for vizinho, peso in self.vizinhanca(vert):
                    if d[vizinho] > d[vert] + peso:
                        d[vizinho] = d[vert] + peso
                        pi[vizinho] = vert
        # Verifica se há ciclos negativos
        for vert in self.listaAdjacencia.keys():
            for vizinho, peso in self.vizinhanca(vert):
                if d[vizinho] > d[vert] + peso:
                    return None, None, "Detectado ciclo negativo"

        return d, pi, None

    def dijkstra(self, vertice):
        """
        Realiza o algoritmo de Dijkstra a partir de um vértice.

        Parâmetros:
        - vertice (str): O vértice de partida do algoritmo.

        Retorna:
        - d (dict): Um dicionário contendo as distâncias mínimas de cada vértice em relação ao vértice de partida.
        - pi (dict): Um dicionário contendo os predecessores de cada vértice no caminho mínimo.

        """
        #Inicializa os atributos da distância, do antecessor, da fila e dos vértices visitados
        d, pi, Q, visitados = {}, {}, [], set()
        # Coloca a distância inicial para os outros vértices como infinita e o antecessor como None
        d = {vert: self.MAX_TAM for vert in self.listaAdjacencia.keys()}
        pi = {vert: None for vert in self.listaAdjacencia.keys()}
        # Coloca a distância inicial para o vértice de partida como 0
        d[vertice] = 0
        # Adiciona o vértice de partida na fila
        Q.append(vertice)
        # Enquanto a fila não estiver vazia, o algoritmo continua
        while Q:
            vert = hq.heappop(Q)
            if vert in visitados:
                continue
            # Se o vértice não estiver na lista de visitados, ele é adicionado
            visitados.add(vert)
            # Relaxa as arestas repetidamente
            for vizinho, peso in self.vizinhanca(vert):
                if d[vizinho] > d[vert] + peso:
                    d[vizinho] = d[vert] + peso
                    pi[vizinho] = vert
                    hq.heappush(Q, vizinho)

        return d, pi

    def caminhoVertice(self, valor, T):
        """
        Encontra um caminho de tamanho mínimo que passe por um determinado número de vértices.

        Parâmetros:
        - valor (int): O número mínimo de vértices que o caminho deve passar.
        - T (dict): árvore geradora emitida por meio de um dos algoritmos.

        Retorna:
        - caminho (list): Uma lista contendo o caminho encontrado.

        """
        #Inicializa os vértices visitados e o caminho
        visitados, caminho = set(), []
        #Para cada vértice, se ele não estiver na lista de visitados, ele é adicionado
        for vertice in self.listaAdjacencia.keys():
            if vertice not in visitados:
                visitados.add(vertice)
                #Obtém o pai do vértice usando a árvore T
                pai = T[vertice]
                #Enquanto o pai não for None, ele é adicionado ao caminho
                while pai is not None:
                    caminho.append(pai)
                    #O pai do vértice é atualizado
                    pai = T[pai]
                #Se o tamanho do caminho for maior ou igual ao valor mínimo, ele é retornado
                if len(caminho) >= valor:
                    return caminho
                else:
                    #Se o tamanho do caminho for menor que o valor mínimo, ele é esvaziado
                    caminho.clear()
                    continue

        return None

    def checarCiclo(self, T):
        """
        Verifica se existe um ciclo de tamanho mínimo no grafo.

        Parâmetros:
        - T (dict): Um dicionário contendo os predecessores de cada vértice.

        Retorna:
        - ciclos (list): Uma lista contendo o ciclo encontrado.
        - mensagem (str) - condicional: Uma mensagem indicando que não há ciclos de tamanho mínimo.

        """
        #Buscamos primeiro um caminho de tamanho mínimo que passe por 5 vértices (valor escolhido com base nas orientações)
        ciclos = self.caminhoVertice(5, T)
        #Criaremos uma cópia em ordem contrária
        ciclosReversos = ciclos.copy()
        ciclosReversos.reverse()

        #Para cada vértice no caminho, verificamos se o vértice inicial é vizinho do vértice final
        for vertice in ciclos:
            for vizinho, _ in self.vizinhanca(vertice):
                if ciclosReversos[0] == vizinho:
                    index = ciclos.index(vertice)
                    #Se o vértice inicial for vizinho do vértice final, verificamos se o tamanho do ciclo é maior ou igual a 5
                    if index >= 5:
                        ciclos = ciclosReversos[0:index]
                        ciclos.append(ciclosReversos[0])
                        return ciclos
        #Se não houver ciclos de tamanho mínimo, retorna uma mensagem
        return "Não há ciclos com tamanho >= 5"

    def verticeMaisDistante(self, vertice):
        """
        Encontra o vértice mais distante de um vértice de partida.

        Parâmetros:
        - vertice (str): O vértice de partida do algoritmo.

        Retorna:
        - maior (tuple): Uma tupla contendo o vértice mais distante e sua distância.
        """
        #Inicializa os atributos da distância e ignoramos o atributo pi retornado pelo Djikstra
        d, _ = self.dijkstra(vertice)
        #Obtém o vértice mais distance em relação ao vértice de partida
        maior = max(d.items(), key = lambda x: x[1])
        return maior

    def lerInput(self, caminhoInput):
        """
        Lê o arquivo de entrada e adiciona as arestas ao grafo.

        Parâmetros:
        - caminhoInput (str): O caminho do arquivo de entrada.

        """
        try:
            with open(caminhoInput, 'r') as arquivo:
                for linha in arquivo.readlines():
                    palavras = linha.split(" ")
                    if not palavras:
                        continue
                    if palavras[0] == 'c': #Ignora as linhas marcadas com c
                        continue
                    if palavras[0] == 'p': #Ignora as inhadas marcadas com p
                        continue
                    if palavras[0] == 'a': #Adiciona as arestas marcadas com a (arco)
                        #Pega as informações da aresta
                        x, y, p = palavras[1], palavras[2], palavras[3]
                        #Converte o peso para inteiro
                        p = int(p)
                        #Adiciona a aresta ao grafo
                        self.addAresta(x, y, p)

        except FileNotFoundError:
            #Caso não encontre o arquivo, será emitida uma mensagem de erro
            print("Arquivo não encontrado!")
        except Exception as e:
            #Caso ocorra algum erro na leitura do arquivo, será emitida uma mensagem de erro
            print("Erro na leitura do arquivo: ", e)
