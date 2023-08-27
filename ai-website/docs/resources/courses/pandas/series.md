---
title: Series
hide:
  - path
  - navigation
---

# Pandas: Series

## Introduction

Pandas Series is one of the foundational data structures provided by the Pandas library. In this tutorial, we'll deep-dive into the concept, covering its creation, manipulation, and various operations you can perform on it. This guide will enable both beginners and advanced users to harness the full potential of the Pandas Series.

## What is a Pandas Series?

A Pandas Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, Python objects, etc.). It comes with both a data sequence and an associated label sequence called its _index_.

## Creating a Pandas Series

#### From a List

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
print(s)
```

#### From a Dictionary

```python
data = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(data)
print(s)
```

#### From a Scalar

If data is a scalar value, an index must be provided:

```python
s = pd.Series(5, index=['a', 'b', 'c'])
print(s)
```

## Accessing Data in a Series

You can access individual elements of a Series similar to arrays and dictionaries:

#### Using the Position

```python
print(s[0])
```

#### Using the Label

```python
print(s['a'])
```

## Basic Operations

### Arithmetic Operations

```python
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
print(s1 + s2)
```

#### Boolean Operations

```python
print(s1 > 2)
```

## Handling Missing Data

Pandas Series provides methods to handle missing data effectively:

```python
s = pd.Series([1, 2, 3, None])
print(s.isnull())
```

## Useful Methods

#### `describe()`:

Gives a quick statistic summary of your data.

```python
print(s.describe())
```

#### `value_counts()`:

Counts unique values.

```python
s = pd.Series(['apple', 'orange', 'apple', 'banana'])
print(s.value_counts())
```

### Series with Datetime

Pandas Series can also handle datetime objects, making time series analysis a breeze:

```python
dates = pd.date_range('20230101', periods=6)
s = pd.Series(dates)
print(s)
```

## Conclusion

Pandas Series provides a robust set of functionalities to handle and manipulate one-dimensional data in Python. This tutorial covered its basics, but there's always more to explore. Make sure to consult the [official Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) for a comprehensive list of functionalities.


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
