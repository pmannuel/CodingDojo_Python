class Cat(object):
  def __init__(self, color, type, age):
    self.color = color
    self.type = type
    self.age = age

garfield = Cat('orange', 'fat', 5)
print garfield.color

class pet(Cat):
    def __init__(self, color, type, age, owner):
        super(pet, self).__init__(color, type, age)
        self.owner = owner
        self.type = "indoor"

wasabi = pet('orange', 'lean', 2, "Mr. Sushi")
print wasabi

class Cats(object):
    def __init__(self):
        self.card1 = card("spade", "ace")
        self.card2 = card("spade", 2)
