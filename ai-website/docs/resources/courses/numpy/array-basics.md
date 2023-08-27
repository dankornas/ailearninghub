---
title: Array Basics
hide:
  - path
  - navigation
---

# Numpy: Array Basics

## **Creating Arrays**

One of the foundational tasks in NumPy is creating arrays. An array is essentially a data structure that stores values of the same type in Python, and it's crucial for machine learning tasks because data in ML is typically represented as arrays. Here's how to create arrays in NumPy:

* **From a Python List:** You can create a NumPy array directly from a Python list.
    
    ```python
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    ```
    
* **Using Functions:** There are several built-in functions in NumPy that allow for array creation, such as `zeros()`, `ones()`, and `arange()`.
    
    ```python
    zeros_arr = np.zeros(5)  # Creates an array of zeros with length 5
    ones_arr = np.ones(5)    # Creates an array of ones with length 5
    range_arr = np.arange(5) # Creates an array with values [0, 1, 2, 3, 4]
    ```
    

## **Data Types**

In NumPy, arrays are grids of values, and they can contain various data types. By default, NumPy tries to guess the data type for the array based on the values you provide, but you can explicitly specify the data type using the `dtype` parameter.

Common data types include:

* `int64`: Integer type
* `float64`: Floating point type
* `complex128`: Complex number type
* `bool`: Boolean type (True/False)

For instance, to create an integer array:

```python
arr = np.array([1, 2, 3, 4], dtype='int64')
```

## **Slicing & Indexing**

Slicing and indexing are vital operations when working with NumPy arrays, especially in the context of machine learning where you often need to select specific data points or split datasets.

* **Indexing:** Just like Python lists, you can access an array's elements by referring to its index number.
    
    ```python
    arr = np.array([10, 20, 30, 40, 50])
    first_element = arr[0]  # Returns 10
    ```
    
* **Slicing:** To select a range of elements from an array, you can use the slice notation, which consists of the start index, end index, and the step value.
    
    ```python
    subset = arr[1:4]  # Returns an array with values [20, 30, 40]
    ```
    

## **Reshaping Arrays**

The shape of a NumPy array is crucial when you're feeding data into machine learning models. Often, you'll need to reshape data to fit the input or output structure of a model.

The `reshape()` method allows you to reorganize the data within an array, providing a new shape without changing the data itself.

```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)  # Reshapes the array into a 2x3 matrix
```

It's crucial to note that the total number of elements must remain the same when reshaping.

## **Stacking & Splitting**

Machine learning often requires merging datasets or splitting them for tasks like training and testing.

* **Stacking:** You can use `vstack()` for vertical stacking and `hstack()` for horizontal stacking.
    
    ```python
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    stacked_arr = np.vstack((arr1, arr2))  # Stacks arr2 below arr1
    ```
    
* **Splitting:** The `array_split()` function can split an array into multiple smaller arrays.
    
    ```python
    arr = np.array([1, 2, 3, 4, 5, 6])
    split_arr = np.array_split(arr, 2)  # Splits the array into two arrays
    ```
    

* * *

By mastering these array basics in NumPy, you'll be well-equipped to handle the data manipulation tasks inherent in the machine learning pipeline. Whether you're preprocessing data, building models, or evaluating results, a solid grasp of NumPy's array functionalities is invaluable.

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