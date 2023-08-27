---
title: Control Flow
hide:
  - path
  - navigation
---

# Python: Control Flow

## **What is Control Flow in Python?**

Control flow refers to the order in which the program's instructions are executed. By manipulating this order, we can make our programs more dynamic, allowing them to react to inputs or changing conditions. In this tutorial, we'll delve deep into Python's control flow tools, ensuring you're well-equipped to build efficient machine learning models.

* * *

## **Conditionals: If/Elif**

Conditionals are the bedrock of decision-making in programming. By evaluating certain conditions, Python can decide which block of code to execute.

### **The `if` Statement**

The simplest form of conditionals is the `if` statement. It checks a condition and, if it's true, executes the code inside its block.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### **Adding `else`**

An `else` statement can be combined with an `if` statement to provide an alternative block of code if the condition is false.

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

### **The `elif` Statement**

For more than two possible conditions, the `elif` (else-if) statement comes into play. It allows for multiple conditions to be checked in sequence.

```python
x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 10 and not equal to 5")
```

* * *

## **While Loop**

The `while` loop repeatedly executes a block of code as long as a condition remains true. It's essential for tasks that require repeated execution until a certain condition is met.

### **Basic Usage**

Here's a simple `while` loop that counts from 1 to 5:

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### **Using `break`**

Sometimes, you might want to exit the loop prematurely when a certain condition is met. The `break` statement allows for this.

```python
count = 1
while count <= 10:
    if count == 6:
        break
    print(count)
    count += 1
```

* * *

## **For Loop**

The `for` loop is another way to iterate over a sequence, like a list or a range. It's widely used in Python for tasks that have a predetermined number of iterations.

### **Looping Through Lists**

Here's how you can print each element in a list:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### **Using `range()`**

The `range()` function generates a sequence of numbers and is commonly used in `for` loops. For instance, to repeat an action 5 times:

```python
for i in range(5):
    print("This is iteration number", i)
```

### **Nested Loops**

You can place a loop inside another loop, allowing for more complex iterations. Here's an example that pairs every combination of two lists:

```python
colors = ["red", "green"]
items = ["book", "pen"]
for color in colors:
    for item in items:
        print(color, item)
```

* * *

## **Conclusion**

Understanding the control flow in Python is paramount for building effective and efficient machine learning models. With the power of conditionals and loops, you can design algorithms that adapt and react to different scenarios and data points. As you dive deeper into Python and machine learning, these foundational concepts will serve as building blocks for more advanced topics. Embrace the journey, and soon you'll harness the full potential of Python in your machine learning projects.

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