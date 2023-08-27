---
title: Input/Output Operations
hide:
  - path
  - navigation
---

# Numpy: Input/Output Operations

## **Reading From Files**

Machine learning projects often involve working with large datasets, commonly saved in files. These could be CSVs, text files, or other formats. NumPy provides straightforward methods to read data from these files into arrays, allowing for immediate processing.

### **Loading Data from Text or CSV Files**

NumPy's `genfromtxt` and `loadtxt` functions are handy tools to load data from text files, like CSVs:

```python
import numpy as np

# Using loadtxt
data = np.loadtxt('data.csv', delimiter=',')

# Using genfromtxt, which offers more advanced options
data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
```

Here, `delimiter` specifies the character that separates values in the file. For CSVs, it's typically a comma.

### **Handling Missing Values**

Real-world data isn't always clean; it can have missing values. When using `genfromtxt`, you can handle these missing values effectively:

```python
data = np.genfromtxt('data.csv', delimiter=',', skip_header=1, filling_values=-999)
```

In the above example, any missing value will be filled with -999.

* * *

## **Saving & Loading NumPy Objects**

After data processing or model training, saving results or trained parameters is often required. Similarly, in other stages of a project, you might need to load these saved objects. NumPy makes both tasks straightforward.

### **Saving Arrays to Disk**

To save a NumPy array as a binary `.npy` file:

```python
arr = np.array([1, 2, 3, 4, 5])
np.save('array_data.npy', arr)
```

For multiple arrays, you can save them as a `.npz` file:

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
np.savez('arrays_data.npz', arr1=arr1, arr2=arr2)
```

### **Loading Arrays from Disk**

Loading your saved data is just as simple:

```python
loaded_arr = np.load('array_data.npy')

# For .npz files
loaded_data = np.load('arrays_data.npz')
first_array = loaded_data['arr1']
```

* * *

Incorporating NumPy's I/O operations into your machine learning workflows ensures that your data handling is both efficient and effective. With just a few commands, you can seamlessly integrate file-based data into your projects, allowing you to focus on what really matters: building and refining your machine learning models.

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