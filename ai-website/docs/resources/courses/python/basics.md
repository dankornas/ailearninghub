---
title: Basics
hide:
  - path
  - navigation
---

# Python: Basics

## **Variables**

In programming, a variable is like a container that stores data values. Think of it as a labeled box, where the label is the variable name, and the content inside is the data value.

In Python, creating a variable is straightforward:

```python
x = 10
name = "Alice"
```

Here, `x` is a variable storing the integer value 10, and `name` stores the string "Alice".

* * *

## **Data Types**

Python has various data types, and it's essential to understand the most common ones:

* **Integers**: Whole numbers, either positive or negative.
    
    ```python
    age = 25
    ```
    
* **Floats**: Numbers with a decimal point.
    
    ```python
    height = 5.9
    ```
    
* **Strings**: Sequence of characters, enclosed within single or double quotes.
    
    ```python
    greeting = "Hello, World!"
    ```
    
* **Booleans**: Represents either True or False.
    
    ```python
    is_student = False
    ```
    

* * *

## **Casting**

Sometimes, you might want to change the data type of a value. This process is called casting. Python provides built-in functions to perform casting:

* `int()`: Converts a value to an integer.
* `float()`: Converts a value to a float.
* `str()`: Converts a value to a string.

For example:

```python
x = 5.5
y = int(x)  # y will be 5
```

* * *

**Output**

Displaying output in Python is done using the `print()` function:

```python
print("Hello, World!")
```

You can also combine strings and variables:

```python
name = "Anna"
print("Hello, " + name + "!")
```

* * *

## **Math**

Python offers a variety of mathematical operations that can be performed on numbers:

* **Addition** (`+`): `5 + 3` will return 8.
* **Subtraction** (`-`): `5 - 3` will return 2.
* **Multiplication** (`*`): `5 * 3` will return 15.
* **Division** (`/`): `5 / 3` will return approximately 1.6667.

For more advanced mathematical functions, Python has a built-in module called `math`:

```python
import math
result = math.sqrt(25)  # returns 5.0
```

* * *

## **Random Values**

Generating random numbers is crucial in many applications, including machine learning. The `random` module in Python provides functions to generate random values:

```python
import random
random_number = random.randint(1, 10)  # generates a random integer between 1 and 10
```

* * *

## **Nan & Inf**

In Python, `NaN` stands for "Not a Number" and represents undefined or unrepresentable values. `Inf` denotes infinity, a value that's larger than any number.

These values can be encountered in computations, especially in the context of data science and machine learning:

```python
import numpy as np

# Creating NaN and Inf values
x = np.nan
y = np.inf

print(x)  # Outputs: nan
print(y)  # Outputs: inf
```

* * *

**Conclusion**

Mastering the basics of Python is the first step towards a successful journey in machine learning. With its intuitive syntax and robust features, Python offers a seamless experience for beginners and professionals alike. As you progress, you'll find Python's versatility and power indispensable in your machine learning projects. Dive in, explore, and let Python be your guide in the captivating world of machine learning.

---

!!! note "Version 1.0"

    This is currently an early version of the learning material and it will be updated over time with more detailed information.

    A video will be provided with the learning material as well.

    Be sure to subscribe to stay up-to-date with the latest updates.

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