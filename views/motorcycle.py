from utils import *
from models import *

motorcycleRepo = Motorcycle()

options = {
  1: 'Criar',
  2: 'Listar',
  3: 'Atualizar',
  4: 'Deletar',
  5: 'Voltar',
  6: 'Sair'
}

table_items = {
  'id': 'Id',
  'brand': 'Marca',
  'model': 'Modelo',
  'price': 'Preço',
  'engine_capacity': 'Cilindrada',
  'max_power': 'Potência máxima'
}

def motorcycle_view():
  while True:
    show_menu(options)
    try:
      option = int(input('Escolha uma opção: '))
    except:
      print('Opção inválida, digite um número de 1 a 6...\n')
    if option == 1:
      motorcycle = motorcycleRepo.create(
        brand=input('Marca: '),
        model=input('Modelo: '),
        price=input('Preço: '),
        engine_capacity=input('Cilindrada: '),
        max_power=input('Potência máxima: ')
      )      
      adapt_table('Moto', format_table_header(motorcycle, table_items), [motorcycle])
    if option == 2:
      motorcycles = motorcycleRepo.read()
      if motorcycles.__len__() != 0:
        adapt_table('Motos', format_table_header(motorcycles[0], table_items), motorcycles)
      else:
        print('Nenhuma moto cadastrada.\n')
    if (option == 3):
      motorcycle = motorcycleRepo.find(input('Id: '))
      if motorcycle:
        motorcycle = motorcycleRepo.update(
          id=motorcycle['id'],
          brand=input('Marca: '),
          model=input('Modelo: '),
          price=input('Preço: '),
          engine_capacity=input('Cilindrada: '),
          max_power=input('Potência máxima: ')
        )
        adapt_table('Moto', format_table_header(motorcycle, table_items), [motorcycle])
      else:
        print('Moto não encontrada.\n')
    if (option == 4):
      motorcycle = motorcycleRepo.find(input('Id: '))
      if motorcycle:
        motorcycleRepo.delete(motorcycle['id'])
        print('Moto deletada com sucesso!\n')
      else:
        print('Moto não encontrada.\n')
    if option == 5:
      break
    if option == 6:
      print('Obrigado por usar nosso sistema!')
      exit()