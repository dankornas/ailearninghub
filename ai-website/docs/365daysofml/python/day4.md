# Day 4: Python Data Types

<iframe width="360" height="655" src="https://www.youtube.com/embed/IPRDpwFUfyQ?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In Python, we utilize a variety of built-in data types to represent diverse forms of data. Let's delve into some of the most frequently used ones.

## Integers in Python

Integers, denoted as 'int' in Python, are whole numbers that can range from being positive, negative, or zero.

```python
# Integers 
var = 5
print(var)
print(type(var))

## Output ##
# 5
# <class 'int'>
```

## Floating-Point Numbers in Python

Floating-point numbers, or 'floats', are numbers that include decimal points.

```python
# Floats 
var2 = 0.1234
print(var2)
print(type(var2))

## Output ##
# 0.1234
# <class 'float'>
```

## Strings in Python

Strings are sequences of characters that are utilized to represent text.

```python
# Strings
str_one = "Hello World"
print(str_one)
print(type(str_one))

## Output ##
# Hello World
# <class 'str'>
```

## Lists in Python

Lists are ordered collections of items of any data type. The items in a list can be modified after its creation.

```python
# Lists
list1 = ["car","bike"]
print(list1)
print(type(list1))

## Output ##
# ['car', 'bike']
# <class 'list'>
```

## Tuples in Python

Tuples are ordered collections of items, similar to lists. However, once a tuple is created, you cannot change its items.

```python
# Tuples
tup= ("car","bike","bus")
print(tup)
print(type(tup))

## Output ##
# ('car', 'bike', 'bus')
# <class 'tuple'>
```

## Sets in Python

Sets are unordered collections of unique items. They are often employed to eliminate duplicates from a list or to verify membership within a group of items.

```python
# Sets 
set_one = set({"Hello","world","Hello"})
print(set_one)
print(type(set_one))

## Output ##
# {'world', 'Hello'}
# <class 'set'>
```

## Dictionaries in Python

Dictionaries are unordered collections of key-value pairs. The keys are used to access the values in the dictionary.

```python
# Dictionaries
dict_one = {"Name": "Steve", "Location": "NewYork"}
print(dict_one)
print(type(dict_one))

## Output ##
# {'Name': 'Steve', 'Location': 'NewYork'}
# <class 'dict'>
```

## Booleans in Python

Booleans are a data type with only two possible values: True and False.

```python
# Booleans
bool_var = True
print(bool_var)
print(type(bool_var))

## Output ##
# True
# <class 'bool'>
```

These are some of the fundamental data types in Python that form the building blocks of Python programming. Understanding these data types is crucial for data manipulation and performing operations in Python.

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
