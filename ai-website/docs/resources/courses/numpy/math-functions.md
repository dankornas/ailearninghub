---
title: Math Functions
hide:
  - path
  - navigation
---

# Numpy: Math Functions


## **Statistics Functions**

Statistical functions play a pivotal role in understanding the underlying patterns and characteristics of data. By providing insights into data distribution, central tendencies, and dispersions, they form the basis of many preprocessing steps in machine learning.

### **Descriptive Statistics**

* **Mean:** The average value, offering a quick glance at the data's central tendency.
    
    ```python
    data = np.array([10, 20, 30, 40, 50])
    mean = np.mean(data)
    ```
    
    The mean helps in understanding the "middle ground" of your data but can be influenced by outliers.
    
* **Median:** A more robust measure than the mean, the median represents the middle value in a sorted dataset, unaffected by extreme values.
    
    ```python
    median = np.median(data)
    ```
    
* **Standard Deviation & Variance:** These metrics shed light on data spread. A high standard deviation indicates that data points are far from the mean, while a low value suggests the opposite.
    
    ```python
    std_dev = np.std(data)
    variance = np.var(data)
    ```
    

### **Correlation**

Understanding how two variables move concerning each other is vital. A high correlation might suggest a relationship worth exploring with machine learning models.

```python
correlation_coefficient = np.corrcoef(data1, data2)[0, 1]
```

* * *

## **Creating Formulas**

Machine learning often requires bespoke transformations on data. Whether it's a normalization function or a complex equation, NumPy makes custom calculations on entire datasets seamless.

### **Applying Custom Functions**

With `np.vectorize()`, a regular Python function can be transformed to operate on entire arrays, making batch operations efficient.

```python
def custom_function(x):
    return x**2 + 5

vectorized_function = np.vectorize(custom_function)
result = vectorized_function(data)
```

This approach is especially beneficial when complex transformations need to be applied uniformly to every data point.

* * *

## **Trigonometry Functions**

While trigonometry might remind some of high school math, it holds significance, especially when dealing with cyclic or periodic data such as sound waves or time series with seasonality.

* **Sin, Cos, and Tan:** These fundamental functions compute the sine, cosine, and tangent of each element in the array.
    
    ```python
    sine_values = np.sin(data)
    cosine_values = np.cos(data)
    tangent_values = np.tan(data)
    ```
    
* **Radians to Degrees:** Sometimes, it's more intuitive to work in degrees rather than radians, especially in graphics or simulations.
    
    ```python
    degrees = np.degrees(data)
    ```
    

* * *

## **Linear Algebra**

The heart of many machine learning algorithms, especially in areas like deep learning and optimization, linear algebra operations are both versatile and essential.

### **Matrix Multiplication**

A fundamental operation in neural networks, matrix multiplication, when done element-wise, can lead to the transformation of data in ways that enable learning from it.

```python
result = np.dot(matrix1, matrix2)
```

### **Eigenvalues and Eigenvectors**

These concepts, while advanced, are instrumental in algorithms like Principal Component Analysis (PCA), which reduces the dimensionality of data.

```python
eigenvalues, eigenvectors = np.linalg.eig(matrix)
```

### **Matrix Inversion**

Crucial in algorithms like linear regression, matrix inversion helps in solving sets of linear equations, which can predict outcomes from input data.

```python
inverse = np.linalg.inv(matrix)
```

* * *

Understanding and effectively leveraging the mathematical functionalities in NumPy can transform the way you approach machine learning problems. By offering optimized, efficient, and versatile operations, NumPy ensures that you spend less time wrangling data and more time extracting valuable insights from it.

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