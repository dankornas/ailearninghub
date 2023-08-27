# Day 34: Inserting data into a table

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/V4geirYDz_w
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Inserting New Rows into SQL Tables

Once you've created a table in your database, there may come a time when you need to update it with new rows of information. This can be easily accomplished using the `INSERT INTO` keyword in SQL.

For instance, let's say we want to add a new book to our 'books' table. We can do this using the SQLite3 library in Python. We first connect to our bookstore database and get a cursor. Then, we execute the `INSERT INTO` command, specifying the table and columns we want to insert our information into. We use the `VALUES` keyword to define the values we want to enter, which in this case is the information about our book. As always, we commit the changes and close the connection to save our data.

## Inserting a New Row into a Table with SQL

Here's how you can insert a new row into the 'books' table using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Insert a new book into the 'books' table
cursor.execute("""
INSERT INTO books (title, author, publication_date, price)
VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', '1925-04-10', 9.99)
""")

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `INSERT INTO` statement to add a new book to the 'books' table. Finally, we commit the changes and close the database connection.

By using the `INSERT INTO` command in SQL, we can easily add new rows of information to our tables.

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