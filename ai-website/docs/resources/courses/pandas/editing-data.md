---
title: Working with Data
hide:
  - path
  - navigation
---

# Pandas: Working with Data

## Editing and Retrieving Data

Navigating the vast landscape of data manipulation in Python, one soon realizes the power of the Pandas library. Specifically, the ability to efficiently edit and retrieve data from DataFrames is a game-changer. In this tutorial, we will delve deep into these aspects, ensuring you gain mastery over your datasets.

Pandas offers a plethora of methods to modify and access data within DataFrames. This guide focuses on the most commonly used techniques, making data manipulation a breeze.

## Setting Up

Before diving in, let's create a sample DataFrame:

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
```

## Retrieving Data

### Selecting Specific Columns

```python
names = df['Name']
print(names)
```

### Selecting Multiple Columns

```python
subset = df[['Name', 'City']]
print(subset)
```

### Filtering Rows Based on Conditions

Retrieve rows where age is greater than 30:

```python
filtered_data = df[df['Age'] > 30]
print(filtered_data)
```

## Editing Data

### Modifying a Specific Value

Change Bob's age to 31:

```python
df.loc[df['Name'] == 'Bob', 'Age'] = 31
print(df)
```

### Renaming Columns

```python
df.rename(columns={'Name': 'Full Name'}, inplace=True)
print(df)
```

### Adding New Rows

Add a new entry:

```python
new_entry = {'Full Name': 'Eva', 'Age': 28, 'City': 'Miami'}
df = df.append(new_entry, ignore_index=True)
print(df)
```

### Deleting Rows

Remove the entry for David:

```python
df = df[df['Full Name'] != 'David']
print(df)
```

## Advanced Retrieval: Using `query`

Pandas provides a `query` method, which allows for more readable and compact data retrieval:

```python
youngsters = df.query("`Age` < 30")
print(youngsters)
```

## Conclusion

With the ability to seamlessly edit and retrieve data, Pandas solidifies its place as a cornerstone in Python data manipulation. While this guide provides a solid foundation, the journey doesn't stop here. Dive deeper into the [official Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) to uncover even more functionalities.

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