---
title: Variables
slug: Var
hide:
  - path
  - navigation
---

# Bash Scripting: Variables

=== "Learning Material"

    <!-- <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe> -->

    ## Introduction to Variables

    In Bash scripting, declaring a variable is straightforward. You simply type the name you want for your variable, include the equal sign with no space, and then in quotes, you can put some text or even a number. For example:

    ```bash
    my_name="Dan"
    ```

    Here, we've created a variable named `my_name` and set it equal to "Dan". This was done directly on the command line, underscoring the fact that there's not much difference between entering commands on the command line and adding commands to a script. A script will contain commands that the underlying command line interpreter understands, and commands on the command line can be used inside a script or as a standalone command interchangeably.

    ## Referencing Variables

    To reference a variable in Bash, we use the `echo` command. In the previous lesson, we used the `echo` command inside a script to print "Hello, world!" to the screen. We can also use `echo` to print the contents of a variable. However, when referencing a variable in Bash, we have to include a dollar sign in front of the name of the variable. Without the dollar sign, Bash will not interpret it as a variable. For example:

    ```bash
    echo $my_name
    ```

    This will print "Dan", the value we assigned to the `my_name` variable. If we had simply typed `echo my_name`, Bash would have printed "my_name", treating it as a string rather than a variable.

    ## Understanding the Dollar Sign in Variable Reference

    You might be wondering why Bash requires a dollar sign in front of a variable name to reference that variable. The dollar sign helps Bash distinguish between a command and a variable. For example, if we create a variable named `ls` and set it equal to "Hello, again", it won't interfere with the `ls` command:

    ```bash
    ls="Hello, again"
    echo $ls
    ```

    The `echo $ls` command will print "Hello, again", not the output of the `ls` command. This distinction helps us avoid name collisions and is mandatory when referencing a variable.

    ## Variable Persistence

    It's important to note that when you declare a variable in Bash, it is tied to that session. Once you close the window, the session's gone, and any variables that you might have declared are wiped out. They don't survive a log out, log in, or an exit of the shell. They're going to be within that session only.

    However, when we include variables inside a script, every time the script is run, it declares the variables, so we don't need to do that manually. This allows us to persist the variables.

    ## Using Variables in Scripts

    Let's return to our script and include variables inside the script. Here's an example:

    ```bash
    #!/bin/bash

    my_name="Dan"
    my_age=40

    echo "Hello, my name is $my_name."
    echo "I'm $my_age years old."
    ```

    In this script, we first set up two variables, `my_name` and `my_age`, and gave them values. Then, we used the `echo` command to print sentences that include these variables. When we run this script, it will print:

    ```vbnet
    Hello, my name is Dan.
    I'm 40 years old.
    ```

    ## The Importance of Double Quotes in Echo Statements

    In the echo statements in our script, we used double quotes. This is because Bash treats variables inside double quotes as variables and prints their contents, not their names. If we had used single quotes, Bash would have printed the names of the variables, not their contents.

    ## Capturing the Output of a Command in a Variable

    Another useful feature of variables in Bash scripting is that they can capture the output of a command. For example, we can create a variable that stores the current date:

    ```bash
    now=$(date)
    echo "The system time and date is $now."
    ```

    In this script, we created a variable named `now` and set it equal to the output of the `date` command. Then, we used the `echo` command to print a sentence that includes the `now` variable. When we run this script, it will print the current system time and date.

    ## Environment Variables

    In addition to the variables we declare ourselves, there are many default variables that are always declared in our environment. For example, the `USER` variable is always going to contain the name of the user that you're currently logged in as. We can reference these environment variables in our scripts in the same way as our own variables. For example:

    ```bash
    echo "Your username is $USER."
    ```

    This will print "Your username is " followed by your username.

    ## Conclusion

    Variables in Bash scripting are powerful tools that enable us to save information for later use and avoid retyping the same thing over and over again. They can store strings, numbers, or the output of commands, and they can be used in echo statements, commands, and other scripts. By understanding and using variables, we can make our scripts more dynamic, efficient, and easy to maintain.

    In the next tutorial, we will continue our journey into Bash scripting. Stay tuned!

=== "All Lessons"
    {nav}

=== "Practice Questions"

    What is the purpose of using variables in bash scripting?

    a. To save information for later use. <br>
    b. To print information on the screen. <br>
    c. To create new commands. <br>
    d. To delete information from the system. <br>

    ??? note "Answer"
        a

    How do you declare a variable in bash?

    a. By typing the variable name, followed by an equal sign, and then the value. <br>
    b. By typing the variable name, followed by a colon, and then the value. <br>
    c. By typing the variable name, followed by a comma, and then the value. <br>
    d. By typing the variable name, followed by a semicolon, and then the value. <br>

    ??? note "Answer"
        a

    How do you reference a variable in bash?

    a. By typing the variable name. <br>
    b. By typing the variable name with a dollar sign in front. <br>
    c. By typing the variable name with a hashtag in front. <br>
    d. By typing the variable name with an asterisk in front. <br>

    ??? note "Answer"
        b

    What happens to variables when you close the terminal session in bash?

    a. They are saved for the next session. <br>
    b. They are deleted. <br>
    c. They are moved to a different session. <br>
    d. They are converted into commands. <br>

    ??? note "Answer"
        b

    What is the best practice for naming your own variables in bash?

    a. Use uppercase names. <br>
    b. Use lowercase names. <br>
    c. Use names with special characters. <br>
    d. Use names with numbers only. <br>

    ??? note "Answer"
        b

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