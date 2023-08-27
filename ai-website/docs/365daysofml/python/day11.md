# Day 11: Python Dictionaries

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/RS1NoCNU6_o
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Dictionaries in Python

Dictionaries in Python are used to store key-value pairs. They are unordered and can contain keys and values of any data type. To create a dictionary in Python, enclose a comma-separated list of key-value pairs in curly braces, with the key and value separated by a colon. You can access and modify the values in a dictionary using their keys. Python also provides various methods to manipulate dictionaries, such as `items()` to return a list of key-value tuples, and `pop()` to remove a key-value pair.

## Creating and Accessing Dictionaries in Python

```python
prices = {
"apple": 0.5,
"banana": 0.25,
"cherry": 0.75
}

info = {
"name": "John",
"age": 30,
"city": "New York"
}
```

In the above example, we have created two dictionaries: `prices` and `info`.

```python
prices = {
"apple": 0.5,
"banana": 0.25,
"cherry": 0.75
}

print(prices["apple"])  # Output: 0.5

prices["banana"] = 0.35
print(prices)  
# Output: {"apple": 0.5, "banana": 0.35, "cherry": 0.75}
```

In this example, we access and modify values in the `prices` dictionary using their keys.

## Manipulating Dictionaries in Python

```python
prices = {
"apple": 0.5,
"banana": 0.25,
"cherry": 0.75
}

# Use items() to return a list of key-value pairs
for item in prices.items():
    print(item)
# Output:
# ('apple', 0.5)
# ('banana', 0.25)
# ('cherry', 0.75)
```

In the above example, we use the `items()` method to return a list of key-value tuples from the `prices` dictionary.

```python
prices = {
"apple": 0.5,
"banana": 0.25,
"cherry": 0.75
}

# Use pop() to remove a key-value pair
prices.pop("banana")
print(prices)  
# Output: {"apple": 0.5, "cherry": 0.75}
```

In this example, we use the `pop()` method to remove a key-value pair from the `prices` dictionary.

By understanding how to create, access, and manipulate dictionaries in Python, you can effectively manage collections of key-value pairs in your code. Stay tuned for more Python-related content.

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