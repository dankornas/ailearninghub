---
title: Introduction
hide:
  - path
  - navigation
---

# Bash Scripting: Introduction

=== "Learning Material"

    <iframe
        src="https://www.youtube.com/embed/2Gg6Seob5Mg"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        >
    </iframe>

    ## Introduction

    Bash scripting is a powerful tool used in the Unix environment to automate tasks and manipulate data. It allows you to execute commands from a file, making it an essential skill for system administrators and developers alike. This tutorial will guide you through the basics of bash scripting, providing code examples where necessary.

    ## Bash Scripts vs Python Scripts

    While Python is a popular language for scripting, bash scripting is often preferred in a Unix environment. The primary reason for this is that bash scripts use the shell as the interpreter. This means that bash scripts have access to the entire Unix toolset, providing a wide range of functionality.

    For example, consider a simple command to print a string in both Python and bash:

    Python:

    ```python
    print("Hello, World!")
    ```

    Bash:

    ```bash
    echo "Hello, World!"
    ```

    In this case, the bash script is simpler and more straightforward. It's also worth noting that bash scripts don't require any additional dependencies or modules to run, unlike Python scripts.

    ## Uses of Bash Scripting

    ### File Management

    Bash scripting is excellent for file management. It allows you to copy, update, and backup files on an automated basis. For example, you can create a bash script to backup a directory:

    ```bash
    #!/bin/bash
    tar -czf /path/to/backup.tar.gz /path/to/directory
    ```

    This script uses the `tar` command to create a compressed backup of a directory.

    ### Data Handling

    While Python is often the go-to language for data science, bash scripting can also handle data effectively. It's not as powerful as Python for complex statistical calculations, but it's more than capable for simple data manipulation tasks.

    For example, you can use a bash script to count the number of lines in a file:

    ```bash
    #!/bin/bash
    wc -l /path/to/file
    ```

    This script uses the `wc` command, which counts the number of lines, words, and bytes in a file.

    ### Task Automation

    Bash scripting is also great for automating tasks. You can write scripts to run programs, perform system maintenance, or even automate your daily tasks.

    For example, you can create a bash script to update your system (for Debian-based systems):

    ```bash
    #!/bin/bash
    sudo apt update && sudo apt upgrade -y
    ```

    This script will automatically update the package lists for upgrades and update all upgradable packages.

    ## Environment Setup

    You can write bash scripts on any Unix-based operating system, including Linux and macOS. You'll also need a text editor. This tutorial will use Sublime Text, but you can use any text editor you prefer.

    ## Creating Your First Shell Script

    Creating a bash script is straightforward. First, you'll need to specify the interpreter using a shebang (`#!`) at the start of your script. For bash scripts, this will be `#!/bin/bash`.

    Here's an example of a simple bash script:

    ```bash
    #!/bin/bash
    echo "Hello, World!"
    ```

    This script will print "Hello, World!" when run. To run the script, you'll need to make it executable using the `chmod` command:

    ```bash
    chmod +x script.sh
    ```

    Then, you can run the script:

    ```bash
    ./script.sh
    ```

    ## File Permissions

    Understanding file permissions is crucial when working with bash scripts. When you create a script, you'll need to make it executable for it to run. You can do this with the `chmod` command, as shown above.

    You can also change the permissions of a script to restrict who can read, write, or execute it. For example, to remove the execute permission from a script, you can use:

    ```bash
    chmod -x script.sh
    ```

    ## Conclusion

    Bash scripting is a powerful tool for any Unix user. It allows you to automate tasks, manage files, and manipulate data. By understanding the basics of bash scripting, you can start to harness the power of the Unix shell.

    Remember, the key to good bash scripting is practice. Try to automate some of your daily tasks with bash scripts, or solve problems using bash. The more you use it, the more comfortable you'll become. Happy scripting!

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
