# Day 25: Python OOP - Class & Static Methods

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/1eYsKuMzKEI
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Class Methods and Static Methods in Python

In Python, class methods and static methods are decorators that allow you to define methods that operate at the class or object level, rather than at the instance level.

A class method is a method that operates on the class itself and is not bound to any specific instance. It is defined using the `@classmethod` decorator and takes the `cls` parameter, which refers to the class itself.

On the other hand, a static method is a method that is not bound to either the instance or the class. It does not have access to any class or instance attributes. It is defined using the `@staticmethod` decorator and does not take any special parameters.

## Defining a Class Method in Python

To define a class method, use the `@classmethod` decorator and provide the method with the `cls` parameter. This parameter refers to the class itself and allows the method to modify class-specific details.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    @classmethod 
    def create_dog(cls, name, breed):
        return cls(name, breed) 
```

In the above example, `create_dog` is a class method that creates a new instance of the `Dog` class.

## Defining a Static Method in Python

To define a static method, use the `@staticmethod` decorator. Unlike class methods and regular methods, static methods do not take a `self` or `cls` parameter. This means they cannot modify the instance or the class, making them independent.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    @staticmethod 
    def bark():
        print("Woof!") 
```

In this example, `bark` is a static method that prints "Woof!" to the console. It does not interact with any class or instance attributes.

```python
dog = Dog.create_dog("Buddy", "Poodle")
print(dog.name)  # Output: "Buddy"
print(dog.breed)  # Output: "Poodle"

Dog.bark()  # Output: "Woof!"
```

In the final example, we create a new `Dog` instance using the class method `create_dog` and call the static method `bark` on the `Dog` class.

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
            <a href="/subscribetext-decoration: none;">Subscribe Now</a>
        </button>
    </div>
</div>