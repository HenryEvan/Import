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
        try:
            partes = linha.strip().split("\t")
            if len(partes) < 2:
                raise ValueError("Linha inválida: não contém nome e IP")
            nome = partes[0]
            ip = partes[1]
            resultado_ping = testar_ping(ip)
            resultados.append(f"{nome}\t{ip}\t{resultado_ping}")
        except Exception as e:
            resultados.append(f"Erro na linha: {linha.strip()} - {str(e)}")

    with open("resultado_ping.txt", "w") as arquivo_resultado:
        arquivo_resultado.write("\n".join(resultados))

# Caminho do arquivo de entrada
caminho_arquivo = "1.txt"
processar_arquivo(caminho_arquivo)
