"""
Sistema de arquivos navegação

Para manipulação importamos o módulo os

getcwd() = pega o diretorio que voce esta

chdir('..') = muda o diretorio, nesta caso volta uma pasta
"""
import os

"""
print(os.getcwd())  # mostra o diretório que você esta, (caminho absoluto)

os.chdir('..')

print(os.getcwd())
"""

"""
print(os.path.isabs('/home/geek'))  # retorna se o diretório é absoluto

print(os.path.isabs('C:\\Users\\geek'))  # forma para Windows, precisa ser a barra dupla para o sistema n confundir
"""

"""
print(os.name)  # para identificar o sistema operacional

print(os.uname())  # mostra as informações do maquina e sistema operacional

import sys

print(sys.platform)  # mostra o nome do sistema operacional
"""

"""
# verificando caminhos

print(os.getcwd())

os.chdir('..')

res = os.path.join(os.getcwd(), 'atividades', 'Atividades_de_treino')
# os.path.join, recebe o diretorio atual e o diretorio que faremos acesso

os.chdir(res)

print(os.getcwd())
"""

#  listar os arquivos

print(os.listdir('//'))

#  listar arquivos com mais detalhes

scanner = os.scandir('//')

arquivos = list(scanner)

print(arquivos[0].name)  # nome

print(arquivos[0].inode())  # numeração do objeto na arvore de diretorios

print(arquivos[0].is_dir())  # é um diretorio ?

print(arquivos[0].is_file())  # é um arquivo?

print(arquivos[0].is_symlink())  # é um link simbólico?

print(arquivos[0].path)  # caminho até o arquivo

print(arquivos[0].stat())  # mostra as informações do arquivo

# quando usamos o scandir() precisamos fecha-lo

scanner.close()