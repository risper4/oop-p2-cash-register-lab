#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self._discount = discount
    self.total = total
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self) :
    return self._discount
  
  @discount.setter
  def discount(self, value) :
    if value is int and 0 <= value <= 100 :
      self._discount = value
    else :
      raise ValueError('Invalid discount input')
    
  def add_item(self, item, price, quantity = 1) :
    self.total += (price * quantity)
    self.items.extend([item] * quantity)
    new_transaction = {
      'item' : item,
      'price' : price,
      'quantity' : quantity
    }
    self.previous_transactions.append(new_transaction)

  def apply_discount(self) :
    if len(self.previous_transactions) == 0 or self.discount == 0 :
      print('There is no discount to apply.')
      return
    else :
      discounted_total = self.total * (1 - (self.discount/100))
      print(f'After the discount, the total comes to ${discounted_total}')
      
   
  def void_last_transaction(self) :
    last = self.previous_transactions[-1]
    self.total -= (last['price'] * last['quantity'])
    self.previous_transactions.pop()
        

milk = CashRegister(20)
milk.add_item('Milk', 100, 2)
dairy = CashRegister(10)
dairy.add_item('Milk', 100, 1)
print(dairy.items)
print(dairy.apply_discount())
print(milk.items)
print(milk.previous_transactions)
print(milk.apply_discount())


  