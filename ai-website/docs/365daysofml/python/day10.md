# Day 10: Python Lists

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/wpQ-YxoD-Q0
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Lists in Python

Lists in Python are used to store a collection of items in a single place. They are ordered and can contain items of any data type, including other lists. To create a list in Python, enclose a comma-separated list of items in square brackets. You can access and modify the items in the list using their index, which starts at 0 for the first item. Python also provides various methods to manipulate lists, such as `append()` to add an item to the end of the list.

## Creating and Accessing Lists in Python

```python
numbers = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry"]
mixed = [1, "apple", 3.14, [4, 5]]
```

In the above example, we have created three lists: `numbers`, `words`, and `mixed`. The `mixed` list even contains another list as one of its items.

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[0])  # Output: 1
print(numbers[2])  # Output: 3

numbers[1] = 6
print(numbers)  # Output: [1, 6, 3, 4, 5]
```

In this example, we access items in the `numbers` list using their index and modify one of the items.

## Manipulating Lists in Python

```python
numbers = [1, 2, 3, 4, 5]

# Use append() to add an item to the end of the list
numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
```

In the above example, we use the `append()` method to add an item to the end of the `numbers` list.

```python
numbers = [1, 2, 3, 4, 5]

# Use pop() to remove an item from the end of the list
numbers.pop()
print(numbers)  # Output: [1, 2, 3, 4]

# You can also specify the index of the item to remove
numbers.pop(1)
print(numbers)  # Output: [1, 3, 4]
```

In this example, we use the `pop()` method to remove an item from the end of the `numbers` list. We also show how to remove an item at a specific index.

By understanding how to create, access, and manipulate lists in Python, you can effectively manage collections of items in your code. Stay tuned for more Python-related content.

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