---
title: Control Statements
hide:
  - path
  - navigation
---

# Bash Scripting: Control Statements

=== "Learning Material"

    <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe>

    ## If Statements in Bash

    One of the most fundamental concepts in any programming language is the if statement. In Bash, if statements allow us to make decisions in our scripts. We can execute different pieces of code based on certain conditions.

    Here's a simple example of an if statement in Bash:

    ```bash
    #!/bin/bash

    # Declare a variable
    my_num=200

    # If statement
    if [ $my_num -eq 200 ]
    then
        echo "The condition is true"
    fi
    ```

    In this script, we first declare a variable `my_num` and assign it the value 200. Then we have an if statement that checks if `my_num` is equal to 200. If the condition is true, it echoes "The condition is true".

    The `-eq` inside the brackets stands for "equal". There are different checks that we can perform within the brackets. For example, `-ne` stands for "not equal", `-gt` stands for "greater than", and `-lt` stands for "less than".

    ## Else Statements in Bash

    In addition to if statements, Bash also provides else statements. An else statement can be combined with an if statement to execute a piece of code when the if condition is not met.

    Here's an example of an if-else statement in Bash:

    ```bash
    #!/bin/bash

    # Declare a variable
    my_num=300

    # If-else statement
    if [ $my_num -eq 200 ]
    then
        echo "The condition is true"
    else
        echo "The condition is false"
    fi
    ```

    In this script, the if condition checks if `my_num` is equal to 200. If the condition is true, it echoes "The condition is true". If the condition is not met (i.e., `my_num` is not equal to 200), the else statement is executed, and it echoes "The condition is false".

    ## Checking the Presence of Files

    Bash allows us to check for the presence of files on the file system. This can be done using the `-f` option in an if statement. The `-f` option checks if a certain file exists and is a regular file.

    Here's an example:

    ```bash
    #!/bin/bash

    # File to check
    file="~/my_file"

    # If statement to check if file exists
    if [ -f $file ]
    then
        echo "The file exists"
    else
        echo "The file does not exist"
    fi
    ```

    In this script, we're checking if the file `my_file` exists in the home directory. If it does, the script echoes "The file exists". If it doesn't, the script echoes "The file does not exist".

    ## Checking the Presence of Commands

    In addition to checking for the presence of files, we can also check if a certain command is available on the system. This can be done using the `command -v` command in an if statement.

    Here's an example:

    ```bash
    #!/bin/bash

    # Command to check
    cmd="htop"

    # If statement to check if command is available
    if command -v $cmd >/dev/null
    then
        echo "$cmd is available"
    else
        echo "$cmd is not available"
    fi
    ```

    In this script, we're checking if the command `htop` is available on the system. If it is, the script echoes "htop is available". If it's not, the script echoes "htop is not available".

    ## Conclusion

    Bash scripting is a powerful tool for automating tasks on Linux and Unix-like operating systems. By understanding concepts like variables, if statements, else statements, and how to check for the presence of files and commands, you can write scripts that automate complex tasks and make your life easier.


=== "All Lessons"
    {nav}

=== "Practice Questions"
    
    What is the role of the "echo" command in bash scripting?

    a. To read input from the user. <br>
    b. To display information on the screen. <br>
    c. To save information for later use. <br>
    d. To delete information from the system. <br>

    ??? note "Answer"
        b

    What does the "read" command do in bash scripting?

    a. It deletes information from the system. <br>
    b. It saves information for later use. <br>
    c. It reads input from the user. <br>
    d. It creates new commands. <br>

    ??? note "Answer"
        c

    What is the purpose of the "if" statement in bash scripting?

    a. To create a loop. <br>
    b. To perform conditional operations. <br>
    c. To print information on the screen. <br>
    d. To delete information from the system. <br>

    ??? note "Answer"
        b

    What is the role of a "for" loop in bash scripting?

    a. To perform operations repeatedly. <br>
    b. To read input from the user. <br>
    c. To print information on the screen. <br>
    d. To delete information from the system. <br>

    ??? note "Answer"
        a

    What is the purpose of the "rm" command in bash scripting?

    a. To save information for later use. <br>
    b. To print information on the screen. <br>
    c. To create new commands. <br>
    d. To delete files from the system. <br>

    ??? note "Answer"
        d

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