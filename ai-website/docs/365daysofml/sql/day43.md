# Day 43: Joining Tables

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/TwwIlgZC1fc
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the JOIN Statement in SQL: Combining Rows from Multiple Tables

The `JOIN` statement in SQL is a powerful tool used to combine rows from two or more tables based on a related column between them. For instance, if you want to find out how many orders a certain customer has made, you can use a `JOIN` statement to combine data from the customers table and the orders table.

In this context, we use the `SELECT` statement to choose the first name from the customers table and the book ID and quantity from the orders table. We then specify the table we're selecting from (orders) and join it with the customers table. The crucial part is the `ON` clause, where we specify the common column between the two tables, in this case, the customer ID.

## Joining Tables with SQL

Here's how you can join the 'Orders' and 'Customers' tables on the 'customer_id' column using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Join the 'Orders' and 'Customers' tables on the 'customer_id' column
cursor.execute("""
SELECT customers.first_name, orders.book_id, orders.quantity
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
""")

# Retrieve all rows returned by the SELECT statement
rows = cursor.fetchall()

# Iterate over the rows and print each row
for row in rows:
    print(row)

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `JOIN` statement to combine data from the 'Orders' and 'Customers' tables based on the 'customer_id' column. The results are fetched and printed, and finally, we close the database connection.

By using the `JOIN` statement, we can efficiently combine data from multiple tables in our SQL queries, enhancing our data analysis capabilities and improving the readability of our code.

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