import os
import platform
import subprocess
import time

def limpar_tela():
    comando = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(comando)

def mostrar_diretorio_atual():
    print(f"\n📁 Diretório atual: {os.getcwd()}") 

def listar_conteudo():
    print("\n📄 Conteúdo:")
    for item in os.listdir():
       print(f"  - {item}")

def mudar_diretorio(caminho):
    try:
        os.chdir(caminho)
    except FileNotFoundError:
        print("❌ Caminho não encontrado.")
    except NotADirectoryError:
        print("❌ Isso não é um diretório.")
    except PermissionError:
        print("❌ Sem permissão para acessar esse diretório.")

def conexoes_ativas():
    #Usa o módulo subprocess para executar o comando netstat -n no terminal:
    #    -n: Mostra os endereços em formato numérico (sem DNS).
    #    capture_output=True: captura a saída do comando.
    #    text=True: retorna como string (em vez de bytes)
    try:
        resultado = subprocess.run(['netstat', '-n'], capture_output=True, text=True)
        linhas = resultado.stdout.splitlines()
        ips = []
        for linha in linhas:
            if "ESTABLISHED" in linha:
                partes = linha.split()
                if len(partes) >= 3:
                    ip_destino = partes[2].split(":")[0]
                    ips.append(ip_destino)
        print(ips)
        return ips
    except Exception as e:
        print(f"Erro ao capturar conexões: {e}")
        return []

def monitorar(ip_monitorado):
    print(f"Monitorando acesso ao IP: {ip_monitorado}")
    while True:
        ips_conectados = conexoes_ativas()
        if ip_monitorado in ips_conectados:
            print(f"🔔 IP {ip_monitorado} foi acessado!")
            break
        else:
            print("Nenhuma conexão com o IP monitorado.")
        time.sleep(5)  


def terminal():
    limpar_tela()
    print("🔧 Terminal de Navegação de Diretórios - Digite 'ajuda' para comandos\n")
    
    while True:
        mostrar_diretorio_atual()
        comando = input(">>> ").strip()

        if comando == "ajuda":
            print("""
Comandos disponíveis:
  ls                     - Listar conteúdo do diretório atual
  cd <caminho>           - Mudar para outro diretório
  cd ..                  - Voltar um diretório
  clear                  - Limpar a tela
  exit                   - Sair do terminal
  netstat -an | grep     - Monitorar acesso
""")

        elif comando == "ls":
            listar_conteudo()

        elif comando.startswith("cd "):
            caminho = comando[3:].strip()
            mudar_diretorio(caminho)

        elif comando == "cd ..":
            mudar_diretorio("..")

        elif comando == "clear":
            limpar_tela()

        elif comando == "exit":
            print("Saindo do terminal...")
            break
        elif comando == "netstat -an | grep":
            IPmonitorado = input("Ip a ser monitorado: ")
            monitorar(IPmonitorado)
        else:
            print("❓ Comando não reconhecido. Digite 'ajuda'.")

if __name__ == "__main__":
    terminal()
