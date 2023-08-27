# Day 39: Extracting info from databases

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/445MtU7Miec
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Extracting Information from Databases Using the SELECT Keyword in SQL

One of the most frequent and common tasks when working with databases is extracting information from them. To accomplish this, we use the `SELECT` keyword in SQL. For instance, if we want to retrieve all the information from a specific table that exists in a database, we use the `SELECT` keyword followed by an asterisk (*) to select all the columns. Then, we specify from where this information is coming, which is from a specific table, in this case, the 'books' table.

However, it's important to note that if you're working with large databases, selecting all columns might not be a good idea because it can take a long time to download the information and can be problematic due to the large amount of data.

## Extracting Data with SQL

Here's how you can extract all data from the 'books' table using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# SELECT all columns from the books table
cursor.execute("SELECT * FROM books")

# Commit the changes and close the connection
conn.commit()
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `SELECT` statement to extract all data from the 'books' table. Finally, we commit the changes and close the database connection.

By using the `SELECT` keyword, we can efficiently extract data from our SQL databases, enhancing our data analysis capabilities and improving the readability of our code.


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