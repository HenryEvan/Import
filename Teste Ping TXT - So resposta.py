import os

def testar_ping(ip):
    # Executa o comando ping; '-c 1' para Unix e '-n 1' para Windows.
    comando = f"ping -c 1 {ip}" if os.name != "nt" else f"ping -n 1 {ip}"
    resposta = os.system(comando)
    return "Sim" if resposta == 0 else "Não"

def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    resultados = []
    for linha in linhas:
        partes = linha.strip().split("\t")
        ip = partes[1]
        resultado_ping = testar_ping(ip)
        resultados.append(resultado_ping)

    with open("2.txt", "w") as arquivo_resultado:
        arquivo_resultado.write("\n".join(resultados))

# Caminho do arquivo de entrada
caminho_arquivo = "1.txt"
processar_arquivo(caminho_arquivo)
