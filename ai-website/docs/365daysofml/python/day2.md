# Day 2: Python Syntax

<iframe width="360" height="655" src="https://youtube.com/embed/FxxF2NhwWmE?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Python, known for its simplicity and readability, is an excellent programming language for beginners.

## Indentation

In Python, indentation is used to denote blocks of code, which are groups of statements executed together. The standard indentation is four spaces. Let's see an example:

```python
x = 10
if x > 5:
    # This line is indented
    print("x is greater than 5") 
    # This line is also indented
    print("This line is also indented") 
# This line is not indented
print("This line is not indented") 
```

## Comments

Comments, starting with a hashtag symbol, are used to explain the code, enhancing its understandability. Everything after the hashtag symbol is ignored by the interpreter. Here's how you can use comments in your code:

```python
# This is a comment
x = 10 # This is also a comment
```

## Statements and Variables

A statement, a line of code that performs a specific task, and a variable, a named location in memory that stores a value, are fundamental concepts in Python. Here are some examples of statements and variables:

```python
x = 10
y = 20
z = 30

# Multiple statements on the same line
x = 10; y = 20; z = 30

x = 10
y = "Hello"
z = True

# Valid variable names
my_variable = 10
_private_variable = 20

# Invalid variable names
# 10_invalid = 10 (starts with a digit)
# invalid-variable = 20 (contains a hyphen)
```

## Data Types

Python has several built-in data types, including integers, floats, strings, and booleans. Here are some examples:

```python
# Integer
x = 10

# Float
y = 10.5

# String
z = "Hello"

# Boolean
flag = True

# And much more ...
```

## Operators

Operators are special symbols that perform operations on values, such as arithmetic, assignment, and comparison. Here's how you can use operators in your code:

```python
# Arithmetic operators
x = 10
y = 20
z = x + y # z = 30
z = x - y # z = -10
z = x * y # z = 200
z = x / y # z = 0.5
z = x % y # z = 10

# Assignment operators
x = 10
x += 5 # x = 15
x -= 5 # x = 10
x *= 5 # x = 50
x /= 5 # x = 10

# Comparison operators
x = 10
y = 20
z = x == y # z = False
z = x != y # z = True
z = x < y # z = True
z = x > y # z = False
z = x <= y # z = True
z = x >= y # z = False

# And much more ...
```

## Functions

A function is a block of code that performs a specific task. Here's how you can define and use functions in your code:

```python
# Define a function
def greet(name):
    print("Hello, " + name)

# Call the function
greet("John") # Prints "Hello, John"

# Use a built-in function
x = min(10, 20) # x = 10
```

## Modules

A module is a collection of related functions and variables that can be imported into a program. Here's how you can use modules in your code:

```python
# Import a built-in module
import math

# Use a function from the module
x = math.sqrt(25) # x = 5.0

# Create a custom module
# my_module.py
def greet(name):
    print("Hello, " + name)

# Use the custom module
# main.py
import my_module
my_module.greet("John") # Prints "Hello, John"
```

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
