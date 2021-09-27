import random

'''

  Create a empty map to start, maps are collections, it's better to name 'users' instead of 'user'

'''
MAX_NUMBER_OF_USERS = 5
MIN_MEMORY_LIMIT = 1
MAX_MEMORY_LIMIT = 1001
users_map = {}

posi = 1

'''
  First loop to read the 'usernames' and populate the map with random values.
'''
while posi <= MAX_NUMBER_OF_USERS:
    randomMemory = random.randint(MIN_MEMORY_LIMIT, MAX_MEMORY_LIMIT)  # esta utilizando as variaveis como
    # limitador do random
    userNameKey = input(f'Digite o {posi} nome: ')
    users_map[userNameKey] = randomMemory  # ele add o usernamekey como chave e o random como valor
    posi += 1
# print(users_map)
'''
  Second loop to print the map values.
'''
for username, memory in users_map.items():
    print(f'o usuário {username} está consumindo {memory}')

