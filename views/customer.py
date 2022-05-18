from utils import *
from models import *

customerRepo = Customer()

options = {
  1: 'Criar',
  2: 'Listar',
  3: 'Buscar por email',
  4: 'Atualizar',
  5: 'Deletar',
  6: 'Voltar',
  7: 'Sair'
}

table_items = {
  'id': 'Id',
  'name': 'Nome',
  'email': 'Email',
  'phone': 'Telefone',
  'address': 'Endereço'
}

def customer_view():
  while True:
    show_menu(options)
    try:
      option = int(input('Escolha uma opção: '))
    except:
      print('Opção inválida, digite um número de 1 a 6...\n')
    if option == 1:
      customer = customerRepo.create(
        name=input('Nome: '),
        email=input('Email: '),
        phone=input('Telefone: '),
        address=input('Endereço: ')
      )      
      adapt_table('Cliente', format_table_header(customer, table_items), [customer])
    if option == 2:
      customers = customerRepo.read()
      if customers.__len__() != 0:
        adapt_table('Clientes', format_table_header(customers[0], table_items), customers)
      else:
        print('Nenhum cliente cadastrado.\n')
    if (option == 3):
      customer = customerRepo.findByEmail(input('Email: '))
      if customer:
        adapt_table('Cliente', format_table_header(customer, table_items), [customer])
      else:
        print('Cliente não encontrado.\n')
    if (option == 4):
      customer = customerRepo.find(input('Id: '))
      if customer:
        customer = customerRepo.update(
          id=customer['id'],
          name=input('Nome: '),
          email=input('Email: '),
          phone=input('Telefone: '),
          address=input('Endereço: ')
        )
        adapt_table('Cliente', format_table_header(customer, table_items), [customer])
      else:
        print('Cliente não encontrado.\n')
    if (option == 5):
      customer = customerRepo.find(input('Id: '))
      if customer:
        customerRepo.delete(customer['id'])
        print('Cliente deletado com sucesso!\n')
      else:
        print('Cliente não encontrado.\n')
    if option == 6:
      break
    if option == 7:
      print('Obrigado por usar nosso sistema!')
      exit()