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

In complex programs, polymorphism is often used to adjust inherited methods to better suit the subclass's need.

## Public, Private, and Partially-Protected Class Members

Classical object-oriented languages. such as C++ and Java, control the access to class resources (i.e. attributes and
methods) by public, private and protected keywords. Private members of the class are denied access from outside the
class. These attributes and methods are only handled within the object created from the class. (In python, Privated is
called Protected). Controlled access to members within a class increases class integrity by only allowing to certain
members externally (encapsulation)

While some languages, like java, default class members to private, Python defaults class members to private.

__Public Members__ are accessible outside the Class. In Python, all members not starting with an underscore are public.

__Private Members__ are only available within the class. They are denoted with a double underscore at the beginning of
the member name. Private Members are nto accessible outside the class. In Python, private members are called protected.

__Protected Members__ are available to the class and its subclasses without the need for a public method. They are
denoted with a single underscore at the beginning of the member name. In Python, protected members are still accessible
outside the class. In addition, Python calls this partially protected members.

```python
class MyClass:
    def __init__(self):
        self.FIRST_NAME = "Michael"  # Public
        self.LAST_NAME = "Zhang"  # Paritally Protected
        self.__MID__INIT = "A"  # Private

    def _protectedMethod(self):
        return

    def __privateMethods(self):
        return


class subClass(MyClass):
    def __init__(self):
        super().__init__()

    def newMethod(self):
        super()._protectedMethod()  # The __privateMethod would not work.
```
