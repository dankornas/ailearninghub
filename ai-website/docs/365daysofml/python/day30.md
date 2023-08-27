# Day 30: Python Regular Expressions

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/OBzeG_jpbZs
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Regular Expressions in Python

Regular expressions, often abbreviated as 'regex', are a powerful tool for matching patterns within text. They employ a unique syntax that is particularly useful for searching, parsing, and manipulating text data.

To utilize regular expressions in Python, you will first need to import the `re` module. Following this, the `re.compile()` function is used to compile a regular expression pattern. Various methods such as `search()`, `findall()`, and `sub()` can then be applied to this compiled pattern for different purposes.

## Importing the Regular Expressions Module

The first step in using regular expressions in Python is to import the `re` module. This module provides support for regular expressions in Python.

```python
import re
```

## Compiling a Regular Expression Pattern

Once the `re` module is imported, you can compile a regular expression pattern using the `re.compile()` function. This function transforms a regular expression pattern into a pattern object, which can be used for pattern matching with various methods.

```python
# any number of digits
pattern = re.compile(r"\d+")  
```

## Searching for a Match

The `search()` method is used to search for a match of the regular expression pattern in a string. If a match is found, it returns a match object. If no match is found, it returns `None`.

```python
string = "There are 3 dogs and 4 cats."
match = pattern.search(string)
print(match.group())  # Output: "3"
```

## Finding All Matches

The `findall()` method is used to find all matches of the regular expression pattern in a string. It returns a list of all matches.

```python
matches = pattern.findall(string)
print(matches)  # Output: ["3", "4"]
```

## Replacing Matches

The `sub()` method is used to replace all matches of the regular expression pattern in a string with a specified replacement string. It returns the string with the replacements.

```python
new_string = pattern.sub("X", string)
print(new_string)  
# Output: "There are X dogs and X cats."
```

In conclusion, regular expressions in Python provide a versatile tool for text manipulation. Whether you're searching for specific patterns, finding all instances of a pattern, or replacing patterns, regular expressions can simplify these tasks significantly.

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