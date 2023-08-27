---
title: Copying Files
hide:
  - path
  - navigation
---

# Parsing Files: Copying Files

## Copying Files in Python

In the dynamic world of Python programming, file operations are a cornerstone. While reading and writing files are fundamental, there are times when you need to duplicate or backup files. This guide will walk you through the process of copying files in Python, ensuring you have a robust toolkit for your file management needs.

### **1. Using the `shutil` Library**

Python's standard library, `shutil`, provides a convenient method for copying files.

```python
import shutil

# Copying 'source.txt' to 'destination.txt'
shutil.copy('source.txt', 'destination.txt')
```

**Key Takeaway**: The `shutil.copy()` method is straightforward and handles the copying process efficiently.

### **2. Copying and Preserving Metadata**

If you want to copy a file and retain its metadata (like permissions), use the `copy2` method.

```python
shutil.copy2('source.txt', 'destination.txt')
```

**Pro Tip**: This method is especially useful when copying system or configuration files where metadata is crucial.

### **3. Copying Directories**

For copying entire directories, `shutil` offers the `copytree` method.

```python
# Copying the 'source_directory' to 'destination_directory'
shutil.copytree('source_directory', 'destination_directory')
```

**Note**: Ensure the destination directory doesn't exist beforehand, or you'll encounter an error.

### **4. Using `os` Library for File Operations**

While `shutil` is powerful, sometimes you might want to leverage the `os` library for more granular control.

```python
import os

# Define source and destination paths
source = 'source.txt'
destination = 'destination.txt'

# Use open and write methods for copying
with open(source, 'rb') as src_file:
    with open(destination, 'wb') as dest_file:
        dest_file.write(src_file.read())
```


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
