---
title: Functions
hide:
  - path
  - navigation
---

# Bash Scripting: Functions

=== "Learning Material"

    <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe>

    ## What is a Function?

    A function is a named section of a program that performs a specific task. In bash scripting, functions allow you to group commands for easy reuse. This can make your scripts more organized, more readable, and easier to maintain.

    The basic structure of a function in bash is as follows:

    ```bash
    function_name () {
        command1
        command2
        ...
        commandN
    }
    ```

    In this structure, `function_name` is the name of the function, and `command1` to `commandN` are the commands that the function will execute when it is called.

    ## Basic Function Example

    Let's start with a simple example. Suppose we want to create a function that prints a greeting message. Here's how we can do it:

    ```bash
    greet () {
        echo "Hello, world!"
    }

    # Call the function
    greet
    ```

    In this script, `greet` is a function that prints "Hello, world!". After the function is defined, it is called by simply writing its name followed by parentheses.

    ## Functions with Parameters

    Functions can also take parameters. Parameters are variables that are passed to the function when it is called. Inside the function, these parameters are accessed as `$1`, `$2`, `$3`, etc., in the order they were passed.

    Here's an example of a function that takes two parameters:

    ```bash
    add () {
        echo "The sum is: $(($1 + $2))"
    }

    # Call the function with two parameters
    add 5 7
    ```

    In this script, `add` is a function that takes two parameters and prints their sum. The parameters are accessed inside the function as `$1` and `$2`.

    ## Functions that Return Values

    In bash, functions don't return values like they do in other programming languages. However, you can simulate a return by using the `return` command to set the function's exit status. The exit status is a numerical value that represents the success (0) or failure (non-zero) of the last command executed in the function.

    Here's an example of a function that "returns" the sum of two numbers:

    ```bash
    add () {
    return $(($1 + $2))
    }

    # Call the function
    add 5 7

    # Print the "return value"
    echo "The sum is: $?"
    ```

    In this script, `add` is a function that "returns" the sum of two numbers by setting the exit status to their sum. After the function is called, the "return value" is accessed using `$?`.

    ## Using Functions to Simplify Scripts

    Functions can be particularly useful for simplifying your scripts. If you find yourself repeating the same set of commands multiple times in your script, you can put these commands into a function and then call the function instead.

    For example, consider a script where you are checking the exit status of a command multiple times:

    ```bash
    command1
    if [ $? -ne 0 ]; then
        echo "An error occurred. Exiting."
        exit 1
    fi

    command2
    if [ $? -ne 0 ]; then
        echo "An error occurred. Exiting."
        exit 1
    fi

    command3
    if [ $? -ne 0 ]; then
        echo "An error occurred. Exiting."
        exit 1
    fi
    ```

    You can simplify this script by creating a function for the exit status check:

    ```bash
    check_exit_status() {
        if [ $? -ne 0 ]; then
            echo "An error occurred. Exiting."
            exit 1
        fi
    }

    command1
    check_exit_status

    command2
    check_exit_status

    command3
    check_exit_status
    ```

    In this revised script, after each command, we call the `check_exit_status` function. This makes the script shorter and easier to read and maintain.

    ## Conclusion

    Functions are a powerful tool in Bash scripting that can help you to write cleaner, more maintainable scripts. By grouping a set of commands into a function, you can avoid repeating the same commands multiple times in your script. Instead, you can call the function whenever you need to execute those commands. This not only makes your scripts shorter and easier to read, but also makes them easier to maintain, as you only need to update a command in one place if it needs to be changed.

=== "All Lessons"
    {nav}

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