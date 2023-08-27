# Day 24: Python Decorators

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/ReyPju06g8E
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Python Decorators

Decorators in Python are a powerful and flexible feature that allow you to modify the behavior of a function without altering its source code. They are defined using the '@' symbol followed by the name of the decorator function.

To define a decorator function, use the 'def' keyword followed by the function name and any required parameters. Then, define the function that will modify the behavior of the decorated function.

In the following example, the 'uppercase' decorator function takes a function as an argument and returns a wrapper function. This wrapper function calls the original function and modifies its result.

The 'greet' function is decorated with the '@uppercase' decorator, which means that it will be passed to the 'uppercase' decorator. The wrapper function returned by the decorator will then be used in place of the original 'greet' function.

## Python Decorator Example

```python
def uppercase(func):
    def wrapper():
        original_result = func() 
        modified_result = original_result.upper() 
        return modified_result 
    return wrapper 

@uppercase 
def greet():
    return "hello" 

print(greet())  # Output: "HELLO"
```

In this example, the 'greet' function returns the string "hello". However, because it is decorated with the '@uppercase' decorator, the output is modified to "HELLO".

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