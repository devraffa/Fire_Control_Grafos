#tentando aprender 

def ler_grafo_txt(entrada):
    grafo = {}

    with open(entrada, "r") as f:
        for linha in f:
            if linha.strip() == "" or linha.strip().startswith("#"):
                continue 

            partes = linha.strip().split()
            vertice = partes[0]
            agua = int(partes[1])
            is_posto = partes[2] == "True"
            is_lago = partes[3] == "True"
            fogo = int(partes[4])

            vizinhos = []
            for viz in partes[5:]:
                nome, custo = viz.split(":")
                vizinhos.append((nome, int(custo)))

            grafo[vertice] = {
                "info": [agua, is_posto, is_lago, fogo],
                "vizinhos": vizinhos
            }

    return grafo

if __name__ == "__main__":
    grafo = ler_grafo_txt("entrada.txt") 
    print("Grafo carregado:")
    for v, dados in grafo.items():
        print(f"{v}: {dados}")

