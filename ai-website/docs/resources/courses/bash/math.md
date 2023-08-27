---
title: Basic Math
hide:
  - path
  - navigation
---

# Bash Scripting: Basic Math

=== "Learning Material"

    <!-- <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe> -->

    ## Introduction

    When it comes to bash scripting, there's no shortage of things to do. From built-in commands to if statements, and many other functions, bash scripting offers a wide range of possibilities. In this tutorial, we're going to focus on math functions. While they may not be something you'll use a lot, understanding them will help you achieve well-rounded knowledge with bash.

    ## Understanding Math Functions in Bash

    Math functions in bash are handled differently than in other programming languages. For example, in Python, if you wanted to add 30 plus 10, you could simply write `30 + 10`. However, this won't work in bash. In bash, we have the `expr` command, which stands for "evaluate expressions". This command lets bash know that what you want to do is evaluate a mathematical expression.

    ### Addition and Subtraction

    To add two numbers together in bash, you can use the `expr` command followed by the two numbers with a plus symbol in between them. For example:

    ```bash
    expr 30 + 10
    ```

    This will output `40`, which is the result of the addition.

    Subtraction works in a very similar way. You simply replace the plus symbol with a minus symbol. For example:

    ```bash
    expr 30 - 10
    ```

    This will output `20`, which is the result of the subtraction.

    ### Division

    To perform division, you replace the minus symbol with a forward slash. For example:

    ```bash
    expr 30 / 10
    ```

    This will output `3`, which is the result of the division.

    ### Multiplication

    Multiplication is a bit tricky in bash because the asterisk (`*`) is a wildcard character in bash, meaning it refers to everything. If you try to use it directly for multiplication, it won't work. For example, `expr 100 * 4` will not work as expected.

    To use the asterisk for multiplication, you need to escape it with a backslash (`\`). For example:

    ```bash
    expr 100 \* 4
    ```

    This will output `400`, which is the result of the multiplication.

    ## Using Variables in Math Functions

    In the previous lesson, we went over variables. One thing you can do with variables is use them in math functions. For example, you can create a variable and add a number to it:

    ```bash
    my_num1=100
    expr $my_num1 + 50
    ```

    This will output `150`, which is the result of adding `50` to the value of the variable `my_num1`.

    You can also add two variables together:

    ```bash
    my_num2=50
    expr $my_num1 + $my_num2
    ```

    This will output `150`, which is the result of adding the values of the variables `my_num1` and `my_num2`.

    ## Conclusion

    In this tutorial, we went over some basic math functions in bash. While they might not seem all that useful right now, they are one of those things that you'll probably use later on. If nothing else, you now know how to evaluate expressions on the command line, which might be especially useful if you're coming from a different shell or a different programming language.

=== "All Lessons"
    {nav}

=== "Practice Questions"

    How do you add two numbers in bash scripting?

    a. 30 + 10 <br>
    b. add 30 10 <br>
    c. expr 30 + 10 <br>
    d. 30 plus 10 <br>

    ??? note "Answer"
        c

    How do you perform division in bash scripting?

    a. 30 / 10 <br>
    b. divide 30 10 <br>
    c. expr 30 / 10 <br>
    d. 30 divide 10 <br>

    ??? note "Answer"
        c

    How do you perform multiplication in bash scripting?

    a. 100 * 4 <br>
    b. multiply 100 4 <br>
    c. expr 100 \* 4 <br>
    d. 100 multiply 4 <br>

    ??? note "Answer"
        c

    What does the asterisk (*) symbol mean in bash?

    a. It means multiplication. <br>
    b. It means division. <br>
    c. It is a wildcard character that refers to everything. <br>
    d. It is used to denote a variable. <br>

    ??? note "Answer"
        c

    How do you add a number to a variable in bash scripting?

    a. my_num1 + 50 <br>
    b. add $my_num1 50 <br>
    c. expr $my_num1 + 50 <br>
    d. $my_num1 add 50 <br>

    ??? note "Answer"
        c

---

!!! note "Version 1.0"

    This is currently an early version of the learning material and it will be updated over time with more detailed information.

    A video will be provided with the learning material as well.

    Be sure to subscribe to stay up-to-date with the latest updates.

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