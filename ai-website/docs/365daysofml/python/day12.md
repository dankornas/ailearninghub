# Day 12: Python Sets

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/CMj7DBS828k
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Sets in Python

Sets in Python are used to store a collection of unique items. They are unordered and cannot contain duplicates. To create a set in Python, enclose a comma-separated list of items in curly braces or use the `set()` function. You can add and remove items from a set using the `add()` and `remove()` methods.

## Creating Sets in Python

```python
numbers = {1, 2, 3, 4, 5}
words = set(["apple", "banana", "cherry"])
```

In the above example, we have created two sets: `numbers` and `words`. The `numbers` set is created using curly braces, while the `words` set is created using the `set()` function.

## Manipulating Sets in Python

```python
numbers = {1, 2, 3, 4, 5}

numbers.add(6)
print(numbers)  
# Output: {1, 2, 3, 4, 5, 6}

numbers.remove(4)
print(numbers)  
# Output: {1, 2, 3, 5, 6}
```

In this example, we use the `add()` and `remove()` methods to add and remove items from the `numbers` set.

By understanding how to create and manipulate sets in Python, you can effectively manage collections of unique items in your code. Stay tuned for more Python-related content.

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