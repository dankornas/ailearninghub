# Day 16: Python List Comprehension

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/_W7BwvyJC3k
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Creating Lists with List Comprehension

List comprehensions in Python offer a succinct method to create lists. They enable you to define the elements of a list using a single line of code.

```python
# Create a list of the squares of the numbers from 1 to 10 using list comprehension
numbers = [x**2 for x in range(1, 11)]
print(numbers)  
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## Modifying Lists with List Comprehension

List comprehensions can also be used to modify the elements of a list. For example, you can create a list of uppercase versions of the words in a list.

```python
# Create a list of the uppercase versions of the words in a list using list comprehension
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  
# Output: ["APPLE", "BANANA", "CHERRY"]
```

## Filtering Lists with List Comprehension

The 'if' clause can be utilized to filter the items included in the list.

```python
# Use an 'if' clause in list comprehension to filter words that start with 'a'
words = ["apple", "banana", "cherry", "apricot"]
a_words = [word for word in words if word[0] == "a"]
print(a_words)  
# Output: ["apple", "apricot"]
```

## Altering List Elements with List Comprehension

You can also use list comprehensions to alter the elements of a list. For example, you can double the value of each number in the list or increment the value of each number in the list by one.

```python
# Use list comprehension to double the value of each number in the list
numbers = [1, 2, 3, 4, 5]
numbers = [x * 2 for x in numbers]
print(numbers)  
# Output: [2, 4, 6, 8, 10]

# Use list comprehension to add 1 to the value of each number in the list
numbers = [x + 1 for x in numbers]
print(numbers)  
# Output: [3, 5, 7, 9, 11]
```

!!! info "Learn More"

    Want to learn more about Python for Machine Learning? Check out the full course [HERE](/ai-roadmap/programming/python/data-types/).

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