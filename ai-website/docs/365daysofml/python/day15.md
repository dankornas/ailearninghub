# Day 15: Python Slicing

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/HhPmtfk4ot8
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Slice Notation in Python

Slice notation in Python is a way to extract a subsequence from a sequence, such as a list, tuple, or string. It is written as `start:stop:step`, where `start` is the index of the first item to include, `stop` is the index of the first item to exclude, and `step` is the number of items to skip between items.

## Extracting Subsequences in Python

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extract the second to fifth items
# (indexes 1 to 4)
sub_sequence = numbers[1:5]
print(sub_sequence)  
# Output: [2, 3, 4, 5]
```

In the above example, we use slice notation to extract a subsequence from the `numbers` list.

## Skipping Items with Slice Notation in Python

```python
# Extract every second item, 
# starting from the second item (index 1)
sub_sequence = numbers[1::2]
print(sub_sequence)  
# Output: [2, 4, 6, 8, 10]
```

In this example, we use slice notation to extract every second item from the `numbers` list.

## Extracting the Last Items with Slice Notation in Python

```python
# Extract the last three items
sub_sequence = numbers[-3:]
print(sub_sequence)  
# Output: [8, 9, 10]
```

In this example, we use slice notation to extract the last three items from the `numbers` list.

By understanding how to use slice notation in Python, you can effectively extract subsequences from your sequences. Stay tuned for more Python-related content.

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