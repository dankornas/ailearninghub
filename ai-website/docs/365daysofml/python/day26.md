# Day 26: Python Modules

<iframe width="360" height="655" 
src="https://www.youtube.com/embed/YluGFwaE7UU
?rel=0&vq=hd1080" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Understanding Python Modules and Packages

Python modules are files containing Python code, which can be imported into other Python files. This feature facilitates code reuse and logical organization of code. To import a module, use the 'import' statement followed by the module's name. Once imported, the module's code can be accessed using dot notation, such as 'module_name.function_name'.

Packages in Python offer a higher level of organization by grouping related modules together. Essentially, they are directories containing one or more module files and a special '**init**.py' file. To import a module from a package, use the 'from package_name import module_name' syntax.

## Importing a Python Module

Consider a Python file named 'module.py' with a function 'greet(name)'. This file can be imported as a module in another Python file as follows:

```python
# module.py 
def greet(name):
    print(f"Hello, {name}!") 

# main.py 
import module 
module.greet("John")  
# Output: "Hello, John!"
```

In the above example, the 'module.py' file is imported into 'main.py', and the 'greet' function is accessed using dot notation.

## Importing a Module from a Python Package

Now consider a Python package named 'package' with a module file 'module.py' containing the 'greet(name)' function. This module can be imported from the package as follows:

```python
# package/module.py 
def greet(name):
    print(f"Hello, {name}!") 

# main.py
from package.module import greet 
greet("John")  
# Output: "Hello, John!"
```

In this example, the 'module.py' file is imported from the 'package' directory, and the 'greet' function is accessed directly.

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