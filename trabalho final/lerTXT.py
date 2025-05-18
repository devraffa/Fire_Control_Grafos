#tentando aprender 
import os

def ler_grafo_txt(entrada):
    grafo = {}

    caminho = os.path.join(os.path.dirname(__file__), entrada)
    with open(caminho, 'r') as arquivo:
        for linhas in arquivo:
            if not linhas.strip() or linhas.startswith("#"):
                continue

            partes = linhas.strip().split()
            vertice = partes[0]
            agua = int(partes[1])
            posto = partes[2] == "True"
            lago = partes[3] == "True"
            fogo = int(partes[4])

            vizinhos = []
            for i in partes[5:]:
                nome, custo = i.split(":")
                vizinhos.append((nome, int(custo)))

            grafo[vertice] = {
                "info": [agua, posto, lago, fogo],
                "vizinhos": vizinhos
            }
    return grafo


if __name__ == "__main__":
    grafo = ler_grafo_txt("entrada.txt")
    print("📋 Grafo carregado:")
    for v, dados in grafo.items():
        print(f"Vértice {v}:")
        print(f"  Info → Água: {dados['info'][0]}, Posto: {dados['info'][1]}, Lago: {dados['info'][2]}, Fogo: {dados['info'][3]}")
        print(f"  Vizinhos → {dados['vizinhos']}")
        print()

           
           

