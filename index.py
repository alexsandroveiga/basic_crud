from utils import *
from views import *

options = {
  1: 'Clientes',
  2: 'Motos',
  3: 'Vendas',
  4: 'Consultas',
  5: 'Sair'
}

while True:
  show_menu(options)
  option = ''
  while option not in options.keys():
    try:
      option = int(input('Escolha uma opção: '))
    except:
      print('Opção inválida, digite um número de 1 a 5...\n')
  if option == 1:
    customer_view()
  elif option == 2:
    motorcycle_view()
  elif option == 3:
    print('Vendas em breve...')
    exit()
  elif option == 4:
    print('Consultas breve...')
    exit()
  elif option == 5:
    print('Obrigado por usar nosso sistema!')
    exit()