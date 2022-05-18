from uuid import uuid4

motorcycles = []

class Motorcycle:
  def create(self, brand, model, price, engine_capacity, max_power):
    id = str(uuid4())
    motorcycles.append({
      'id': id,
      'brand': brand,
      'model': model,
      'price': price,
      'engine_capacity': engine_capacity,
      'max_power': max_power
    })
    for motorcycle in motorcycles:
      if motorcycle['id'] == id:
        return motorcycle

  def read(self):
    return motorcycles

  def find(self, id):
    for motorcycle in motorcycles:
      if motorcycle['id'] == id:
        return motorcycle

  def update(self, id, brand, model, price, engine_capacity, max_power):
    for motorcycle in motorcycles:
      if motorcycle['id'] == id:
        motorcycle['brand'] = brand
        motorcycle['model'] = model
        motorcycle['price'] = price
        motorcycle['engine_capacity'] = engine_capacity
        motorcycle['max_power'] = max_power
    return motorcycle

  def delete(self, id):
    for motorcycle in motorcycles:
      if motorcycle['id'] == id:
        motorcycles.remove(motorcycle)
    return None