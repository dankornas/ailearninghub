# Day 13: Python Tuples

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/a1FUURTDM8I
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Tuples in Python

Tuples in Python are used to store a collection of items. They are similar to lists, but they are immutable, meaning that their items cannot be modified once they are created. To create a tuple in Python, enclose a comma-separated list of items in parentheses. You can access and unpack the items in a tuple using their index or using multiple assignment. Tuples are often used to return multiple values from a function, and they can also be used as keys in dictionaries since they are immutable.

## Creating Tuples in Python

```python
numbers = (1, 2, 3, 4, 5)
words = ("apple", "banana", "cherry")
mixed = (1, "apple", 3.14, [4, 5])
```

In the above example, we have created three tuples: `numbers`, `words`, and `mixed`.

## Accessing and Unpacking Tuples in Python

```python
numbers = (1, 2, 3, 4, 5)

print(numbers[0])  # Output: 1
print(numbers[2])  # Output: 3

x, y, z, _, _ = numbers 
print(x, y, z)  
# Output: 1 2 3
```

In this example, we access items in the `numbers` tuple using their index. We also unpack the `numbers` tuple using multiple assignment.

By understanding how to create, access, and unpack tuples in Python, you can effectively manage collections of immutable items in your code. Stay tuned for more Python-related content.

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