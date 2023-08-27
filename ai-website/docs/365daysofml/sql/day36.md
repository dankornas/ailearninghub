# Day 36: Dropping a table

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/L79waEWt7U8
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Deleting a Table in SQLite using Python

In Python, if you have created a table in SQLite but no longer need it, you can remove it using the 'DROP TABLE' SQL command. However, be cautious when using this command, as it permanently deletes the table and all its data, which cannot be recovered.

Here's how you can delete a table in SQLite using Python:

```python
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Drop the 'books' table from the 'bookstore' database
cursor.execute("DROP TABLE books")

# Commit changes and close the connection
conn.commit()
conn.close()
```

In this example, the 'books' table from the 'bookstore' database is deleted. Remember to commit your changes using `conn.commit()` and close the connection using `conn.close()` after executing your SQL commands.

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