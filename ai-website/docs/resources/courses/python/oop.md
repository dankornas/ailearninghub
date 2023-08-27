---
title: Object-Oriented Programming
hide:
  - path
  - navigation
---

# Python: Object-Oriented Programming

## **Object-Oriented Programming in Python for Machine Learning**

As the world of machine learning continues to evolve, the need for structured and scalable code becomes ever more paramount. Enter Object-Oriented Programming (OOP) – a programming paradigm that revolves around the concept of objects and classes. Python, with its clear syntax and OOP support, stands as an ideal language for integrating machine learning with OOP principles. In this tutorial, we'll demystify the core concepts of OOP in Python, setting the stage for you to build robust and maintainable machine learning applications.

* * *

## **Classes / Objects**

At the heart of OOP lie classes and objects. A class defines a blueprint for creating objects, encapsulating data for the object and methods to manipulate that data.

### **Defining a Class**

Here's how you can create a simple class named `Person`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### **Creating Objects**

Once a class is defined, you can create objects (or instances) of that class:

```python
person1 = Person("John", 30)
print(person1.name)  # Outputs: John
```

* * *

## **Getters / Setters**

In OOP, it's often desirable to hide the internal representation of an object and only show the necessary attributes. Getters and setters allow you to define methods to get and set the values of private attributes.

### **Using Getters**

The `@property` decorator is used to create getter methods:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

### **Using Setters**

The `@<attribute>.setter` decorator is used to create setter methods:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
```

* * *

## **Inheritance & Polymorphism**

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). Polymorphism allows objects of different classes to be treated as objects of a common super class.

### **Inheritance**

Here's a basic example showcasing inheritance:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

student1 = Student("Alice", "S12345")
student1.greet()  # Outputs: Hello, Alice!
student1.study()  # Outputs: Alice is studying.
```

### **Polymorphism**

Polymorphism is exemplified when we have multiple classes with the same method names, allowing for a unified interface.

```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def animal_sound(animal):
    print(animal.speak())

my_cat = Cat()
my_dog = Dog()

animal_sound(my_cat)  # Outputs: Meow
animal_sound(my_dog)  # Outputs: Woof
```

* * *

## **Magic Methods**

Magic methods (or dunder methods) in Python are special methods with double underscores at the beginning and end of their names. They allow customization of fundamental object behaviors.

### **Example: __str__ and __repr__**

The `__str__` and `__repr__` methods allow you to define human-readable and unambiguous representations of objects, respectively.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person1 = Person("John", 30)
print(str(person1))  # Outputs: John, 30 years old
print(repr(person1))  # Outputs: Person('John', 30)
```

* * *

## **Conclusion**

Object-Oriented Programming in Python offers a structured approach to coding, making the development of machine learning applications more organized and manageable. By understanding classes, objects, inheritance, polymorphism, and magic methods, you unlock the potential to design scalable and efficient machine learning solutions. As you delve deeper into the world of Python and machine learning, these OOP principles will serve as invaluable pillars, guiding you towards coding excellence. Dive in, experiment, and embrace the power of OOP in Python for machine learning.


---

!!! note "Version 1.0"

    This is currently an early version of the learning material and it will be updated over time with more detailed information.

    A video will be provided with the learning material as well.

    Be sure to subscribe to stay up-to-date with the latest updates.

<div style="padding: 20px; color: white; background-color: #0f1624; border-radius: 10px; margin: 10px 0 20px 0; text-align: center;">
    <h2 style="color: white;">Need help mastering Machine Learning?</h2>
    <p style="font-size: 16px;">Don't just follow along — join me!
    Get exclusive access to me, your instructor, who can help answer any of your questions. Additionally, get access to a private learning group where you can learn together and support each other on your AI journey.
    </p><br>
    <div style="text-align: center; margin-bottom: 20px;">
        <button style="display: inline-block; padding: 10px 20px; font-size: 20px; color: white; background: #1018A8; border: none; border-radius: 5px;">
            <a href="/subscribe" style="color: white; text-decoration: none;">Subscribe Now</a>
        </button>
    </div>
</div>