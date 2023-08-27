# Day 46: Using subqueries

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/gozUuMOY2QE
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Optimizing SQL Queries with Subqueries: A Practical Example

Subqueries offer a powerful way to streamline your SQL queries by allowing you to use one query within another. This technique can significantly simplify complex tasks, such as finding the book with the highest price in a database.

Without subqueries, you would typically need to perform two separate queries to achieve this. First, you would find the maximum price, and then, using that value, you would select the book with the highest price. However, with subqueries, you can combine these two steps into a single query.

## Using SQL Without Subqueries

Here's how you might approach this task without using subqueries:

```sql
sql_query("SELECT MAX(price) FROM books")
sql_query("""
SELECT book_id, title
FROM books
WHERE price = 14.99
""")
```

In the first query, we find the maximum price from the books table. In the second query, we select the book with a price that matches the maximum price we found earlier. Note that we've hardcoded the maximum price (14.99) in the second query.

## Streamlining with Subqueries

Now, let's see how we can streamline this process using a subquery:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Find the book with the highest price using a subquery
cursor.execute("""
SELECT book_id, title
FROM books
WHERE price = (SELECT MAX(price) FROM books)
""")

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use a subquery to find the book with the highest price in a single step. The subquery `(SELECT MAX(price) FROM books)` finds the maximum price, and the outer query selects the book with that price. Finally, we close the database connection.

By using subqueries, we can write more efficient and readable SQL queries, reducing the complexity of our code and improving its performance.

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