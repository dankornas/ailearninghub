---
title: While Loops
hide:
  - path
  - navigation
---

# Bash Scripting: While Loops

=== "Learning Material"

    <!-- <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe> -->

    ## What is a While Loop?

    A while loop is a control flow statement that allows code to be executed repeatedly based on a given condition. The code inside the loop is executed as long as the condition evaluates to true. Once the condition becomes false, the loop terminates.

    The basic structure of a while loop in bash is as follows:

    ```bash
    while [ condition ]
    do
        command1
        command2
        ...
        commandN
    done
    ```

    In this structure, `condition` is a test or command that returns a status. If the status is zero (which means true in a shell scripting context), the commands between `do` and `done` are executed. The loop continues to execute until the condition returns a non-zero status (which means false).

    ## Basic While Loop Example

    Let's start with a simple example. Suppose we want to print the numbers from 1 to 10. Here's how we can do it using a while loop:

    ```bash
    counter=1
    while [ $counter -le 10 ]
    do
        echo "Current number is: $counter"
        ((counter++))
    done
    ```

    In this script, `counter` is a variable that starts at 1. The condition in the while loop checks if `counter` is less than or equal to 10. The `echo` command prints the current number, and `((counter++))` increments the counter by 1 at each iteration. The loop ends after `counter` exceeds 10.

    ## Practical Use of a While Loop: Reading a File Line by Line

    Now, let's look at a more practical example. Suppose we have a text file, and we want to read it line by line. Here's how we can do it using a while loop:

    ```bash
    while IFS= read -r line
    do
        echo "Line: $line"
    done < file.txt
    ```

    In this script, `line` is a variable that represents each line in the file. The `IFS=` and `-r` options ensure that the read command reads each line exactly as it is, preserving whitespace and backslashes. The `echo` command prints each line. The loop ends after it has read all lines in the file.

    ## Using While Loops for User Input

    While loops can also be used to handle user input in interactive scripts. For example, you can use a while loop to keep asking for user input until a valid input is received:

    ```bash
    while :
    do
        read -p "Enter a number: " number
        if [[ $number =~ ^[0-9]+$ ]]
        then
            break
        else
            echo "Invalid input. Please enter a number."
        fi
    done
    ```

    In this script, the loop continues indefinitely because the condition is simply `:` (which always evaluates to true). The `read -p` command asks for user input, and the `if` statement checks if the input is a number. If the input is a number, the `break` command terminates the loop. If the input is not a number, an error message is printed, and the loop continues.

    ## Conclusion

    While loops are a versatile tool in bash scripting. They allow you to automate tasks that need to be performed repeatedly until a certain condition is met. Whether you're printing numbers, reading files, or handling user input, while loops can make your scripts more efficient and easier to manage.

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