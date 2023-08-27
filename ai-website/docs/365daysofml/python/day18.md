# Day 18: Defining Python Classes

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/uEBYrcr3_L4
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Python Classes

In Python, classes are user-defined templates or blueprints that encapsulate data and functions into a single entity. They are defined using the 'class' keyword, followed by the class name and a colon. The attributes and methods of the class are defined in an indented block under the class definition.

The `__init__` method is a special method in Python, known as a constructor. This method is automatically called when an instance of the class is created, and it is used to initialize the attributes of the instance. The 'self' keyword refers to the instance of the class and is used to access the attributes and methods of the instance from within the class.

Additional methods can be defined in the class by writing functions inside the class. These methods can operate on the attributes of the instance, providing the functionality associated with the class.

## Defining a Class in Python
```python
class Dog:
    # Class attribute
    species = "mammal"

    # Initializer method
    def __init__(self, name, breed):
        # Instance attributes
        self.name = name 
        self.breed = breed 

    # Method
    def bark(self):
        print("Woof!") 
```

In the above example, a class named 'Dog' is defined with a class attribute 'species', two instance attributes 'name' and 'breed', and a method 'bark'.

## Adding Additional Methods to a Class

Additional methods can be added to the class to provide more functionality. For example, a method 'bark_loudly' can be added to the 'Dog' class as follows:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    def bark(self):
        print("Woof!") 

    def bark_loudly(self):
        print("WOOF!") 

dog = Dog("Fido", "Labrador")
dog.bark()  # Output: "Woof!"
dog.bark_loudly()  # Output: "WOOF!"
```

In this example, the 'bark_loudly' method is called on an instance of the 'Dog' class, and it prints "WOOF!" to the console.


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