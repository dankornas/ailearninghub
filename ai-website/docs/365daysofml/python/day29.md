# Day 29: Python - Reading & Writing Files

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/kSRcRi4a72k
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

"File Input/Output (I/O) in Python is a fundamental technique for data manipulation, allowing you to read from and write data to files on your computer. To open a file, Python provides the `open()` function, which requires the file path and mode as arguments. Common modes include 'r' for reading and 'w' for writing.

Reading from a file can be accomplished using methods such as `read()`, `readline()`, or `readlines()`. Conversely, writing to a file involves the `write()` or `writelines()` methods. It's crucial to remember to close the file after operations are completed, which can be done by invoking the `close()` method."

## Writing to a File in Python

```python
# Write to a file
with open('file.txt', 'w') as f:
    f.write("Hello, world!\n") 
    f.write("This is some text.\n") 
```

In this example, we're using Python's `open()` function with 'w' mode to write data to a file named 'file.txt'. The `write()` method is used to write strings to the file.

## Reading from a File in Python

```python
# Read from a file
with open('file.txt', 'r') as f:
    print(f.read())  
# Output: 
# "Hello, world!\nThis is some text.\n"
```

Here, we're opening the same file in 'r' mode to read its content. The `read()` method is used to read the entire content of the file, which is then printed to the console.

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