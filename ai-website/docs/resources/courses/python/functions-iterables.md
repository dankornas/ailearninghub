---
title: Functions & Iterables
hide:
  - path
  - navigation
---

# Python: Functions & Iterables

## **Functions**

Functions are reusable blocks of code that perform specific tasks. They can accept inputs, process them, and return results.

### **Defining a Function**

A function is defined using the `def` keyword, followed by a name and a set of parentheses.

```python
def greet():
    print("Hello, World!")
```

### **Function Parameters**

Functions can accept parameters, which are values you pass into the function for processing.

```python
def greet(name):
    print(f"Hello, {name}!")
```

### **Return Values**

Functions can return values using the `return` statement.

```python
def add(x, y):
    return x + y
```

* * *

## **Lambda (Anonymous Function)**

Lambda functions are small, unnamed functions defined using the `lambda` keyword. They are used for creating quick, throwaway functions without the need for a full `def` block.

### **Basic Usage**

A lambda function to add two numbers:

```python
add = lambda x, y: x + y
print(add(5, 3))  # Outputs 8
```

* * *

## **Map**

The `map` function applies a function to all items in the given iterable, such as a list or tuple.

### **Using Map with Functions**

```python
def square(n):
    return n * n

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Outputs [1, 4, 9, 16]
```

### **Using Map with Lambda**

```python
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x*x, numbers)
print(list(squared_numbers))  # Outputs [1, 4, 9, 16]
```

* * *

## **Filter**

The `filter` function filters the elements from an iterable based on a function that returns either `True` or `False`.

### **Filtering with Functions**

```python
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Outputs [2, 4, 6]
```

### **Filtering with Lambda**

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Outputs [2, 4, 6]
```

* * *

## **Reduce**

The `reduce` function successively applies a function to elements of an iterable, reducing the iterable to a single accumulated result.

### **Using Reduce**

To use `reduce`, you need to import it from the `functools` module.

```python
from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)
print(product)  # Outputs 24
```

* * *

## **Iterators**

Iterators are objects that can be iterated upon. They implement two methods, `__iter__()` and `__next__()`, allowing you to loop through items using a `for` loop or the `next` function.

### **Creating an Iterator**

Here's an example of a simple iterator that returns numbers:

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

numbers = MyNumbers()
iterable = iter(numbers)

print(next(iterable))  # Outputs 1
print(next(iterable))  # Outputs 2
```

* * *

## **Ranges**

The `range` function generates a sequence of numbers. It's particularly useful in loops when you want to iterate a specific number of times.

### **Using Range**

```python
for i in range(5):
    print(i)  # Outputs 0, 1, 2, 3, 4
```

### **Range with Start, Stop, and Step**

You can also define a start, stop, and step for the `range`:

```python
for i in range(2, 10, 2):
    print(i)  # Outputs 2, 4, 6, 8
```

* * *

## **Conclusion**

Python's support for functions and iterables is a testament to its power and flexibility. As you venture deeper into machine learning, you'll find these tools indispensable in crafting efficient algorithms, preprocessing data, and much more. With functions, lambda expressions, and iterables in your arsenal, you're well on your way to mastering the intricacies of machine learning with Python. Dive in, experiment, and watch your machine learning projects come to life.


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