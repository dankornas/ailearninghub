# Day 44: Updating tables

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/Q3UWCRWAPK8
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the UPDATE Statement in SQL: Modifying Data in Your Database

There may be instances where you need to modify data in your database. For example, if you want to update the price of a specific book in your bookstore, you can use the `UPDATE` statement in SQL.

In this context, we start with the `UPDATE` keyword, followed by the name of the table we want to update, which is the books table. We then use the `SET` keyword to specify what we want to modify, in this case, the price, and set it to 12.99. However, we don't want to change the price for all the books, so we use the `WHERE` clause to specify the title of the book we want to update, 'To Kill a Mockingbird'.

## Updating Data with SQL

Here's how you can update the price of 'To Kill a Mockingbird' in the books table using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Update the price of a specific book
cursor.execute("""
UPDATE books
SET price = 12.99
WHERE title = 'To Kill a Mockingbird'
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `UPDATE` statement to change the price of 'To Kill a Mockingbird' in the books table. After making the changes, we commit them to the database and close the connection.

By using the `UPDATE` statement, we can efficiently modify data in our SQL database, enhancing our data management capabilities and improving the readability of our code.


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