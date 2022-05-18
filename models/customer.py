from uuid import uuid4

customers = []

class Customer:
  def create(self, name, email, phone, address):
    customers.append({
      'id': str(uuid4()),
      'name': name,
      'email': email,
      'phone': phone,
      'address': address
    })
    for customer in customers:
      if customer['email'] == email:
        return customer

  def read(self):
    return customers

  def findByEmail(self, email):
    for customer in customers:
      if customer['email'] == email:
        return customer

  def find(self, id):
    for customer in customers:
      if customer['id'] == id:
        return customer

  def update(self, id, name, email, phone, address):
    for customer in customers:
      if customer['id'] == id:
        customer['name'] = name
        customer['email'] = email
        customer['phone'] = phone
        customer['address'] = address
        return customer

  def delete(self, id):
    for customer in customers:
      if customer['id'] == id:
        customers.remove(customer)
        return None