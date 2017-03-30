'''
Python inheritance example
http://www.dreamincode.net/forums/topic/182253-import-another-py-file/
'''
import oop

'''
Inheritance Template

class subclass(parentclass):
    def __init__(self):
        parentclass.__init__(self)
        self.new_subclass_attributes = 'sumptin'
'''

class BlackPerson(Person):
  def __init__(self):
    Person.__init__(self):
    self.race = 'African American'