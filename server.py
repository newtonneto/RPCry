from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import psutil as ps #pip install psutil
import os

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Cria o server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Funções do servidor
    # Listar arquivos a partir do diretorio em que o servidor está rodando
    def files_list():
      array_files = []
      for subdir, dirs, files in os.walk('./'):
        for file in files:
          array_files.append(file)

      if (len(array_files) == 0):
        return "Nenhum arquivo neste diretório"

      return array_files
    server.register_function(files_list)

    # Listar arquivos a partir de um diretorio especificado
    def dir_files_list(path):
      array_files = []
      for subdir, dirs, files in os.walk(path):
        for file in files:
          array_files.append(file)

      if (len(array_files) == 0):
        return "Nenhum arquivo neste diretório ou diretório inválido"

      return array_files
    server.register_function(dir_files_list)

    # Lista apenas os arquivos presentes na raiz de um diretorio
    def dir_files_only_list(path):
      array_files = []
      dirs = os.listdir(path)
      for file in dirs:
        array_files.append(file)

        if (len(array_files) == 0):
          return "Nenhum arquivo neste diretório ou diretório inválido"

      return array_files
    server.register_function(dir_files_only_list)

    # Verificar se um arquivo existe
    def file_exists(path, filename):
      if os.path.isfile(path + filename):
        return "Arquivo encontrado"

      return "Arquivo não encontrado"
    server.register_function(file_exists)

    # Lista os processos em execução
    def process_list():
      array_process = [process.name() for process in ps.process_iter()]

      return array_process
    server.register_function(process_list)
      

    # Faz o server ficar rodando em loop
    server.serve_forever()