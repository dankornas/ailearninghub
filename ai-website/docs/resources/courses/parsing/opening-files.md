---
title: Opening Files
hide:
  - path
  - navigation
---

# Parsing Files: Opening Files


## Opening a File in Python

In the realm of programming, especially in Python, working with files is a fundamental skill. Whether you're reading data or writing results, understanding how to open and manage files is crucial.

### 1. Using the `open` Function to Open a File

In Python, the built-in `open` function is used to open a file. It returns a file object which can be used to read, write, or append to the file.

#### Syntax

```python
file_object = open("filename", "mode")
```

* **filename**: The name of the file you want to open.
* **mode**: The mode in which you want to open the file. Common modes include:
    * `r`: Read (default mode)
    * `w`: Write
    * `a`: Append

#### Example

```python
# Opening a file named "sample.txt" in read mode
file = open("sample.txt", "r")
```

### 2. The Importance of Closing a File

Once you're done working with a file, it's essential to close it using the `close` method. Closing a file:

* Frees up the resources that were tied with the file.
* Ensures that changes made to the file are saved.
* Prevents potential data corruption.

#### Example

```python
file = open("sample.txt", "r")
# ... perform operations on the file ...
file.close()  # Closing the file
```

### 3. Printing the Name of the File

Every file object in Python has a `name` attribute that stores the name of the file. You can easily print it as follows:

```python
file = open("sample.txt", "r")
print(file.name)  # Outputs: sample.txt
file.close()
```

### 4. Printing the Mode of the File

To determine in which mode a file was opened (read, write, append, etc.), you can use the `mode` attribute of the file object.

```python
file = open("sample.txt", "r")
print(file.mode)  # Outputs: r
file.close()
```


---

!!! note "Version 1.0"

    This is currently an early version of the learning material and it will be updated over time with more detailed information.

    A video will be provided with the learning material as well.

    Be sure to subscribe to stay up-to-date with the latest updates.

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
