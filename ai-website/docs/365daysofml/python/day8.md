# Day 8: Python Arguments & Parameters

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/sPfOzBYE29Q
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Function Parameters and Arguments in Python

In Python, when calling a function, you can pass values to the function as arguments. These values are then received by the function as parameters. You can also specify default values for parameters in the function definition. If an argument is not provided when the function is called, the default value will be used. In this context, the value that is being passed into the function is the argument, while the parameter is the variable that receives this value.

## Function Parameters and Arguments in Python

```python
# Argument and Parameters
def greet(name):
    print("Hello, " + name)

greet("John")  
```

In the above example, "John" is the argument, and "name" is the parameter.

## Specifying Default Values for Parameters in Python

You can specify default values for parameters in the function definition. This means that if an argument is not provided when the function is called, the default value will be used.

```python
# Specify default values for parameters in the function
def greet(name="Guest"):
    print("Hello, " + name)

greet()  # Output: "Hello, Guest"
greet("John")  # Output: "Hello, John"
```

In the above example, if no argument is passed to the `greet` function, it uses the default value "Guest" for the `name` parameter.

Understanding the difference between parameters and arguments, and how to use them in Python functions, can help you write more efficient and readable code. Stay tuned for more Python-related content.

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
