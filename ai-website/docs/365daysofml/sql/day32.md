# Day 32: Creating a database

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/JHelLdPAkic
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction to SQL with Python

We're embarking on a new journey to master SQL with Python, leveraging the power of the sqlite3 library. Our first step is to create a database using the `connect` method. This handy function serves a dual purpose - if the database doesn't exist, it will create a new one; if it does, it will connect to the existing database.

## Setting the Context

For the purpose of our upcoming tutorials, we'll imagine we're running a bookstore, tracking books, orders, and customers.

## What's Next?

In the subsequent videos, we'll dive deep into various SQL commands essential for managing your database. So, stay tuned!"

And here's the corrected code snippet with headers:

## Importing Necessary Libraries

```python
import sqlite3
```

## Connecting to the Database

```python
# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")
```

## Creating a Cursor

```python
# Create a cursor to execute SQL commands
# which acts as a pointer to the database
# connection
cursor = conn.cursor()
```

## Executing SQL Query

**Please note that you need to replace "SQL query" with your actual SQL query.**

```python
# SELECT all columns from the books table
cursor.execute("SQL query")
```

## Fetching and Printing the Results

```python
# Retrieve all rows returned by the SELECT statement
rows = cursor.fetchall()
# Iterate over the rows
for row in rows:
    print(row)
print()
```

## Closing the Connection

```python
conn.close()
```

!!! info "Learn More"

    Want to learn more about SQL for Machine Learning? Check out the full course [HERE](/ai-roadmap/data-collection/sql-databases/).

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