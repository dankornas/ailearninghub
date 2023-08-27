# Day 53: Using the BETWEEN operator

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/TsHfupmZAPE
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the BETWEEN Operator in SQL: Finding Values Within a Specific Range

The `BETWEEN` operator in SQL is a powerful tool that allows us to find values within a specific range. For instance, if you want to find books priced between $10 and $20, you can use the `BETWEEN` operator.

In this context, we use the `SELECT` command to get the title and price from the books table. We then specify that we want rows where the price is between 10 and 20.

## Finding Values Within a Range with SQL

Here's how you can select books priced between $10 and $20 using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Use the BETWEEN operator to retrieve books with a price between 10 and 20
cursor.execute("""
SELECT title, price
FROM books
WHERE price BETWEEN 10 AND 20
""")

# Retrieve all rows returned by the SELECT statement
rows = cursor.fetchall()

# Iterate over the rows and print each row
for row in rows:
    print(row)

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `BETWEEN` operator to select books priced between $10 and $20. The results are fetched and printed, and finally, we close the database connection.

By using the `BETWEEN` operator, we can efficiently find values within a specific range in our SQL queries, enhancing our data analysis capabilities and improving the readability of our code.

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