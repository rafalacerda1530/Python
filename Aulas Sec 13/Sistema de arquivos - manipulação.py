"""
Manipulação de arquivos


"""
import os
"""


print(os.path.exists('frutas.txt'))  # verificando se existe um arquivo, retorna TRUE ou FALSE
"""

"""
# CRIANDO ARQUIVOS

open('arquivos_teste.txt', 'w').close()

# forma 2
open('arquivos_teste2.txt', 'a').close()

# forma 3
with open('arquivo_teste3.txt', 'w') as arquivo:
    pass

# forma correta

os.mknod('arquivo_teste4.txt')

os.mknod('/home/rafael/PycharmProjects/ppe/Aulas Sec 13/arquivo_teste5.txt')

# no MAC OS pode ter um erro de PermissionError
# se o arquivo existir teremos um erro FileEXists
"""

"""
# criando diretórios

os.mkdir('teste1')  # cria o diretório, se ele ja existir teremos o erro FileEXists, (path relativo)
os.mkdir('/home/rafael/PycharmProjects/ppe/Aulas Sec 13/teste2')  # path absoluto

# OBS: se não tiver permissões para criar o diretorio, teremos PermissionError

# criando dois diretorios

os.makedirs('teste1/teste2')  # esta criando o dir teste1 e o teste2 dentro dele
# se ele ja existir teremos o erro FileEXists

# tratando erro no makedirs

os.makedirs('teste1', exist_ok=True)  # exist_ok=True, se ele existir, retorne TRUE
"""

"""
# renomeando diretórios e arquivos

os.rename('teste1', 'renomeado')
# se o diretório não estiver vazio, teremos um OSError
# para renomear arquivos é da mesma forma
# se você colocar todo o caminho no apontamento, deve-se colocar todo o caminho na alteração tbm
# os.rename('caminh/teste1', 'caminho/renomeado')
"""

"""
# deletar arquivos

# ao deletar os arquivos ele não vão para a lixeira
# ele não deleta diretórios, somente arquivos

os.remove('frutas.txt')
"""

"""
# deletando diretórios vazios

os.rmdir('teste2')  
"""

"""
# deletando diretorios com diretorios vaziso dentro dentro
os.removedirs('renomeado/teste2')
# precisa colocar o caminho dos diretórios
# se o diretorio tiver arquivos o processo para
"""

"""
# encaminhando arquivos e diretórios para a lixeira

from send2trash import send2trash

os.remove('cesta1')  # não vai para a lixeira
send2trash('cesta2')  # vai para a lixeira, pode ser restaurado

send2trash('teste')
"""

"""
# diretorio temporários

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'criei temporariamente o arquivo em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('RAFAEL LACERDA\n')
    input()

# criou um diretorio temporário e dentro dele colocamos um arquivo, após encerrar o bloco with ele apaga o arquivo
"""

"""
import tempfile

# criando arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'RAFAEL LACERDA\n')  # em arquivos temporários so lemos em bytes, por isso o 'b'
    tmp.seek(0)
    print(tmp.read())
    input()

# forma 2 sem o bloco With

arquivo = tempfile.TemporaryFile()
arquivo.write(b'RAFAEL LACERDA')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# forma 3 

arquivo = tempfile.NamedTemporaryFile()

arquivo.write(b'RAFAEL LACERDA')
arquivo.seek(0)

print(arquivo.name)
print(arquivo.read())
input()

arquivo.close()
"""
