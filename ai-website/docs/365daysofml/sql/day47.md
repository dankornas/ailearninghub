# Day 47: Using aggregate functions

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/jmqr0Dgg8tc
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Leveraging Aggregate Functions in SQL: Calculating Average Ratings

Aggregate functions in SQL, such as `AVG`, allow you to perform various operations on multiple values and return a single value. For instance, if you want to find out the average rating of books in your database, you can use the `AVG` function.

In this context, we use the `SELECT` keyword followed by the `AVG` function to calculate the average of the ratings from the books table. This operation yields an average rating of 4.53.

## Calculating Average Ratings with SQL

Here's how you can calculate the average rating of books using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# SELECT the average of the ratings column
cursor.execute("SELECT AVG(rating) FROM books")

# Retrieve the result
result = cursor.fetchone()

# Print the result
print(f"The average rating of all books is: {result[0]}")

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `AVG` function to calculate the average rating of all books in the books table. The result is fetched and printed, and finally, we close the database connection.

By using aggregate functions like `AVG`, we can efficiently perform calculations on multiple values in our database, simplifying data analysis and improving the readability of our code.

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