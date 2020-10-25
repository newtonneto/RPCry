import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:8000')

print(server.files_list())
print(server.dir_files_list("D:\Downloads"))
print(server.dir_files_only_list("D:\Downloads"))
print(server.file_exists("D:\Downloads/", "TCE.pdf"))
print(server.process_list())