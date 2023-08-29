---
description: Something
---

# Day 20: Accessing Python Class Object Attributes

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/HzhLohqXtIc
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding the 'self' Keyword in Python Classes

In Python classes, the 'self' keyword is used to access the attributes and methods of an object from within the object's class. It refers to the instance of the class and is used to distinguish the instance's attributes and methods from those of the class itself.

To access the attributes of an object from within the class, use the 'self' keyword followed by the attribute name. Similarly, to access the methods of an object from within the class, use the 'self' keyword followed by the method name.

## Accessing Attributes and Methods with 'self' in Python Classes

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    def bark(self):
        print("Woof!") 

    def show_info(self):
        # Accessing attributes with 'self'
        print(f"Name: {self.name} Breed: {self.breed}") 

dog = Dog("Fido", "Labrador")
dog.show_info() 
# Output: "Name: Fido Breed: Labrador"
```

In the above example, the 'show_info' method uses the 'self' keyword to access the 'name' and 'breed' attributes of the 'Dog' instance.

## Using 'self' to Access Methods in Python Classes

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    def bark(self):
        print("Woof!")

    def show_info(self):
        print(f"Name: {self.name} Breed: {self.breed}") 

    def do_bark(self):
        # Accessing method with 'self'
        self.bark()
        print("Barking!")

dog = Dog("Buddy", "Poodle")
dog.do_bark()  # Output: "Woof! Barking!"
```

In this example, the 'do_bark' method uses the 'self' keyword to call the 'bark' method of the 'Dog' instance.

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