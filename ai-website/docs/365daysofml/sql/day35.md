# Day 35: Altering a table

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/1YYROCFqppc
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Modifying SQL Tables: Adding a New Column

There might be instances where you've created a table, but later decide to modify it by adding a new column. This can be accomplished using the `ALTER` keyword in SQL.

For instance, let's say we want to add a new column named 'publisher' to our 'books' table. We can do this using the SQLite3 library in Python. We first connect to our bookstore database and get a cursor. Then, we execute the `ALTER TABLE` command, specifying the name of the table we want to alter. We use the `ADD COLUMN` keywords to add a new column, name the column 'publisher', and define the type of information it will hold, which in this case is text. As always, we commit the changes and close the connection to save our data.

## Adding a New Column to a Table with SQL

Here's how you can add a new column to the 'books' table using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Add a new column 'publisher' to the 'books' table
cursor.execute("""
ALTER TABLE books
ADD COLUMN publisher text
""")

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `ALTER TABLE` statement to add a new column 'publisher' to the 'books' table. Finally, we commit the changes and close the database connection.

By using the `ALTER TABLE` command in SQL, we can easily modify our tables to better suit our data needs.

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