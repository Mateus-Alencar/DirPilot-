import os
import platform

def limpar_tela():
    comando = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(comando)

def mostrar_diretorio_atual():
    print(f"\n📁 Diretório atual: {os.getcwd()}") # retorna o caminho completo do diretório atual

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

def terminal():
    limpar_tela()
    print("🔧 Terminal de Navegação de Diretórios - Digite 'ajuda' para comandos\n")
    
    while True:
        mostrar_diretorio_atual()
        comando = input(">>> ").strip()

        if comando == "ajuda":
            print("""
Comandos disponíveis:
  ls                 - Listar conteúdo do diretório atual
  cd <caminho>       - Mudar para outro diretório
  cd ..              - Voltar um diretório
  clear              - Limpar a tela
  exit               - Sair do terminal
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

        else:
            print("❓ Comando não reconhecido. Digite 'ajuda'.")

if __name__ == "__main__":
    terminal()
