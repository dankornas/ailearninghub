# Day 27: Python Data Classes

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/pkE2rMAwrgY
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Python Data Classes: Simplifying Data Storage

Python data classes are a modern feature that streamline the creation of classes specifically designed for storing data. Essentially, a class serves as a blueprint for generating objects, and data classes are a specialized type of class tailored for data storage.

For instance, if you're developing a program to record people's names and ages, data classes can be incredibly useful. You could establish a class named 'Person' with two fields: one for the name and another for the age. Consequently, you can generate multiple instances of the 'Person' class, each with a unique name and age.

## Implementing Data Classes in Python

```python
from dataclasses import dataclass 

@dataclass 
class Person: 
    name: str 
    age: int 

p1 = Person("John", 30)
print(p1)
```

In the above code snippet, we import the 'dataclass' decorator from the 'dataclasses' module. We then define a 'Person' class with 'name' and 'age' as its fields. The '@dataclass' decorator above the class definition indicates that 'Person' is a data class. Finally, we create an instance of the 'Person' class and print it.

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