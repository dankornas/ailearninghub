# Day 45: Deleting data from tables

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/7G7ooqnuAv8
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the DELETE Statement in SQL: Removing Data from Your Database

At some point, you may need to remove data from your database. For instance, if you have a book in your bookstore that you no longer want to sell, you can delete it from your database. In this context, we use the `DELETE` keyword to remove data from the books table where the title of the book is 'The Great Gatsby'.

## Deleting Data with SQL

Here's how you can delete a book titled 'The Great Gatsby' from the books table using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Delete a book from the table
cursor.execute("""
DELETE FROM books
WHERE title = 'The Great Gatsby'
""")

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `DELETE` statement to remove the book titled 'The Great Gatsby' from the books table. Finally, we close the database connection.

By using the `DELETE` statement, we can efficiently remove data from our SQL database, enhancing our data management capabilities and improving the readability of our code.

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