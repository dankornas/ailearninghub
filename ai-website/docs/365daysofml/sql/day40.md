# Day 40: Using the WHERE clause

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/-ijdZ0U7JUE
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the WHERE Clause in SQL: Filtering Your Data

Often, you may want to filter specific information from your database. In such cases, the `WHERE` clause in SQL proves to be very helpful. For instance, if you want to retrieve books that have a rating of 5, you can use the `WHERE` clause.

In this context, we use the `SELECT` statement to choose the title and rating columns. We specify that we're getting this information from the books table. Then, we use the `WHERE` clause to specify that we want to filter books where the rating equals 5.

## Filtering Data with SQL

Here's how you can filter books by rating using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# SELECT the book title and rating columns from the books table WHERE the rating is equal to 5
cursor.execute("""
SELECT title, rating
FROM books
WHERE rating = 5
""")

# Retrieve all rows returned by the SELECT statement
rows = cursor.fetchall()

# Iterate over the rows and print each row
for row in rows:
    print(row)

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `WHERE` clause to filter book titles and ratings where the rating equals 5. The results are fetched and printed, and finally, we close the database connection.

By using the `WHERE` clause, we can efficiently filter data in our SQL queries, enhancing our data analysis capabilities and improving the readability of our code.

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
            <a href="/subscribetext-decoration: none;">Subscribe Now</a>
        </button>
    </div>
</div>