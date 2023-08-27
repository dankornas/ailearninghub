# Day 41: Using the ORDER BY clause

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/lM9q_nBHxH0
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the ORDER BY Clause in SQL: Sorting Your Data

Often, we want to view our data in a specific order. In such cases, the `ORDER BY` clause in SQL comes in handy. For instance, if you want to order your data by the title name, you can use the `ORDER BY` clause.

In this context, we use the `SELECT` statement to choose the title and author columns that we want to view. We specify that we're getting this information from the books table. Then, we use the `ORDER BY` clause to specify that we want to order the information by the title name.

## Sorting Data with SQL

Here's how you can sort books by title using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Execute SQL command to select the 'title' and 'author' columns from the 'books' table, ordered by the 'title' name
cursor.execute("""
SELECT title, author
FROM books
ORDER BY title
""")

# Retrieve all rows returned by the SELECT statement
rows = cursor.fetchall()

# Iterate over the rows and print each row
for row in rows:
    print(row)

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `ORDER BY` clause to sort book titles and select the corresponding authors. The results are fetched and printed, and finally, we close the database connection.

By using the `ORDER BY` clause, we can efficiently sort data in our SQL queries, enhancing our data analysis capabilities and improving the readability of our code.

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