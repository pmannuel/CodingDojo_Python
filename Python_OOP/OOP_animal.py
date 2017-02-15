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
        print 'name: {} \nhealth: {}'.format(self.name,self.health)

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)

    def displayHealth(self):
        print "I am a dragon! Rawr!"
        super(Dragon, self).displayHealth()

penguinsaurus = Animal("penguinsaurus")
penguinsaurus.walk().walk().walk().run().run().displayHealth()

print '\n'

mastermind = Dog("mastermind")
mastermind.walk().walk().walk().run().run().pet().displayHealth()

print '\n'

dragon = Dragon("dragon")
dragon.walk().walk().walk().run().run().displayHealth()
