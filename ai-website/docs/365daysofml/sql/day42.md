# Day 42: Using the GROUP BY clause

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/TmVCY-VKkz4
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Utilizing the GROUP BY Clause in SQL: Organizing Similar Information

The `GROUP BY` clause in SQL is a useful tool that helps organize similar information together, providing a better overview and understanding of our data. For instance, if you want to see how many books have the same ratings, you can use the `GROUP BY` clause.

In this context, we use the `SELECT` statement to choose the rating and count the number of titles (or books) that have that specific rating. We're getting this information from the books table and we want to group the results by the rating. This will return the rating and the count of books that share the same rating.

## Grouping Data with SQL

Here's how you can group books by rating and count the number of books that share the same rating using SQL and Python:

```python
import sqlite3

# Connect to the bookstore.db database
conn = sqlite3.connect("bookstore.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Using 'GROUP BY' to organize book ratings
# The following SQL command returns the rating and the count of books that share the same rating.
# It uses the 'GROUP BY' clause to organize the results by rating.
cursor.execute("""
SELECT rating, COUNT(title)
FROM books
GROUP BY rating
""")

# Retrieve all rows returned by the SELECT statement
rows = cursor.fetchall()

# Iterate over the rows and print each row
for row in rows:
    print(row)

# Close the database connection
conn.close()
```

In this Python script, we connect to the bookstore.db database and create a cursor to execute SQL commands. We then use the `GROUP BY` clause to organize book ratings and count the number of books that share the same rating. The results are fetched and printed, and finally, we close the database connection.

By using the `GROUP BY` clause, we can efficiently organize similar data in our SQL queries, enhancing our data analysis capabilities and improving the readability of our code.

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