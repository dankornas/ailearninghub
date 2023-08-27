# Day 22: Python Inheritance

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/QlLoXIRjGRk
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Python Inheritance and Subclasses

In Python, inheritance is a fundamental concept that allows the creation of a new class, known as a subclass, from an existing class, referred to as the superclass. This mechanism enables the subclass to inherit and utilize the attributes and methods of the superclass, while also having the flexibility to introduce specific attributes and methods of its own.

To create a subclass in Python, the 'class' keyword is used, followed by the subclass name. The superclass name is then passed as an argument within parentheses. The attributes and methods of the subclass are defined in an indented block underneath the class definition.

The 'super()' function plays a crucial role in Python inheritance. It is used within a subclass to call the methods of the superclass, thereby promoting code reusability. This function also allows the subclass to modify the inherited methods as needed, providing a high degree of flexibility in class design.

## Implementing Inheritance in Python

```python
class Animal:
    def __init__(self, name, species): 
        self.name = name 
        self.species = species 

    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed 
        super().__init__(name, species="Dog") 

    def make_sound(self):
        print("Woof!")

dog = Dog("Buddy", "Poodle")
print(dog.name)  # Output: "Buddy"
print(dog.species)  # Output: "Dog"
print(dog.breed)  # Output: "Poodle"
dog.make_sound()  # Output: "Woof!"
```

In the above example, 'Animal' is the superclass, and 'Dog' is the subclass. The 'Dog' subclass inherits the attributes and methods of the 'Animal' superclass and introduces a new attribute 'breed'. The 'make_sound' method is overridden in the 'Dog' subclass to print "Woof!" instead of "Some generic animal sound". The 'super()' function is used in the 'Dog' subclass to call the '**init**' method of the 'Animal' superclass.

!!! info "Learn More"

    Want to learn more about Python for Machine Learning? Check out the full course [HERE](/ai-roadmap/programming/python/data-types/).

---

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