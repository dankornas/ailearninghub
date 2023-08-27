# Day 33: Creating a table

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/KeHg6Yaw70Q
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Creating a Table in SQL Database

To create a table in a SQL database, you first need to establish a connection to the database. Once the connection is established, a cursor is created. This cursor points to the location in the database where we want to execute our commands.

In Python, we use the `execute` method to run SQL commands. To create a table, we use the `CREATE TABLE` command, followed by the `IF NOT EXISTS` condition to avoid creating a table that already exists. We then specify the name of the table, in this case, 'books'.

Next, we define each column that we want in our table, along with the type of data it will hold (integer, text, date, real, etc.). We also specify any constraints, such as whether the column is a primary key or if it cannot be null (empty).

Once we've defined our table, we commit the changes to save them and then close the connection to the database.

## Creating a Table in SQL Database with Python

Here's an example of how to create a table in a SQL database using Python:

```python
import sqlite3

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create the 'books' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publisher TEXT NOT NULL,
    published_date DATE NOT NULL,
    price REAL NOT NULL,
    genre TEXT NOT NULL,
    rating INTEGER NOT NULL,
    is_bestseller INTEGER NOT NULL
)
""")

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `CREATE TABLE` statement to create a new 'books' table with various columns and constraints. Finally, we commit the changes and close the database connection.

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