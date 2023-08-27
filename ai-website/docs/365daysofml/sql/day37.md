# Day 37: Adding constraints to a table

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/ISxKDZmTFtI
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Implementing Constraints in SQL: Ensuring Data Integrity

Constraints in SQL are a way to set rules for our tables. For instance, if we want to ensure that we never forget to include the title of a book when inserting new information into our bookstore database, we can use constraints.

To do this, we first need to modify our current table using the `ALTER` keyword. We specify that we want to alter the 'books' table, then we add the constraint. We give the constraint a name, in this case 'title_not_null', and then we define our constraint. Here, we want to check that the title is not null. We use the `CHECK` clause and specify that the title column should not be null. This way, we can ensure that each time we enter new information into our table, the title column will always contain some kind of information.

## Adding Constraints with SQL

Here's how you can add a 'NOT NULL' constraint to the 'title' column of the 'books' table using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Add a NOT NULL constraint to the title column of the books table
cursor.execute("""
ALTER TABLE books
ADD CONSTRAINT title_not_null
CHECK (title IS NOT NULL)
""")

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `ALTER TABLE` statement to add a 'NOT NULL' constraint to the 'title' column of the 'books' table. Finally, we commit the changes and close the database connection.

By using constraints in SQL, we can ensure data integrity and improve the quality of our data.


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