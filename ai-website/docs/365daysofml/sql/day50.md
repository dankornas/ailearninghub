# Day 50: Using the IN operator

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/6ai-kbubYR8
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the IN Operator in SQL: Checking Values Within a Specific Range

The `IN` operator in SQL is a useful tool for checking if values fall within a specific range. For instance, if you want to find books with ratings between 3 and 4, you can use the `IN` operator.

In this context, we use the `SELECT` keyword followed by an asterisk (`*`), which means we're selecting all columns from the books table. We then specify that we're looking for rows where the rating is within the range of 3 and 4. In other words, we're looking for books with ratings between 3 and 4.

## Checking Values Within a Range with SQL

Here's how you can find books with ratings between 3 and 4 using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Get books within a range of ratings
cursor.execute("""
SELECT *
FROM books
WHERE rating IN (3, 4)
""")

result = cursor.fetchone()

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `IN` operator to find books with ratings between 3 and 4. The result is fetched and finally, we close the database connection.

By using the `IN` operator, we can efficiently check if values fall within a specific range in our database, enhancing our data analysis capabilities and improving the readability of our code.

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