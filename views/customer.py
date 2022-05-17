from utils import *
from models import Customer

from terminaltables import SingleTable

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

def customer_view():
  show_menu(options)
  option = ''
  while option not in options.keys():
    try:
      option = int(input('Escolha uma opção: '))
    except:
      print('Opção inválida, digite um número de 1 a 6...')
    if option == 1:
      customer = customerRepo.create(
        name=input('Nome: '),
        email=input('Email: '),
        phone=input('Telefone: '),
        address=input('Endereço: ')
      )
      
      return adapt_table('Novo cliente', format_table_header(customer), [customer])
    if option == 2:
      customers = customerRepo.read()
      return adapt_table('Clientes', format_table_header(customers[0]), customers)
    if (option == 3):
      try:
        customer = customerRepo.findByEmail(input('Email: '))
        return adapt_table('Cliente encontrado', format_table_header(customer), [customer])
      except:
        print('Cliente não encontrado')
    if (option == 4):
      try:
        customer = customerRepo.update(
          id=input('ID: '),
          name=input('Nome: '),
          email=input('Email: '),
          phone=input('Telefone: '),
          address=input('Endereço: ')
        )
        return adapt_table('Clientes', format_table_header(customer), [customer])
      except:
        print('Cliente não encontrado')
    if (option == 5):
      try:
        customerRepo.delete()
        print('Cliente deletado com sucesso!')
      except:
        print('Cliente não encontrado')
    if option == 6:
      break
    if option == 7:
      exit()