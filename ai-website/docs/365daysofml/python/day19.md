# Day 19: Creating Python Class Objects

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/o0wQBRK5rjk
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding the **init** Method in Python

The `__init__` method in Python is a special method known as a constructor. It is utilized to initialize the attributes of an object at the time of its creation. To define the `__init__` method, it should be written inside a class and given the 'self' parameter.

The 'self' parameter refers to the instances of the class and is used to access the attributes and methods of the instance from within the class. The `__init__` method is automatically invoked when you create an instance of the class using the class name syntax.

You can pass arguments to the `__init__` method to initialize attributes of the instance.

## Defining the **init** Method in a Class

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    def bark(self):
        print("Woof!") 

# Create an instance of the Dog class 
# and initialize its attributes
dog = Dog("Fido", "Labrador")
print(dog.name)  # Output: "Fido"
print(dog.breed)  # Output: "Labrador"
```

In the above example, the `__init__` method is defined within the 'Dog' class. It takes 'self', 'name', and 'breed' as parameters. When an instance of the 'Dog' class is created, the `__init__` method is automatically called, initializing the 'name' and 'breed' attributes of the instance.

## Passing Arguments to the **init** Method

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    def bark(self):
        print("Woof!") 

# Create an instance of the Dog class 
# and initialize its attributes
dog = Dog("Buddy", "Poodle")
print(dog.name)  # Output: "Buddy"
print(dog.breed)  # Output: "Poodle"
```

In this example, arguments "Buddy" and "Poodle" are passed to the `__init__` method when creating a new instance of the 'Dog' class. These arguments are used to initialize the 'name' and 'breed' attributes of the instance.

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