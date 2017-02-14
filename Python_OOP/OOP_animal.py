class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 1000

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print 'name: {} \n health: {}'.format(self.name,self.health)

class Dog(Animal):
    def __init__(self, name, cuteness):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

penguinsaurus = Animal("penguinsaurus")
penguinsaurus.walk().walk().walk().run().run().displayHealth()

print '\n'

mastermind = Dog("mastermind")
mastermind.walk().walk().walk().run().run().pet().displayHealth()
