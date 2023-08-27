# Day 28: Python Excpetion Handling

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/ha9l-6UUBeo
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Exception Handling in Python

Exception handling is a method used to manage runtime errors in your Python code. It prevents your program from crashing due to unexpected issues. In Python, the 'try' and 'except' statements are used for handling exceptions.

The 'try' block contains the code that might throw an exception. If an exception occurs, the 'except' block, which contains the code to handle the exception, is executed.

You can also use the 'else' block to specify code that should be executed if no exception occurs in the 'try' block. Additionally, the 'finally' block is used to specify code that should be executed regardless of whether an exception occurs or not.

## Example of Exception Handling in Python

Consider the following example where the function 'divide' attempts to divide 'a' by 'b'. It handles a ZeroDivisionError if it occurs. If no exception occurs, the 'else' block is executed, and the result is printed. The 'finally' block is always executed, regardless of whether an exception occurs or not.

```python
def divide(a, b):
    try:
        result = a / b 
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"Result: {result}")
    finally:
        print("Division finished.")

divide(4, 2)  
# Output: 
# "Result: 2.0" 
# "Division finished."

divide(4, 0)  
# Output: 
# "Cannot divide by zero!" 
# "Division finished."
```

In the above code, the 'try' block attempts to divide 'a' by 'b'. If 'b' is zero, a ZeroDivisionError is thrown, and the 'except' block is executed, printing "Cannot divide by zero!". If 'b' is not zero, the 'else' block is executed, printing the result of the division. Regardless of the outcome, the 'finally' block is always executed, printing "Division finished.".

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