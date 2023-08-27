# Day 49: Using the LIKE operator

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/hBWZbaFGEIg
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the LIKE Operator in SQL: Searching for Patterns in Data

The `LIKE` operator in SQL is a powerful tool that allows us to find patterns in our data. For instance, if you want to find a book that includes the word "Python" in its title, you can use the `LIKE` operator.

In this context, we start with the `SELECT` keyword to select the title column from the books table. We then use the `LIKE` operator to search for titles that contain the word "Python". The percent signs (`%`) act as wildcards, indicating that any characters can come before or after "Python". This means the title doesn't have to be exactly the word "Python".

## Searching for Patterns with SQL

Here's how you can find books with "Python" in the title using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Find books that have "Python" in their title
cursor.execute("""
SELECT title
FROM books
WHERE title LIKE '%Python%'
""")

result = cursor.fetchone()

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `LIKE` operator to find books with "Python" in the title. The result is fetched and finally, we close the database connection.

By using the `LIKE` operator, we can efficiently search for patterns in our database, enhancing our data analysis capabilities and improving the readability of our code.

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