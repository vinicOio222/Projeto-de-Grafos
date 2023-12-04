from classes_lib.Digrafo import Digrafo
from classes_lib.Grafo import Grafo

"""
Este código permite ao usuário escolher entre analisar um grafo ou um digrafo.
Ele solicita ao usuário que selecione o objeto de análise e um vértice.
Em seguida, realiza várias operações no objeto escolhido, como encontrar as distâncias mínima e máxima,
calcular um caminho de determinado comprimento, verificar ciclos e encontrar o vértice mais distante de um vértice dado.
"""

print(
    "1. Grafo" + "\n"
    + "2. Digrafo"  + "\n"
)

op = int(input("Escolha o objeto de análise: "))

tipo_classe = Grafo("_input/USA-NY-road.txt") if op == 1 else Digrafo("_input/USA-NY-road.txt")
tipo  = 'G' if op == 1 else 'D'

vertice  = input("Escolha o vértice: ")
print(f'a) O valor de {tipo}.minD() = {tipo_classe.minD()}')
print("-"*100)
print(f'b) O valor de {tipo}.maxD() = {tipo_classe.maxD()}')
_, T = tipo_classe.dijkstra(vertice)
print("-"*100)
print(f'c) Um caminho de tamanho 10 ou superior para o vértice {vertice} é: {tipo_classe.caminhoVertice(10, T)}')
print("-"*100)
print(f'd) Um ciclo com quantidade de arestas maior ou igual a 5: {tipo_classe.checarCiclo(T)}')
print("-"*100)
print(f'e) O vértice mais distante de 129, e o valor da distância entre eles é: {tipo_classe.verticeMaisDistante("129")}')
