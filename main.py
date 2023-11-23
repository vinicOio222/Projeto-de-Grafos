from classes_lib.Digrafo import Digrafo
from classes_lib.Grafo import Grafo

# op  = int(input("Escolha o objeto de análise:"))
# print(
#     "1. Grafo" + "\n"
#     + "2. Digrafo"  + "\n"
#     )

if __name__ == "__main__":
    g = Grafo("_input/USA-NY-road.txt")
    #g.ExibirGrafo()
    print(g.m()) 
    print(g.n())
    print(g.vizinhanca("10000"))
    #main()