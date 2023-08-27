---
title: Array Operations
hide:
  - path
  - navigation
---

# Numpy: Array Operations


## **Copying Arrays**

One of the foundational concepts to grasp in NumPy is the difference between copying by reference and creating a true copy of an array. When working with data, especially in machine learning, it's essential to understand how your data is being manipulated to avoid unintentional changes to your datasets.

### **Shallow Copy (View) vs. Deep Copy**

* **Shallow Copy (View):** When you create a shallow copy of an array, both the original and the copy refer to the same memory location. Any changes made to one will reflect on the other.
    
    ```python
    import numpy as np
    arr = np.array([1, 2, 3, 4])
    shallow_copy = arr.view()
    shallow_copy[0] = 10
    # Now, arr[0] will also be 10
    ```
    
* **Deep Copy:** A deep copy creates an entirely new array in memory. Changes to the copied array won't affect the original and vice versa.
    
    ```python
    deep_copy = arr.copy()
    deep_copy[1] = 20
    # arr[1] will still be 2
    ```
    

For machine learning tasks, where data integrity is paramount, understanding the difference between these two types of copies can be crucial.

* * *

## **Universal Math**

NumPy offers a comprehensive set of mathematical operations that can be performed on arrays. These are termed "universal functions" as they operate universally on all elements of an array. These functions are optimized, allowing for fast and efficient computations, which is invaluable in machine learning tasks involving large datasets.

### **Basic Arithmetic**

You can easily perform element-wise arithmetic operations on arrays. This means operations are performed on corresponding elements of arrays.

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sum_arr = arr1 + arr2  # Outputs [5, 7, 9]
```

### **Aggregation Functions**

Aggregation functions operate over arrays and return single values. They are useful in machine learning for summarizing data or checking data properties.

* `np.sum()`: Sum of all elements.
* `np.min()`: Minimum value in array.
* `np.max()`: Maximum value in array.
* `np.mean()`: Mean of all elements.

### **Trigonometric and Exponential Functions**

For tasks like feature engineering or specific algorithms, you might need trigonometric or exponential functions. NumPy has you covered with functions like:

* `np.sin()`
* `np.cos()`
* `np.tan()`
* `np.exp()`: Exponential function

* * *

Mastering array operations in NumPy is a foundational step in becoming proficient at machine learning in Python. Whether you're tweaking data for a neural network, performing feature engineering for a regression model, or simply exploring your dataset, understanding these operations is key. Dive in, practice, and soon enough, these operations will become second nature, streamlining your machine learning workflows.

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