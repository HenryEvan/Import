from pysnmp.hlapi import SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, getCmd
import os

def testar_snmp(ip):
    print(f"Tentando SNMP em {ip}...")
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData('s1m_isp', mpModel=1),  # mpModel=1 indica SNMPv2c
            UdpTransportTarget((ip, 161), timeout=1, retries=1),  # Porta SNMP e timeout configurados
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))  # OID comum para teste (sysDescr)
        )

        error_indication, error_status, error_index, var_binds = next(iterator)

        # Verifica o resultado da requisição SNMP
        if error_indication:
            print(f"[{ip}] Erro de indicação: {error_indication}")
            return "Não"
        elif error_status:
            print(f"[{ip}] Erro de status: {error_status.prettyPrint()}")
            return "Não"
        else:
            for var_bind in var_binds:
                print(f"[{ip}] Resposta recebida: {var_bind}")
            return "Sim"
    except Exception as e:
        print(f"[{ip}] Exceção capturada: {e}")
        return "Não"

def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    resultados = []
    for linha in linhas:
        partes = linha.strip().split("\t")
        if len(partes) < 2:
            print(f"Linha inválida: {linha.strip()}")
            continue
        nome = partes[0]
        ip = partes[1]
        resultado_snmp = testar_snmp(ip)
        resultados.append(f"{nome}\t{ip}\t{resultado_snmp}")

    with open("resultado_snmp.txt", "w") as arquivo_resultado:
        arquivo_resultado.write("\n".join(resultados))
    print("Teste SNMP finalizado. Resultados salvos em resultado_snmp.txt.")

# Caminho do arquivo de entrada
caminho_arquivo = "1.txt"
processar_arquivo(caminho_arquivo)
