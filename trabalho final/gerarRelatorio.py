import sys
import os

def gerar_relatorio(nome_arquivo="relatorio.txt"):
    
    caminho_completo = os.path.join(os.path.dirname(__file__), nome_arquivo)
    sys.stdout = open(caminho_completo, "w", encoding="utf-8")
