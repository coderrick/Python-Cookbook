'''
Monads in Python ofijnfddf
'''
class Monad:
  #def __init__(self):

  def monad_greeting(self):
    print("Embarking on Monad journey")
  
  def multiply_by_2(self, n):
    return n * 2
  
  def divide_by_3(self, n):
    return n/3

  def round_it(self, n):
    return round(n)
  
  def apply_all_operations(self, n):
    return self.round_it(self.divide_by_3(self.multiply_by_2(n)))
    
p = Monad()
p.monad_greeting()