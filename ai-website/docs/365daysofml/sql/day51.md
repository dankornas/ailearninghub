# Day 51: Using the LIMIT operator

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/bd2SaZuyegM
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the LIMIT Operator in SQL: Controlling the Number of Rows Returned

The `LIMIT` operator in SQL is a valuable tool when you want to control the number of rows returned from your query. Instead of retrieving every row from a table or multiple tables, you can limit the results to a specific number.

For instance, if you want to select only the first five rows from the books table, you can use the `LIMIT` operator. In this context, we use the `SELECT` keyword followed by an asterisk (`*`), which means we're selecting all columns from the books table. However, we limit the results to the first five rows.

## Limiting Rows Returned with SQL

Here's how you can select the first five books from the books table using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Select the first 5 books from the books table
cursor.execute("""
SELECT *
FROM books
LIMIT 5
""")

result = cursor.fetchone()

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `LIMIT` operator to select only the first five books from the books table. The result is fetched and finally, we close the database connection.

By using the `LIMIT` operator, we can efficiently control the number of rows returned from our SQL queries, enhancing our data analysis capabilities and improving the readability of our code.

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