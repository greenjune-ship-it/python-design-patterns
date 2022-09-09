# Python: Design Patterns

This repository contains learning notes about ready-to-use patterns examples written in Python

## List of Content

### Creatinal Patterns:

* `factory.py` method pattern is a creational pattern that uses factory methods to deal with the problem of creating objects without having to specify the exact class of the object that will be created
* `abstract-factory.py` design pattern is interface to create families of related objects without specifying their concrete classes
* `singleton.py` this pattern involves a single class which is responsible to create an object while making sure that only single object gets created
* `builder_animals.py, builder_cars.py` the intent of the **builder design pattern** is to separate the construction of a complex object from its representation
* `prototype.py` is used when the type of objects to create is determined by a prototypical instance, which is cloned to produce new objects

### Structural Patterns

* `decorator.py` pattern allows a user to add new functionality to an existing object without altering its structure
* `proxy.py` pattern allows to create a class that represents functionality of another class (the object having original object to interface its functionality to outer world)
* `adapter.py` pattern is a software design pattern (also known as wrapper, an alternative naming shared with the decorator pattern) that allows the interface of an existing class to be used as another interface
* `composite.py` pattern describes a group of objects that are treated the same way as a single instance of the same type of object
* `bridge.py` pattern involves an interface which acts as a bridge which makes the functionality of concrete classes independent from interface implementer classes

### Behavioral Patterns
* `observer.py` is a software design pattern in which an object, named the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods
* `visitor.py` design pattern is a way of separating an algorithm from an object structure on which it operates. A practical result of this separation is the ability to add new operations to existing object structures without modifying the structures
* `iterator.py` is used to traverse a container and access the container's elements
* `strategy.py` enables selecting an algorithm at runtime. Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use
* `chain.py` pattern is recommended when multiple objects can handle a request and the handler doesn't have to be a specific object
* 