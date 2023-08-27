# Day 48: Using MIN/MAX functions

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/x-FCKJtWyOM
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing Aggregate Functions in SQL: Finding Minimum and Maximum Values

The `MIN` and `MAX` functions in SQL are types of aggregate functions that are extremely useful for data analysis. For instance, if you want to find out the minimum and maximum prices of books in your database, you can use these functions.

In this context, we use the `SELECT` keyword followed by the `MIN` and `MAX` functions to find the minimum and maximum prices, respectively, from the books table.

## Finding Minimum and Maximum Prices with SQL

Here's how you can find the minimum and maximum prices of books using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Get the minimum and maximum prices of books
cursor.execute("""
SELECT MIN(price), MAX(price)
FROM books
""")

result = cursor.fetchone()
min_price = result[0]
max_price = result[1]

print(f"The minimum price is {min_price}")
print(f"The maximum price is {max_price}")

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `MIN` and `MAX` functions to find the minimum and maximum prices of all books in the books table. The results are fetched, printed, and finally, we close the database connection.

By using aggregate functions like `MIN` and `MAX`, we can efficiently perform calculations on multiple values in our database, simplifying data analysis and improving the readability of our code.

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