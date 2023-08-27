# Day 7: Python Functions

<iframe width="360" height="655" src="https://www.youtube.com/embed/8n6NWvFqkcs?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Functions in Python

Functions in Python are defined blocks of code that can be invoked by their specific names. They serve as a crucial tool for organizing and reusing code, enhancing the efficiency of your programming. To define a function in Python, the 'def' keyword is utilized, followed by the function name and a set of parentheses. These parentheses may encompass parameters as required. The code block within the function is indented for clarity and structure. Moreover, Python functions can return a value using the 'return' keyword, further expanding their utility.

## Defining a Function in Python

```python
# Define a function
def greet(name):
    print("Hello, " + name)
```

In the above example, we have defined a function named 'greet'. This function takes one parameter, 'name', and prints a greeting message. To call this function, we simply use its name followed by the argument in parentheses:

```python
greet("John")  # Output: "Hello, John"
```

## Returning a Value from a Python Function

```python
# Return a value from a function
def add(x, y):
    return x + y
```

In this example, we have a function named 'add' that takes two parameters, 'x' and 'y'. The function returns the sum of these two parameters. To use this function and store the returned value, we assign the function call to a variable:

```python
result = add(3, 4)  # Output: 7
```

In this case, 'result' will hold the value returned by the 'add' function, which is the sum of the arguments passed.

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
