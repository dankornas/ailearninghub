# Day 23: Python Polymorphism

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/CvQ1d5saQr8
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Polymorphism in Python

Polymorphism is a fundamental concept in object-oriented programming that allows you to use the same interface for different underlying forms or data types. In Python, polymorphism enables us to define methods in the child class with the same name as defined in their parent class. As the name suggests, a child class inherits methods and attributes from the parent class. However, it is free to override the methods according to its requirements.

In essence, polymorphism grants the ability to use a single type entity (method, operator or object) to represent different types in different scenarios. It's the characteristic of an entity to behave in multiple forms.

## Implementing Polymorphism through Inheritance and Overriding

In Python, we can achieve polymorphism using inheritance and method overriding. We define a superclass with a method that we want to override in the subclass. Then, we define the subclass that inherits from the superclass and override the method with a new implementation.

For instance, consider an `Animal` class with a `make_sound` method. This method is then overridden in the `Dog` and `Cat` subclasses. When you create an instance of the `Dog` class, it will make a "Woof!" sound, and when you create an instance of the `Cat` class, it will make a "Meow!" sound.

```python
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()

# Output: "Woof!" "Meow!"
```

In the above code, `Dog` and `Cat` classes override the `make_sound` method of the `Animal` class. Hence, when we iterate over the `animals` list and call `make_sound`, the respective class's method is invoked, demonstrating polymorphism.

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