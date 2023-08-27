# Day 38: Indexing databases

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/YPI5dbIrKYA
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Indexing in Databases

Indexing is a technique that significantly simplifies searching a database. For instance, if we want to search for a specific book title, we first need to create an index. To do this, we use the 'CREATE INDEX' keywords and assign a specific name to the index. We then specify the table and column we want to index, in this case, the 'books' table and the 'title' column.

## Creating an Index

```python
# Connect to the database
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Create an index on the "title" column in the "books" table
cursor.execute("""
CREATE INDEX idx_title
ON books (title)
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
```

Once the index is created, we can easily search for a book that includes the word 'programming'. We select the 'book_id' and 'book_title' from the 'books' table where the 'book_title' is similar to or includes the word 'programming'. The '%' symbols act as wildcards in this context.

## Using an Index

```python
# Connect to the database
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Searching an indexed column
cursor.execute("""
SELECT book_id, title
FROM books
WHERE title
LIKE '%programming%'
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
```

In this example, we're creating an index on the 'title' column of the 'books' table in our bookstore database. This index, named 'idx_title', significantly improves the speed and efficiency of our searches. We then use this index to search for books with titles that include the word 'programming'. The '%' symbols act as wildcards, allowing us to match any titles that contain 'programming' anywhere within the text.

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