import copy


class Prototype:

    def __init__(self):
        """Create a dictionary object that contains the objects to be cloned"""
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and its attributes"""
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


class Airplane:
    def __init__(self):
        self.name = "Airbus"
        self.color = "White"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


# create Car and Airplane instances
car = Car()
airplane = Airplane()
# create Prototype instance
prototype = Prototype()
# register an object
prototype.register_object('skylark', car)
prototype.register_object('airbus', airplane)
# clone object with changed 'color' attribute
cloned_car = prototype.clone(name='skylark', color='Black', options='Ex')
# clone object without changed attributes
cloned_airplane = prototype.clone(name='airbus')

print(cloned_car)
print(cloned_airplane)
