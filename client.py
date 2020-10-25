import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:8000')

print("Opções:")
print("1 - Listar arquivos do diretório atual")
print("2 - Selecionar um diretório para listar todos os arquivos a partir dele")
print("3 - Selecionar um diretório para listar apenas seus arquivos")
print("4 - Verifica se um arquivo existe em um diretório")
print("5 - Listar processos em execução")

opcao = input()

if opcao == "1":
    print(server.files_list())

if opcao == "2":
    print("Digite o caminho do diretório")
    path = input()
    print(server.dir_files_list(path))

if opcao == "3":
    print("Digite o caminho do diretório")
    path = input()
    print(server.dir_files_only_list(path))

if opcao == "4":
    print("Digite o caminho do diretório")
    path = input()
    print("Digite o nome do arquivo junto com a extensão")
    file = input()
    print(server.file_exists(path, file))
    
if opcao == "5":
    print(server.process_list())



    