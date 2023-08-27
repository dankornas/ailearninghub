---
title: Dataframes
hide:
  - path
  - navigation
---

# Pandas: Dataframes

Diving into the world of data analysis with Python, you'll frequently come across the term "DataFrame" if you use the Pandas library. In this extensive tutorial, we'll unravel the nuances of creating DataFrames in Pandas, ensuring you're well-equipped to handle tabular data with ease.

## What is a Pandas DataFrame?

A **Pandas DataFrame** is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). Imagine an in-memory Excel sheet where you can perform operations programmatically; that's your DataFrame!

## Creating a DataFrame

Pandas provides multiple methods to create a DataFrame:

### From a Dictionary of Series or Lists

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)
```

### From a List of Dictionaries

```python
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]

df = pd.DataFrame(data)
print(df)
```

### From a CSV File

```python
# Assuming you have a file 'data.csv' with appropriate data
df = pd.read_csv('data.csv')
print(df)
```

## Setting Custom Indexes

While creating a DataFrame, you can also set a custom index:

```python
df = pd.DataFrame(data, index=['Student1', 'Student2', 'Student3'])
print(df)
```

## Accessing Data in a DataFrame

### Selecting Columns

```python
print(df['Name'])
```

### Selecting Rows

Using `loc` for label-based indexing:

```python
print(df.loc['Student1'])
```

Using `iloc` for position-based indexing:

```python
print(df.iloc[0])
```

## DataFrame Basic Operations

### Adding a New Column

```python
df['Score'] = [85, 90, 88]
print(df)
```

### Deleting a Column

```python
df.drop('Score', axis=1, inplace=True)
print(df)
```

### Handling Missing Data

```python
df['Score'] = [85, None, 88]
print(df.fillna(0))
```

## Conclusion

The Pandas DataFrame is a powerful tool for data manipulation and analysis in Python. This tutorial touched upon its creation and basic operations, but there's a universe of possibilities with DataFrames. For an exhaustive list of functionalities, check the [official Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

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