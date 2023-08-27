# Day 17: Python Object Oriented Programming

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/kp3ZsAE7LGU
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a programming paradigm that utilizes objects to represent data and the corresponding methods that operate on that data. It provides a structured approach to organizing and structuring your code, making it easier to understand, maintain, and extend. In Python, you can define a class to create an object. A class serves as a blueprint for an object, encompassing its attributes (data) and methods (functions).

## Defining a Class

Now, let's apply this concept using a simple example:

```python
# Defining the Dog Class
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    # Defining the bark method
    def bark(self):
        print("Woof!") 
```

In the above code, we've defined a `Dog` class with attributes `name` and `breed`, and a method `bark`.

## Creating an Instance of a Class

Now, let's create an instance of the `Dog` class:

```python
# Creating an Instance of the Dog Class
dog = Dog("Fido", "Labrador")
print(dog.name)  # Output: "Fido"
print(dog.breed)  # Output: "Labrador"
dog.bark()  # Output: "Woof!"
```

In this section, we've created a `Dog` object named `Fido` of breed `Labrador`. We then accessed its attributes and called the `bark` method. This example illustrates the fundamental principles of Object-Oriented Programming in Python.

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