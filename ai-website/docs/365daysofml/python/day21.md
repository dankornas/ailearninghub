# Day 21: Modifying Python Class Object Attributes

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/sfgufcP7Svw
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Modifying Object Attributes in Python

In Python, you can modify the attributes of an object by defining methods within the object's class that operate on the object's attributes. To define a method that modifies an attribute, you write a function inside the class and use the 'self' keyword to access the attribute.

For instance, consider a 'Dog' class where each dog object has a 'name' and 'breed' attribute. Initially, we name our dog 'Fido'. However, with the 'set_name' method, we can change the name of the dog to 'Buddy'.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    def set_name(self, name):
        self.name = name 

dog = Dog("Fido", "Labrador")
print(dog.name)  
# Output: "Fido"

dog.set_name("Buddy")
print(dog.name)  
# Output: "Buddy"
```

In a similar manner, you can define a method that updates multiple attributes at once. In the following example, the 'update_info' method updates both the 'name' and 'breed' attributes of the dog object.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    def update_info(self, name, breed):
        self.name = name 
        self.breed = breed 

dog = Dog("Fido", "Labrador")
print(f"Name:{dog.name} Breed:{dog.breed}") 
# Output: "Name: Fido Breed: Labrador"

dog.update_info("Buddy", "Poodle")
print(f"Name:{dog.name} Breed:{dog.breed}")  
# Output: "Name: Buddy Breed: Poodle"
```

This way, you can effectively change object attribute Python-style, providing flexibility and control over your object instances.

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