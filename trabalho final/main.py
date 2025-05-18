
#jogando teste na main para ver se funciona no futuro pra chamar todas as funções aqui
#depois concertar 

criar_postos(grafo)
criar_coleta(grafo)
lagos = [k for k in grafo if grafo[k]["info"][2]]   
postos = [k for k in grafo if grafo[k]["info"][1]]
criarfogo(grafo, postos, lagos)

# Mostra estado inicial
print("\n=== Estado inicial do grafo ===")
for vertice, dados in grafo.items():
    info = dados["info"]
    vizinhos = ", ".join([f"{v} (custo {c})" for v, c in dados["vizinhos"]])
    print(f"Vértice {vertice}:")
    print(f"  Água necessária: {info[0]}")
    print(f"  Posto de brigada: {info[1]}")
    print(f"  Lago: {info[2]}")
    print(f"  Estado do fogo: {info[3]}")
    print(f"  Vizinhos: {vizinhos}")
    print()

# Propagação inicial
print("\n=== Propagando fogo... ===")
propagacao(grafo)

# Cria brigadas nos postos
brigadas = []
for p in postos:
    b = Vingadores(p, qtd_agua = 2)
    brigadas.append(b)

turno = 0
tempo_fogo = {}

print("\n=== Simulando turnos até o fogo acabar ===")
while em_chamas(grafo):
    print(f"\n------ TURNO {turno} ------")
    
    # Atualiza tempo de fogo
    for vertice in grafo:
        if grafo[vertice]["info"][3] == 1:
            tempo_fogo[vertice] = tempo_fogo.get(vertice, 0) + 1
            if tempo_fogo[vertice] >= 4:
                grafo[vertice]["info"][3] = 2  # queimado
                print(f"💀 O vértice {vertice} queimou completamente após 4 turnos!")

    # Diminui intensidade do fogo com o tempo
    for vertice in grafo:
        if grafo[vertice]["info"][3] == 1:
            if grafo[vertice]["info"][0] > 0:
                grafo[vertice]["info"][0] -= 1
                print(f"🔥 O fogo em {vertice} perdeu intensidade! Agora precisa de {grafo[vertice]['info'][0]} de água.")
            if grafo[vertice]["info"][0] == 0:
                grafo[vertice]["info"][3] = -1
                print(f"✅ O fogo em {vertice} apagou sozinho por falta de combustível.")

    # Ações das brigadas
    for b in brigadas:
        b.andando(grafo)

    # Propagação do fogo
    propagacao(grafo)

    turno+=1

# Mostra caminhos percorridos
print("\n=== Caminhos percorridos pelas brigadas ===")
for b in brigadas:
    print(f"Brigada iniciou em {b.trajeto[0]} e percorreu:")
    print(" → ".join(b.trajeto))

# Imprime grafo com marcações
imprimirTrajetos(grafo, brigadas)
