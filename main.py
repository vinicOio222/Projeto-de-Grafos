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
    g.ExibirVertice("4162")
    print(g.m())
    print(g.n())
    print(g.vizinhanca("4162"))
    print(g.d("4162"))
    print(g.w("4162", "4161"))
    print(g.vizinhanca("4162"))
    print(g.dist("4162"))
    print(g.minD())
    print(g.maxD())
    
    #main()