from uuid import uuid4

clientes = []
motos = []

while True:
  print("""
1 - CRUD de clientes
2 - CRUD de motos
3 - Sair
  """)

  opcao = int(input("Digite uma opção: "))

  if opcao == 1:
    print("""
1 - Criar cliente
2 - Listar clientes
3 - Alterar cliente
4 - Excluir cliente
5 - Voltar
6 - Sair
    """)

    while True:
      opcao = int(input("Digite uma opção: "))

      if opcao == 1:
        nome = input("Nome: ")
        email = input("Email: ")
        clientes.append({
          "id": str(uuid4()),
          "nome": nome,
          "email": email
        })
        print('Cliente criado com sucesso!')        

      elif opcao == 2:
        for cliente in clientes:
          print(cliente)

      elif opcao == 3:
        id = input("Id: ")
        for cliente in clientes:
          if cliente["id"] == id:
            cliente["nome"] = input("Novo nome: ")
            cliente["email"] = input("Novo email: ")
            print('Cliente atualizado com sucesso!')
          print('Cliente não encontrado!')

      elif opcao == 4:
        id = input("Id: ")
        for cliente in clientes:
          if cliente["id"] == id:
            clientes.remove(cliente)
            print('Cliente deletado com sucesso!')
          print('Cliente não encontrado!')

      elif opcao == 5:
        break

      elif opcao == 6:
        exit()

  if opcao == 2:
    print("""
1 - Criar moto
2 - Listar motos
3 - Alterar moto
4 - Excluir moto
5 - Voltar
6 - Sair
    """)

    while True:
      opcao = int(input("Digite uma opção: "))

      if opcao == 1:
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        motos.append({
          "id": str(uuid4()),
          "marca": marca,
          "modelo": modelo
        })
        print('Moto criada com sucesso!')

      elif opcao == 2:
        for moto in motos:
          print(moto)

      elif opcao == 3:
        id = input("Id: ")
        for moto in motos:
          if moto["id"] == id:
            moto["marca"] = input("Novo marca: ")
            moto["modelo"] = input("Novo modelo: ")

      elif opcao == 4:
        id = input("Id: ")
        for moto in motos:
          if moto["id"] == id:
            motos.remove(moto)

      elif opcao == 5:
        break

      elif opcao == 6:
        exit()

  if opcao == 3:
    exit()
  