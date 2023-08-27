# Day 9: Python Scopes

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/CCq0TOlPWlg
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Scopes in Python

In Python, variables are defined by their scope, which determines where they can be accessed within the code. There are two primary types of scope: global and local. Global variables are defined outside of any function and can be accessed from anywhere within the code. Conversely, local variables are defined within a function and can only be accessed from within that specific function.

## Global Variables in Python

```python
x = 5  # This is a global variable

def func():
    # The global variable x can be accessed from within this function
    print(x)

func()  # This will output: 5
```

In the above example, `x` is a global variable. It is defined outside of any function and can be accessed from anywhere within the code, including inside the function `func()`.

## Local Variables in Python

```python
def func():
    x = 5  # This is a local variable
    print(x)

func()  # This will output: 5
```

In this example, `x` is a local variable. It is defined within the function `func()` and can only be accessed from within that function. Attempting to print `x` outside of the function would result in an error, as `x` is not defined in that scope.

```python
# This will cause an error, because x is not defined outside of the function
print(x)
```

By understanding the difference between global and local variable scope in Python, you can write more efficient and error-free code.

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
