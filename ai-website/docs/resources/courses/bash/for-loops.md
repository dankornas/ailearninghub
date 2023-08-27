---
title: For Loops
hide:
  - path
  - navigation
---

# Bash Scripting: For Loops

=== "Learning Material"

    <!-- <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe> -->

    ## What is a For Loop?

    A for loop is a control flow statement that allows code to be executed repeatedly. It is used when you want to perform a task for every item in a set. This set could be a list of numbers, strings, file names, or any other type of data that bash can handle.

    The basic structure of a for loop in bash is as follows:

    ```bash
    for variable in set
    do
        command1
        command2
        ...
        commandN
    done
    ```

    In this structure, `variable` is a placeholder that represents each item in the `set` as the loop iterates over it. The commands between `do` and `done` are executed for each item.

    ## Basic For Loop Example

    Let's start with a simple example. Suppose we want to print the numbers from 1 to 10. Here's how we can do it using a for loop:

    ```bash
    for current_number in {1..10}
    do
        echo "Current number is: $current_number"
        sleep 1
    done
    ```

    In this script, `current_number` is the variable that represents each item in the set `{1..10}`. The `echo` command prints the current number, and `sleep 1` pauses the script for one second before the next iteration. The loop ends after it has iterated through all the numbers in the set.

    ## Practical Use of a For Loop: Compressing Log Files

    Now, let's look at a more practical example. Suppose we have a directory full of log files, and we want to compress each of them using the `tar` command. Here's how we can do it using a for loop:

    ```bash
    for file in /var/log/*.log
    do
        tar -czvf "$file.tar.gz" "$file"
    done
    ```

    In this script, `file` is the variable that represents each log file in the `/var/log` directory. The `tar -czvf "$file.tar.gz" "$file"` command compresses each log file and creates a `.tar.gz` file for it. The loop ends after it has iterated through all the log files in the directory.

    ## Variable Naming in For Loops

    It's important to note that the variable used in the for loop can be named anything. It's common to see single-letter variable names in for loop examples online, but the variable name doesn't actually matter. For example, the following script is equivalent to the previous one:

    ```bash
    for f in /var/log/*.log
    do
        tar -czvf "$f.tar.gz" "$f"
    done
    ```

    In this script, `f` is the variable that represents each log file. Even though it's a different name, it serves the same purpose as `file` in the previous script.

    ## Conclusion

    For loops are a powerful tool in bash scripting. They allow you to automate tasks that need to be performed on every item in a set. Whether you're printing numbers, compressing log files, or doing something else entirely, for loops can make your scripts more efficient and easier to read.

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