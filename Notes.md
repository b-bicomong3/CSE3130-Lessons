// Notes.md

# Object-Oriented Programming 2 Notes

### Inheritance

Inheritance si the process where one class inherits attributes and methods from another class. While some languages such
as Java prohibit it, classes can inherit from multiple parents classes. However, this process of multiple inheritances
if often avoided because of potential conflicts from duplicates attributes and method name.

* Inheritance describes an Is-A relationship.
    * The _deck_ __is a__ _group of cards_ and the _hand_ __is a__ _group of cards_, but the _deck_ is not a _hand_.
      Therefore, a _deck_ and _hand_ can both inherit from a _group of cards_.
        * __Abstract Classes__ (as opposed to concrete classes) are classes that are never instantiated by themselves.
          These classes are written solely for the purpose of inheritance. Often times these classes have __abstract
          methods__ which cannot fully function within the Abstract Class; instead they rely on data in their respective
          subclasses.
        * Inheritance often reveals itself during the design process when multiple classes have similar attributes or
          methods.

```python
class Mammal:  # abstract class
    def __init__(self, genus, species, name):
        self.genus = genus
        self.species = species
        self.name = name

    def setCry(self, sound):
        self.crySound = sound

    def Cry(self):
        return self.crySound


class Dog(Mammal):  # concrete child class
    def __init__(self, genus, species, name="Rover"):
        Mammal.__init__(genus, species, name)
        self.setCry("Borf")


class Cat(Mammal):  # concrete child class
    def __init__(self, genus, species, name):
        Mammal.__init__(genus, species, name)
        self.setCry("Meow")


PYRENESS = Dog("Canis", "Lupis", "Bond")
BOMBAY = Cat("Felis", "Catis", "Ben")

PYRENESS.Cry()  # return Borf
BOMBAY.Cry()  # return Meow
```

## Polymorphism

Polymorphism is the ability to have the same methods in the different classes perform different tasks/outcomes

```python
# Use classes from above
PYRENESS.Cry()  # "Borf"
BOMBAY.Cry()  # "Meow"
```
Note the both objects have the same method, but have different output.